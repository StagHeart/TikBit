from django.contrib import admin
from .forms import *
from .models import *

# Sign up for admin
class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "updated"]
	form = SignUpForm
	# class Meta:
	# 	model = SignUp


# Register for signup form in admin
admin.site.register(SignUp, SignUpAdmin)
admin.site.register(SignUp_Squiggles, SignUpAdmin)
admin.site.register(SignUp_Friends, SignUpAdmin)
admin.site.register(SignUp_Herbs, SignUpAdmin)
admin.site.register(SignUp_Fitness, SignUpAdmin)
admin.site.register(SignUp_GoodNews, SignUpAdmin)
admin.site.register(SignUp_Ranger, SignUpAdmin)
