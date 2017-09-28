from django.shortcuts import render
# from websh.models import User

# Create your views here.

def login_form(request):
	return render(request, 'login.html', {'user': 'test'})
