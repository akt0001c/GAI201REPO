from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse("Hello index.")

def greet_user(request,username):
    return HttpResponse(f"Hello, {username}")

def farewell_user(request,username):
    return HttpResponse(f"Goodbye, {username}")