from django.db import models
from app import models as app



class UserProfile(models.Model):
    user = models.ForeignKey(app.User, related_name='userprofile', on_delete=models.CASCADE)
    is_vendor = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email


