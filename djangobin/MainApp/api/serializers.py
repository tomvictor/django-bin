from rest_framework.serializers import ModelSerializer,HyperlinkedIdentityField
from MainApp.models import Post

class MsgListSerializer(ModelSerializer):
    # url = HyperlinkedIdentityField(
    #     view_name='api-detail'
    # )
    class Meta:
        model = Post
        fields = [
            # 'url',
            'id',
            'slug',
            'title',
            'content',
            'status',
            'writer',
            'timestamp',
        ]



class MsgCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'status',
            'files',
        ]

class MsgDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'status',
            'writer',
            'timestamp',
        ]






"""
data = {
    "msg" : "Tom testing rest",
    "topic" : "hai",
    "time" : "2016-08-13 12:36:47.711279"
}

new_data = MsgListSerializer(data=data)
if new_data.is_valid():
    new_data.save()
else:
    print(new_data.errors)

"""
