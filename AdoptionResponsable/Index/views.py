from django.shortcuts import render



def home_view(request):
    user = request.user
    hello = 'Hello World'
    context ={
        'user' : user, 
        'hello' : hello,
    }
    return render(request,'home.html',{'user':user,'hello':hello})