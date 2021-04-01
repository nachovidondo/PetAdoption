from django.shortcuts import render,redirect,reverse
from django.core.mail import send_mail



def contact(request):
    if request.method == "POST":
        name = request.POST['message-name']
        email = request.POST['message-email']
        message = request.POST['message']
        #Send Email
        send_mail(
            name,   
            message, 
            email,     #from email
            ['ignaciovidondo@hotmail.com'], #to email
            )
        return render(request,'Contact/contact.html',{'name': name })
    
    else:
        return render(request, 'Contact/contact.html',{})