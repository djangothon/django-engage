from swampdragon import route_handler
from swampdragon.route_handler import ModelRouter
from swampdragon.permissions import LoginRequired

from .serializers import UserMessageSerializer
from .models import UserMessage


class UserMessageRouter(ModelRouter):
    serializer_class = UserMessageSerializer
    model = UserMessage
    route_name = 'user-message'
    permission_classes = [LoginRequired()]

    def get_object(self, **kwargs):
        print self.connection.user
        return self.model.objects.get(pk=kwargs['pk'])

    def get_query_set(self, **kwargs):
        return self.model.all()


route_handler.register(UserMessageRouter)
