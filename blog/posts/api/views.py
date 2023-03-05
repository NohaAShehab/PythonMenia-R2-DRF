import json
from django.http import  HttpResponse, JsonResponse
from posts.models import Post
from posts.api.serializers import  PostSerializer
from django.views.decorators.csrf import  csrf_exempt

# def posts_api(request):
#     if request.method =='GET':
#         posts = Post.get_all_posts()
#         return HttpResponse(posts)

# def posts_api(request):
#     if request.method =='GET':
#         posts = Post.get_all_posts()
#         # myl = []
#         # for p in posts:
#         #     print(p.__dict__)
#         #     myl.append(p.__dict__)
#         # newposts = {"data":myl}
#         return JsonResponse({'data':"post"}, safe=False)
@csrf_exempt
def posts_api(request):
    if request.method =='GET':
        posts = Post.get_all_posts()
        serialized_posts = []
        for post in posts:
            serialized_posts.append(PostSerializer(post).data)
        print(serialized_posts)
        return JsonResponse(serialized_posts, safe=False)
    elif request.method=='POST':
        print(request.body)
        # json.load
        post_data  = json.loads(request.body)
        print(post_data)
        post = Post.objects.create(**post_data)
        # return JsonResponse({"data":"post_added"})
        return JsonResponse(PostSerializer(post).data)

@csrf_exempt
def post_api(request, id):
    ## get object
    post = Post.get_post(id)
    if request.method =='GET':

        return JsonResponse(PostSerializer(post).data)

    elif request.method=='PUT':
        updated_data = json.loads(request.body)
        post.title= updated_data["title"]
        post.description= updated_data["description"]
        post.save()
        return JsonResponse(PostSerializer(post).data)

    elif request.method=='DELETE':
        post.delete()
        return JsonResponse({"delete":1})