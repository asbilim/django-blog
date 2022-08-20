from rest_framework.serializers import ModelSerializer
from listings.models import Post

class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['author','title','description']