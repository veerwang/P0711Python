from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hi 这个是智能柜子的第一个view界面.")
