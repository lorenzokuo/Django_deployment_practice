from __future__ import unicode_literals
from django.db import models
from ..login_app.models import User

class Job(models.Model):
    title = models.CharField(max_length=45)
    desc = models.TextField(max_length=1000)
    location = models.CharField(max_length=45)
    posted_by = models.ForeignKey(User, related_name='user_jobs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Granted(models.Model):
    user = models.ForeignKey(User, related_name="user_granteds")
    job = models.ForeignKey(Job, related_name="job_granteds")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
