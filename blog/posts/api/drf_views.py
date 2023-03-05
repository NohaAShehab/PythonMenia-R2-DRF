from  rest_framework.response import  Response
from rest_framework.decorators import  api_view
from posts.api.serializers import PostSerializer
from rest_framework import status
from posts.models import  Post

@api_view(['GET','POST'])
def posts_resource(request):
    if request.method =='GET':
        posts = Post.get_all_posts()
        serialized_posts= PostSerializer(posts, many=True)
        return Response(serialized_posts.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        print(request.data)
        post = PostSerializer(data=request.data)
        print(post)
        if post.is_valid():
            print("valid")
            post.save()
            print(post.data)
        else:
            return Response(post.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response("test", status=status.HTTP_200_OK)

@api_view(['GET', 'PUT', 'DELETE'])
def post_resource(request, id):  # rest request ---> request.data
    post = Post.get_post(id)
    if request.method=='GET':
        serialized_post =PostSerializer(post)
        return Response(serialized_post.data, status=status.HTTP_200_OK)

    elif request.method=='DELETE':
        post.delete()
        return Response({'deleted':1}, status=status.HTTP_204_NO_CONTENT)

    elif request.method=='PUT':
        serilized_post= PostSerializer(instance=post, data=request.data)
        if serilized_post.is_valid():
            serilized_post.save()
            return Response(serilized_post.data, status=status.HTTP_200_OK)
        else:
            return Response(serilized_post.errors,status=status.HTTP_400_BAD_REQUEST)

