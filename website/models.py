

from django.db import models
# from datetime  import datetime

from django.contrib.auth.models import AbstractBaseUser

# date_string = '2022-01-01T12:00:00'
# datetime.fromisoformat(date_string)
class usermodel(AbstractBaseUser):
    username = models.CharField(max_length=20 ,null=False)

    email = models.CharField(max_length=20 ,null=False)
    password = models.CharField(max_length=12 ,null=False)
    confirmpassword = models.CharField(max_length=12 ,null=False)
    # date = models.DateField(date_string)

    def __str__(self):
        return self.username


    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()