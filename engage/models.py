from django.db import models
from django.conf import settings

from swampdragon.models import SelfPublishModel
from .serializers import UserMessageSerializer


class UserMessage(SelfPublishModel, models.Model):
    serializer_class = UserMessageSerializer
    text = models.CharField(max_length=250)
    user = models.ForeignKey(
                settings.AUTH_USER_MODEL,
                related_name='messages'
            )
    direction = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text
