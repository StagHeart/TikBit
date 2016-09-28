from .models import *

# everything that has to do with counting goes in this file

# --view Counter--
def viewCounter(page):
    rec = Counter_View.objects.get(pk=1)
    temp  = getattr(rec, page)
    temp += 1
    setattr(rec, page, temp) 
    rec.save()

# --Sign Up Counter--
def signUpCounter(form):
    rec = Counter_SignUp.objects.get(pk=1)
    temp  = getattr(rec, form)
    temp += 1
    setattr(rec, form, temp) 
    rec.save()

# -- SignUp Counter--
def signUpCounterNum():
    num = SignUp.objects.count()    
    return (num)

# -- Squiggles SignUp Counter--
def signUpCounterSquigglesNum():
    num = SignUp_Squiggles.objects.count()  
    return (num)

# -- Ranger SignUp Counter--
def signUpCounterRangerNum():
    num = SignUp_Ranger.objects.count() 
    return (num)

# -- Herbs SignUp Counter--
def signUpCounterHerbsNum():
    num = SignUp_Herbs.objects.count()  
    return (num)

# -- Friends SignUp Counter--
def signUpCounterFriendsNum():
    num = SignUp_Friends.objects.count()    
    return (num)

# -- Fitness SignUp Counter--
def signUpCounterFitnessNum():
    num = SignUp_Fitness.objects.count()    
    return (num)

# -- GoodNews SignUp Counter--
def signUpCounterGoodNewsNum():
    num = SignUp_GoodNews.objects.count()   
    return (num)


#-- Counts Views of one page
def viewCount(page):
    rec = Counter_View.objects.get(pk=1)
    temp  = getattr(rec, page)
    return(temp)

#-- View Counter --
#  gets the number of views for the different pages and returns an arr
def allViewCounter():
    arr = []
    
    arr.append(viewCount('home_page'))
    arr.append(viewCount('apps_page'))
    arr.append(viewCount('business_page'))
    arr.append(viewCount('contact_page'))
    arr.append(viewCount('fitness_page'))
    arr.append(viewCount('friends_page'))
    arr.append(viewCount('games_page'))
    arr.append(viewCount('goodnews_page'))
    arr.append(viewCount('herbs_page'))
    arr.append(viewCount('squiggles_page'))
    arr.append(viewCount('about_page'))
    arr.append(viewCount('lab_page'))
    arr.append(viewCount('ranger_page'))

    return(arr)

# --Sign Up Pie Info--
# returns an arr of all the sign ups
def signUpPie():
    arr = []
    arr.append(signUpCounterSquigglesNum());
    arr.append(signUpCounterHerbsNum());
    arr.append(signUpCounterFriendsNum());
    arr.append(signUpCounterFitnessNum());
    arr.append(signUpCounterGoodNewsNum());
    arr.append(signUpCounterRangerNum());
    return(arr)

# -- sets the view to Zero--
def viewZero(page):
    rec = Counter_View.objects.get(pk=1)
    temp  = getattr(rec, page)
    temp = 0
    setattr(rec, page, temp) 
    rec.save()

# -- Sets ALL the views to Zero--
def allZero():

    viewZero('home_page')
    viewZero('home_page')
    viewZero('apps_page')
    viewZero('business_page')
    viewZero('contact_page')
    viewZero('fitness_page')
    viewZero('friends_page')
    viewZero('games_page')
    viewZero('goodnews_page')
    viewZero('herbs_page')
    viewZero('squiggles_page')
    viewZero('about_page')
    viewZero('lab_page')
    viewZero('ranger_page')
