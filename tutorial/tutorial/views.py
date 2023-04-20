from django.http import  HttpResponse
def home(request):
    print("hello")
    return HttpResponse("this is home page")