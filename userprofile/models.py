from django.db import models
from app import models as app

class UserProfile(models.Model):
    user = models.ForeignKey(app.User, related_name='userprofile', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email