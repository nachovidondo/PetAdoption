from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import UpdateView, DeleteView
from Profile.models import Profile
from .forms import PostModelForm, CommentModelForm
from .models import Post, Like


def post_comments_create_and_list_view(request):
    qs = Post.objects.all()
    profile = Profile.objects.get(user=request.user)
    #Post form , comment form
    p_form = PostModelForm()
    c_form = CommentModelForm()
    post_added = False
    
    if 'submit_p_form' in request.POST:
        p_form = PostModelForm(request.POST,request.FILES)
        if p_form.is_valid():
            instance = p_form.save(commit=False)
            instance.author = profile
            instance.save()
            p_form = PostModelForm()
            post_added = True
           
            
    if 'submit_c_form' in request.POST:
        c_form = CommentModelForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = profile
            instance.post = Post.objects.get(id=request.POST.get('post_id'))
            instance.save()
            c_form = CommentModelForm()
    
    context = {
        'qs':qs,
        'profile':profile,
        'p_form':p_form,
        'c_form':c_form,
        'post_added':post_added,
        
    }
    return render(request,'Post/main.html', context)

def like_unlike_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        profile = Profile.objects.get(user=user)
        
        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)
        
        like, created = Like.objects.get_or_create(user=profile,post_id=post_id)
        
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        else:
            like.value = 'Like'
            
            post_obj.save()
            like.save()
            
    return redirect('main')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'confirm_del.html'
    success_url = reverse_lazy ('main')
    
    def get_object(self,*args,**kwargs):
        pk = self.kwargs.get('pk')
        obj = Post.objects.get(pk=pk)
        if not obj.author.user == self.request.user:
            messages.warning(self.request,'Debes ser el autor de este Post para poder eliminarlo')
        return obj


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostModelForm
    template_name = 'update.html'
    success_url = reverse_lazy('main')
    
    def form_valid(self):
        profile = Profile.objects.get(user=self.request.user)
        if form.instance.author == profile:
            return super().form_valid(form)
        else:
            form.add_error(None,'Debes ser el autor de este Post para poder editarlo')
            return super().form_invalid(form)
        