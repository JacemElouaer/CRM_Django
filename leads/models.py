from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    pass
#   after creating User with that method we should add AUTH_USER_MODEL = 'leads.User'

# we need to heritage from  AbstractUser to create our own users
# add the user to the settings

class Lead(models.Model):
    # SOURCE_CHOICES = (
    #     ('Youtube', 'Youtube'),
    #     ('Google', 'Google'),
    #     ('Newsletter', 'Newsletter')
    # )
    first_name = models.CharField(max_length=25,null=False )
    last_name = models.CharField(max_length=25, null=False)
    age = models.IntegerField(default=0)
    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES , max_length=220)
    # profile_picture = models.ImageField(blank=True ,  null=True)
    # special_file = models.FileField(blank=True ,  null=True)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " " + self.first_name



# in the foreign key we put agent enter "" to say that Agent is in that file model

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
