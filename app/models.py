from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Question(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.CharField(max_length=100)
    def get_absolute_url(self):
        return reverse('QuestionDeatil', kwargs={'pk': self.pk})
    

class Answer(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.ForeignKey(Question,on_delete=models.CASCADE,related_name='questions')
    answere=models.CharField(max_length=100)

