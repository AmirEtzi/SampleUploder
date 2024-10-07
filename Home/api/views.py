from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Home.models import Post, PostImage
from Home.api.serializers import PostSerializer, PostImageSerializer


@api_view(["GET"])
def sample_list(request):
    if request.method == "GET":
        context = Post.objects.all()
        post_serializer = PostSerializer(context, many=True)
        return Response(post_serializer.data)
