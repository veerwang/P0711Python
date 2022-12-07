from django.shortcuts import render
from globals.globalsvar import GlobalVars


# Create your views here.
def index(request):
    context = {"login_account": GlobalVars.getInstance().account}
    return render(request, 'home/home.html', context)
