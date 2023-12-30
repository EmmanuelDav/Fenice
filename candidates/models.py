from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from autoslug import AutoSlugField
from django_countries.fields import CountryField
from django.utils import timezone


CHOICEs = (
      ('Full Time', 'Full Time'),
      ('Part Time', 'Part Time'),
      ('Remote', 'Remote'),
      ('Intenship', 'Intenship')
)



class Profile(models.Model):
      user = models.OneToOneField( User, on_delete=models.CASCADE, primary_key=True, related_name='profile')
      full_name = models.CharField(null=True,max_length=200,blank=True)
      country = CountryField(null=True,blank=True)
      location = models.CharField(max_length=225, null=True,blank=True)
      resume = models.FileField(upload_to='resume', null=True,blank=True)
      grad_year = models.IntegerField(blank=True)
      lookingfor =models.CharField(max_length=30, choices = CHOICEs,default= 'Full Time',null=True)
      slug = AutoSlugField(populate_from='user', unique=True)


      def save(self, *args, **kwargs):
            super().save(*args, **kwargs)

    
      def get_absolute_url(self):
            return "/profile/{}".format(self.slug)
      
      def __str__(self):
            return self.user.username
      

class Skill(models.Model):
      skill = models.CharField(max_length = 200)
      user = models.ForeignKey(User, related_name='skills', on_delete= models.CASCADE)


class SavedJobs(models.Model):
    job = models.ForeignKey(
        Job, related_name='saved_job', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='saved', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.job.title


class AppliedJobs(models.Model):
    job = models.ForeignKey(
        Job, related_name='applied_job', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='applied_user', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.job.titl      
            

