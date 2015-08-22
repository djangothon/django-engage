from django.db import models

from swampdragon.models import SelfPublishModel
from .serializers import UserMessageSerializer


class UserMessage(SelfPublishModel, models.Model):
    serializer_class = UserMessageSerializer
    text = models.CharField(max_length=250)

    def __unicode__(self):
        return self.text
