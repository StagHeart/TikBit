from django.db import models

# all models go here

#-- general Sign Up
class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self): #Python 3.3 is __str__
		return self.email

# --GAMES--
# Squiggles
class SignUp_Squiggles(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self): #Python 3.3 is __str__
		return self.email

# Ranger
class SignUp_Ranger(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self): #Python 3.3 is __str__
		return self.email

# --APPS--
# Friends
class SignUp_Friends(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self): #Python 3.3 is __str__
		return self.email

# Herbs
class SignUp_Herbs(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self): #Python 3.3 is __str__
		return self.email

# Fitness
class SignUp_Fitness(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self): #Python 3.3 is __str__
		return self.email

# Good News
class SignUp_GoodNews(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120, blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self): #Python 3.3 is __str__
		return self.email
		
# keeps track of the view per page
# --Page Counter--
class Counter_View(models.Model):
	home_page = models.IntegerField(default=0, editable=False)
	games_page = models.IntegerField(default=0, editable=False)
	squiggles_page = models.IntegerField(default=0, editable=False)
	apps_page = models.IntegerField(default=0, editable=False)
	herbs_page = models.IntegerField(default=0, editable=False)
	friends_page = models.IntegerField(default=0, editable=False)
	fitness_page = models.IntegerField(default=0, editable=False)
	goodnews_page = models.IntegerField(default=0, editable=False)
	business_page = models.IntegerField(default=0, editable=False)
	contact_page = models.IntegerField(default=0, editable=False)
	about_page = models.IntegerField(default=0, editable=False)
	lab_page = models.IntegerField(default=0, editable=False)
	ranger_page = models.IntegerField(default=0, editable=False)


	
	




