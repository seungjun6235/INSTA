from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField

# Create your models here.

class User(AbstractUser):
    profile_image = ResizedImageField(
        size=[500,500],
        crop=['middle','center'],
        upload_to='profile'
    )

    #user의 post_set 
    #like_user의 post_set = reverse accessor 이름 중복 
    #            => like_posts로 바꿈

    followings = models.ManyToManyField('self',related_name='followers', symmetrical=False)
    # user_set 자동생성