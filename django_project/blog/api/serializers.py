from rest_framework.serializers import ModelSerializer

from blog.models import Post


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content',]



class PostDetailSerializer(ModelSerializer):
    class Meta:
        model =Post
        fields = ['id','title', 'content', 'author']