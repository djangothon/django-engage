from swampdragon import route_handler
from swampdragon.route_handler import ModelRouter
from swampdragon.permissions import LoginRequired
from swampdragon.pubsub_providers.data_publisher import publish_data
from django.contrib.auth import get_user_model

from .serializers import UserMessageSerializer
from .models import UserMessage


class UserMessageRouter(ModelRouter):
    serializer_class = UserMessageSerializer
    model = UserMessage
    route_name = 'user-message'
    permission_classes = [LoginRequired()]
    valid_verbs = ['subscribe', 'create', 'unsubscribe']

    def get_subscription_channels(self, **kwargs):
        # ret = [('user-message-' + user.pk) for user in get_user_model().objects.all()]
        return ['user-message-1', 'user-message-2']

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['pk'])

    def get_query_set(self, **kwargs):
        return self.model.all()

    def create(self, **kwargs):
        initial = self.get_initial('create', **kwargs)
        self.serializer = self.serializer_class(data=kwargs, initial=initial)
        msg = UserMessage.objects.create(
            text=self.serializer.data['text'],
            user=self.connection.user,
            direction='from'
        )
        publish_data('user-message-%s' % self.connection.user.pk, {
            'text': msg.text,
            'created_at': str(msg.created_at),
            'direction': 'from'
        })
        self.send('done')


class AdminMessageRouter(ModelRouter):
    serializer_class = UserMessageSerializer
    model = UserMessage
    route_name = 'admin-message'
    permission_classes = [LoginRequired()]

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['pk'])

    def get_query_set(self, **kwargs):
        return self.model.all()

    def create(self, **kwargs):
        initial = self.get_initial('create', **kwargs)
        self.serializer = self.serializer_class(data=kwargs, initial=initial)
        pk = self.serializer.data['user']
        user = get_user_model().objects.get(pk=pk)
        msg = UserMessage.objects.create(
            text=self.serializer.data['text'],
            user=user,
            direction='to'
        )
        publish_data('user-message-%s' % user.pk, {
            'text': msg.text,
            'created_at': str(msg.created_at),
            'direction': 'from'
        })

        self.send('done')

route_handler.register(UserMessageRouter)
route_handler.register(AdminMessageRouter)
