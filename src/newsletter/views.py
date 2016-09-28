from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .counter import *

from .forms import *
from .models import *


   
# views go here.

# sitemap for google
def sitemap(request):
	   
	return render(request, "sitemap.xml", {})

# --PAGES--

# home page view
def home(request):	
	if  not request.user.is_authenticated() and not request.user.is_staff:
		viewCounter("home_page")
		
	return render(request, "home.html", {})

# about page view
def about(request):
	if  not request.user.is_authenticated() and not request.user.is_staff:
		viewCounter("about_page")
	return render(request, "pages/about.html", {})
	
# -- FORMS--

# business page view
def business(request):
	if  not request.user.is_authenticated() and not request.user.is_staff:
		viewCounter("business_page")
	title = 'Contact Us About Business'
	title_align_center = True
	form = BusinessContactForm(request.POST or None)
	if request.method == "POST":
		pDict = request.POST.copy() 
		form = BusinessContactForm(pDict) #if not valid shows error with previous post values in corresponding field
			
		if form.is_valid():
			
			form_email = form.cleaned_data.get("email")
			form_message = form.cleaned_data.get("message")
			form_full_name = form.cleaned_data.get("full_name")
			form_phone_number = form.cleaned_data.get("phone_number")
			form_business_name = form.cleaned_data.get("business_name")

			# print email, message, full_name
			subject = 'Site Business Contact Form'
			from_email = settings.EMAIL_HOST_USER
			to_email = [settings.EMAIL_HOST_USER]

			contact_message = "Name = %s | Business =  %s | Message = %s | Email =  %s | Phone =  %s"%( 
					form_full_name,
					form_business_name, 
					form_message, 
					form_email,
					form_phone_number)

			if (send_mail(subject, contact_message, from_email,to_email, fail_silently=False)):
				form = BusinessContactForm()
				context = {
			"form": form,
			"title": "Thank you",
			"title_align_center": title_align_center,
			}
			return render(request, "pages/business.html", context)

	context = {
		"form": form,
		"title": title,
		"title_align_center": title_align_center,
	}
	return render(request, "pages/business.html", context)

# business contact view
def business_contact(request):
	if  not request.user.is_authenticated() and not request.user.is_staff:
		viewCounter("business_page")

	title = 'Contact Us About Business'
	title_align_center = True
	form = BusinessContactForm(request.POST or None)

	if request.method == "POST":
		pDict = request.POST.copy() 
		form = BusinessContactForm(pDict) #if not valid shows error with previous post values in corresponding field
		
		if form.is_valid():
			
			form_email = form.cleaned_data.get("email")
			form_message = form.cleaned_data.get("message")
			form_full_name = form.cleaned_data.get("full_name")
			form_phone_number = form.cleaned_data.get("phone_number")
			form_business_name = form.cleaned_data.get("business_name")

			# print email, message, full_name
			subject = 'Site Business Contact Form'
			from_email = settings.EMAIL_HOST_USER
			to_email = [settings.EMAIL_HOST_USER]

			contact_message = "Name = %s | Business =  %s | Message = %s | Email =  %s | Phone =  %s"%( 
					form_full_name,
					form_business_name, 
					form_message, 
					form_email,
					form_phone_number)
	   
			if (send_mail(subject, contact_message, from_email,to_email, fail_silently=False)):
				form = BusinessContactForm()
				context = {
			"form": form,
			"title": "Thank you",
			"title_align_center": title_align_center,
			}
			return render(request, "pages/business.html", context)
	context = {
		"form": form,
		"title": title,
		"title_align_center": title_align_center,
	}
	return render(request, "forms/business_contact.html", context)

# signup view
def signup(request):
	pieSignUpArr = signUpPie();

	title = 'Sign up to be notified on all TikbiT projects!'
	title_align_center = True
	form = SignUpForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	}
	if form.is_valid():
		
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name		
		instance.save()
		context = {
			"title": "Thank you",
			"squiggles_sign": pieSignUpArr[0],
			"herbs_sign": pieSignUpArr[1],
			"friends_sign": pieSignUpArr[2],
			"fitness_sign": pieSignUpArr[3],
			"goodNews_sign": pieSignUpArr[4],
			"ranger_sign": pieSignUpArr[5]
		}

	if request.user.is_authenticated() and request.user.is_staff:
		
		queryset = SignUp.objects.all().order_by('-timestamp')		
		context = {
			"queryset": queryset,
		}


	return render(request, "forms/signup.html", context)

