from swampdragon.serializers.model_serializer import ModelSerializer


class UserMessageSerializer(ModelSerializer):
    class Meta:
        model = 'engage.UserMessage'
        publish_fields = ('text', 'created_at')
        update_fields = ('text', )
