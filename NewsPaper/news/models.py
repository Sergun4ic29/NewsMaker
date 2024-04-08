from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



articale = 'AR'
news = 'NW'
POSITIONS = [
    (articale,'статья'),
    (news,'новость')
]

# Create your models here.
class Author(models.Model):
    ratio    = models.IntegerField(default=0)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def update_rating(self):
        posts_ratio = 0
        coments_ratio = 0
        raitios_posts = 0
        posts = Post.objects.filter(auther=self)
        for p in posts:
            posts_ratio += p._postratio
        coments = Coment.objects.filter(user=self.user)
        for c in coments:
            coments_ratio += c._comentratio
        raitios_p = Coment.objects.filter(post__auther=self)
        for r in raitios_p:
            raitios_posts += r._comentratio
        self.ratio = posts_ratio *3 + coments_ratio + raitios_posts
        self.save()
    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=50,unique=True)
    subscribers = models.ManyToManyField(User)
    def __str__(self):
        return self.title

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subscribers'].initial = 'default_user'

class Post (models.Model):
    auther = models.ForeignKey(Author, on_delete=models.CASCADE)
    rulobject = models.CharField(max_length=2,choices=POSITIONS)
    date =models.DateTimeField(auto_now_add=True)
    catygorys = models.ManyToManyField(Category,through='PostCategory')
    header = models.CharField(max_length=30)
    text = models.TextField()
    _postratio = models.IntegerField(default=0)

    @property
    def postratio(self):
        return self._postratio
    @postratio.setter
    def postratio(self,value):
        self._postratio = int(value) if int(value) > 0 else 0
        self.save()

    def likeRatio(self):
        self._postratio = self._postratio + 1
        self.save()

    def dislikeRatio(self):
        self._postratio = self._postratio - 1
        self.save()

    def previw(self):
        return self.text[:50] + '...'
    def __str__(self):
        return f'({self.header.title()} : {self.rulobject})'
    def get_absolute_url(self):
        return reverse('post_detail',args=[str(self.id)])

class Coment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    textcoment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    _comentratio = models.IntegerField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    @property
    def comentratio(self):
        return self._comentratio
    @comentratio.setter
    def comentratio(self,value):
        self._comentratio = int(value) if int(value) > 0 else 0
        self.save()
    def likeRatio(self):
        self._comentratio = self._comentratio + 1
        self.save()
    def dislikeRatio(self):
        self._comentratio = self._comentratio - 1
        self.save()


class PostCategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)