# contact page view
def contact(request):
	if  not request.user.is_authenticated() and not request.user.is_staff:
		viewCounter("contact_page")
	title = 'Contact Us'
	title_align_center = True
	form = ContactForm(request.POST or None)

	if request.method == "POST":
		pDict = request.POST.copy() 
		form = ContactForm(pDict)
		if form.is_valid():           
		
			form_email = form.cleaned_data.get("email")
			form_message = form.cleaned_data.get("message")
			form_full_name = form.cleaned_data.get("full_name")
			form_phone_number = form.cleaned_data.get("phone_number")

			# print email, message, full_name
			subject = 'Site contact form'
			from_email = settings.EMAIL_HOST_USER
			to_email = [settings.EMAIL_HOST_USER]
			contact_message = "%s: %s via %s | %s"%( 
					form_full_name, 
					form_message, 
					form_email,
					form_phone_number)
	   
			if (send_mail(subject, contact_message, from_email,to_email, fail_silently=False)):               
				form = ContactForm()
				context = {
			"form": form,
			"title": "Thank you",
			"title_align_center": title_align_center,
			}
			return render(request, "forms/forms.html", context)

	context = {
		"form": form,
		"title": title,
		"title_align_center": title_align_center,
	}
	return render(request, "forms/forms.html", context)

# --APPS--

# projects page view
def projects(request):
	if  not request.user.is_authenticated() and not request.user.is_staff:
		viewCounter("apps_page")
	
	# For Pie Chart
	pieSignUpArr = signUpPie();	
	title = 'Sign Up For All!'
	form = SignUpForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	}
	if form.is_valid():
		
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save()
		context = {
			"title": "Thank you",
			"squiggles_sign": pieSignUpArr[0],
			"herbs_sign": pieSignUpArr[1],
			"friends_sign": pieSignUpArr[2],
			"fitness_sign": pieSignUpArr[3],
			"goodNews_sign": pieSignUpArr[4],
			"ranger_sign": pieSignUpArr[5]
		}

	if request.user.is_authenticated() and request.user.is_staff:
		
		queryset = SignUp.objects.all().order_by('-timestamp') 
		context = {
			"queryset": queryset,
		}

	return render(request, "apps/projects.html", context)

# friends page view
def friends(request):
	if not request.user.is_authenticated() and not request.user.is_staff:
		viewCounter("friends_page")
	pieSignUpArr = signUpPie();	
	title = 'Sign Up Now'
	form = SignUpFormFriends(request.POST or None)
	context = {
		"title": title,
		"form": form
	}
	if form.is_valid():
		
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save()
		context = {
			"title": "Thank you",
			"squiggles_sign": pieSignUpArr[0],
			"herbs_sign": pieSignUpArr[1],
			"friends_sign": pieSignUpArr[2],
			"fitness_sign": pieSignUpArr[3],
			"goodNews_sign": pieSignUpArr[4],
			"ranger_sign": pieSignUpArr[5]
		}

	if request.user.is_authenticated() and request.user.is_staff:

		queryset = SignUp_Friends.objects.all().order_by('-timestamp')
		context = {
			"queryset": queryset
		}

	return render(request, "apps/titles/friends.html", context)

# fitness page view
def fitness(request):
	if  not request.user.is_authenticated() and not request.user.is_staff:
		viewCounter("fitness_page")

	pieSignUpArr = signUpPie();

	title = 'Sign Up Now'
	form = SignUpFormFitness(request.POST or None)
	context = {
		"title": title,
		"form": form
	}
	if form.is_valid():
		
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save()
		context = {
			"title": "Thank you",
			"squiggles_sign": pieSignUpArr[0],
			"herbs_sign": pieSignUpArr[1],
			"friends_sign": pieSignUpArr[2],
			"fitness_sign": pieSignUpArr[3],
			"goodNews_sign": pieSignUpArr[4],
			"ranger_sign": pieSignUpArr[5]
		}

	if request.user.is_authenticated() and request.user.is_staff:

		queryset = SignUp_Fitness.objects.all().order_by('-timestamp')
		context = {
			"queryset": queryset
		}

	return render(request, "apps/titles/fitness.html", context)

