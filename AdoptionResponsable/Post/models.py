from django.db import models
from django.core.validators import FileExtensionValidator
from Profile.models import Profile


class Post(models.Model):
    content = models.TextField()
    image = models.ImageField(
        upload_to="post/", validators=[FileExtensionValidator(['png','jpg','jpeg'])],
                                       blank=True)
    liked = models.ManyToManyField(
        Profile,blank=True,related_name='likes')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, 
                               on_delete=models.CASCADE, related_name="posts")
    
    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return str(self.content[:20])
    
    def num_likes(self):
        return self.liked.all().count()
    
    def num_comments(self):
        return self.comment_set.all().count()



class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body =  models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.pk)

LIKE_CHOICES = (
    (
        'Me gusta','Me gusta'
    ),
    (
        'No me gusta','No me gusta'
    ),
)

class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=11)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"
    
    
 
        

    
    