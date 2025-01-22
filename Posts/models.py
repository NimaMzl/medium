from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from datetime import datetime

class PublishManager(models.Manager):
      def get_queryset(self):
         
         return super(PublishManager,self).get_queryset().filter(status="publish")



class Article(models.Model):
      STATUS=(
            ('checking','Checking'),
            ('rejected','Rejected'),
            ('publish','Publish'),
      )
      
      title=models.CharField(max_length=200)
      content=models.TextField()
      created=models.DateTimeField(auto_now_add=True)
      editted=models.DateTimeField(auto_now=True, auto_now_add=False)
      author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
      status=models.CharField(max_length=12, choices=STATUS,default="checking")
      slug=models.SlugField(unique=True,null=True)
      image=models.ImageField(upload_to="images/%Y/%m/%d",blank=True,null=True)

      def save(self,*args, **kwargs):
            super().save(*args,**kwargs)
            now=datetime.now()
            if not self.slug:
                  self.slug =slugify(self.title)+"-"+str(now.year)+"-"+str(now.month)+"-"+str(now.day)
                  self.save()

      class Meta:
            ordering=("created",)

      def __str__(self):
            return self.title   

      objects=models.Manager()
      publish=PublishManager()   