# herbs page view
def herbs(request):
	if  not request.user.is_authenticated() and not request.user.is_staff:
		viewCounter("herbs_page")

	pieSignUpArr = signUpPie();
	title = 'Sign Up Now'
	form = SignUpFormHerbs(request.POST or None)
	context = {
		"title": title,
		"form": form
	}
	if form.is_valid():
		
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save()
		context = {
			"title": "Thank you",
			"squiggles_sign": pieSignUpArr[0],
			"herbs_sign": pieSignUpArr[1],
			"friends_sign": pieSignUpArr[2],
			"fitness_sign": pieSignUpArr[3],
			"goodNews_sign": pieSignUpArr[4],
			"ranger_sign": pieSignUpArr[5]
		}

	if request.user.is_authenticated() and request.user.is_staff:

		queryset = SignUp_Herbs.objects.all().order_by('-timestamp') 
		context = {
			"queryset": queryset
		}

	return render(request, "apps/titles/herbs.html", context)

# goodnews page view
def goodnews(request):
	if  not request.user.is_authenticated() and not request.user.is_staff:
		viewCounter("goodnews_page")

	pieSignUpArr = signUpPie();
	title = 'Sign Up Now'
	form = SignUpFormGoodNews(request.POST or None)
	context = {
		"title": title,
		"form": form
	}
	if form.is_valid():
		
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save()
		context = {
			"title": "Thank you",
			"squiggles_sign": pieSignUpArr[0],
			"herbs_sign": pieSignUpArr[1],
			"friends_sign": pieSignUpArr[2],
			"fitness_sign": pieSignUpArr[3],
			"goodNews_sign": pieSignUpArr[4],
			"ranger_sign": pieSignUpArr[5]
		}

	if request.user.is_authenticated() and request.user.is_staff:		

		queryset = SignUp_GoodNews.objects.all().order_by('-timestamp')
		context = {
			"queryset": queryset
		}

	return render(request, "apps/titles/goodnews.html", context)

# --GAMES--

# games overview page view
def games(request):
	if  not request.user.is_authenticated() and not request.user.is_staff:
		viewCounter("games_page")

	pieSignUpArr = signUpPie();
	title = 'Sign Up For All!'
	form = SignUpForm(request.POST or None)
	context = {
		"title": title,
		"form": form
	}
	if form.is_valid():
		
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save()
		context = {
			"title": "Thank you",
			"squiggles_sign": pieSignUpArr[0],
			"herbs_sign": pieSignUpArr[1],
			"friends_sign": pieSignUpArr[2],
			"fitness_sign": pieSignUpArr[3],
			"goodNews_sign": pieSignUpArr[4],
			"ranger_sign": pieSignUpArr[5]
		}

	if request.user.is_authenticated() and request.user.is_staff:

		queryset = SignUp.objects.all().order_by('-timestamp')
		context = {
			"queryset": queryset
		}

	return render(request, "games/game_overview.html", context)

# squiggles page view
def squiggles(request):
	if  not request.user.is_authenticated() and not request.user.is_staff:
		viewCounter("squiggles_page")

	pieSignUpArr = signUpPie();

	title = 'Sign Up Now'
	form = SignUpFormSquiggles(request.POST or None)
	context = {
		"title": title,
		"form": form
	}
	if form.is_valid():

		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save()
		context = {
			"title": "Thank you",
			"squiggles_sign": pieSignUpArr[0],
			"herbs_sign": pieSignUpArr[1],
			"friends_sign": pieSignUpArr[2],
			"fitness_sign": pieSignUpArr[3],
			"goodNews_sign": pieSignUpArr[4],
			"ranger_sign": pieSignUpArr[5]
		}

	if request.user.is_authenticated() and request.user.is_staff:

		queryset = SignUp_Squiggles.objects.all().order_by('-timestamp')
		context = {
			"queryset": queryset
		}

	return render(request, "games/titles/squiggles.html", context)

# ranger page view
def ranger(request):
	if  not request.user.is_authenticated() and not request.user.is_staff:
		viewCounter("ranger_page")

	pieSignUpArr = signUpPie();
	title = 'Sign Up Now'
	form = SignUpFormRanger(request.POST or None)
	context = {
		"title": title,
		"form": form
	}
	if form.is_valid():
		
		instance = form.save(commit=False)
		full_name = form.cleaned_data.get("full_name")
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save()
		context = {
			"title": "Thank you",
			"squiggles_sign": pieSignUpArr[0],
			"herbs_sign": pieSignUpArr[1],
			"friends_sign": pieSignUpArr[2],
			"fitness_sign": pieSignUpArr[3],
			"goodNews_sign": pieSignUpArr[4],
			"ranger_sign": pieSignUpArr[5]
		}

	if request.user.is_authenticated() and request.user.is_staff:

		queryset = SignUp_Ranger.objects.all().order_by('-timestamp')
		context = {
			"queryset": queryset
		}

	return render(request, "games/titles/ranger.html", context)

