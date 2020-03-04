from django.db import models
from django.contrib.auth.models import User
class Project(models.Model):
    """this is our project"""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    client = models.CharField(max_length=200)
    client_human = models.CharField(max_length=200)
    client_pn = models.IntegerField()
    project_inf = models.TextField()
    def __str__(self):
        return self.project_inf[:10]+"..."