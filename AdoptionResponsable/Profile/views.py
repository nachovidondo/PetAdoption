from django.shortcuts import render
from .forms import ProfileModelForm
from .models import Profile



def my_profile(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileModelForm(request.POST or None, request.FILES or None, instance=profile)
    confirm = False
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True
    
    context =  {
        'profile':profile,
        'form':form,
        'confirm':confirm,
    }
    return render(request,'my_profile.html', context)