# --admin overview terminal--
def terminal(request):
	all_sign = signUpCounterNum();   
	pieSignUpArr= signUpPie();
	allViewArr = allViewCounter();

	#-- clears the pages view count piechart and sets it to 0 --
	form = viewZeroForm(request.POST or None)

	if form.is_valid():
			form_zero = form.cleaned_data.get("zero")
			if (form_zero == True):

				allZero()
				allViewArr = allViewCounter();

			form = viewZeroForm(request.POST or None)
			context = {
				"form": form,
				"all_sign": all_sign,
				"squiggles_sign": pieSignUpArr[0],
				"herbs_sign": pieSignUpArr[1],
				"friends_sign": pieSignUpArr[2],
				"fitness_sign": pieSignUpArr[3],
				"goodNews_sign": pieSignUpArr[4],
				"ranger_sign": pieSignUpArr[5],
				"homeView": allViewArr[0],
				"appView": allViewArr[1],
				"businessView": allViewArr[2],
				"contactView": allViewArr[3],
				"fitnessView": allViewArr[4],
				"friendsView": allViewArr[5],
				"gamesView": allViewArr[6],
				"goodnewsView": allViewArr[7],
				"herbsView": allViewArr[8],
				"squiggles": allViewArr[9],
				"aboutView": allViewArr[10],
				"labView": allViewArr[11],
				"rangerView": allViewArr[12]
			}
	    
	page = "home.html"
	if request.user.is_authenticated() and request.user.is_staff:
		page = "admin/terminal.html"
	
	context = {
		"form": form,
		"all_sign": all_sign,
		"squiggles_sign": pieSignUpArr[0],
		"herbs_sign": pieSignUpArr[1],
		"friends_sign": pieSignUpArr[2],
		"fitness_sign": pieSignUpArr[3],
		"goodNews_sign": pieSignUpArr[4],
		"ranger_sign": pieSignUpArr[5],
		"homeView": allViewArr[0],
		"appView": allViewArr[1],
		"businessView": allViewArr[2],
		"contactView": allViewArr[3],
		"fitnessView": allViewArr[4],
		"friendsView": allViewArr[5],
		"gamesView": allViewArr[6],
		"goodnewsView": allViewArr[7],
		"herbsView": allViewArr[8],
		"squiggles": allViewArr[9],
		"aboutView": allViewArr[10],
		"labView": allViewArr[11],
		"rangerView": allViewArr[12]        
	}    
	return render(request, page, context)

# -- FOR TESTING--
def test(request):
	page = "home.html"
	if request.user.is_authenticated() and request.user.is_staff:
		page = "admin/test.html"
	
	return render(request, page, {})

# lab page view 
def lab(request):
	if not request.user.is_authenticated() and not request.user.is_staff:
		viewCounter("lab_page") 

	all_sign = signUpCounterNum();   
	pieSignUpArr= signUpPie();
	allViewArr = allViewCounter();
	
	context = {
		"all_sign": all_sign,
		"squiggles_sign": pieSignUpArr[0],
		"herbs_sign": pieSignUpArr[1],
		"friends_sign": pieSignUpArr[2],
		"fitness_sign": pieSignUpArr[3],
		"goodNews_sign": pieSignUpArr[4],
		"ranger_sign": pieSignUpArr[5],
		"homeView": allViewArr[0],
		"appView": allViewArr[1],
		"businessView": allViewArr[2],
		"contactView": allViewArr[3],
		"fitnessView": allViewArr[4],
		"friendsView": allViewArr[5],
		"gamesView": allViewArr[6],
		"goodnewsView": allViewArr[7],
		"herbsView": allViewArr[8],
		"squiggles": allViewArr[9],
		"aboutView": allViewArr[10],
		"labView": allViewArr[11],
		"rangerView": allViewArr[12]        
	}    
	return render(request, "lab/overview.html", context)
























