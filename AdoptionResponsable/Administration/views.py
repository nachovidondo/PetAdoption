from django.shortcuts import render


def administration(request):
    return render(request,'Administration/admins.html')