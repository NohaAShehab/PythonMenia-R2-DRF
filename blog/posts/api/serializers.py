
from rest_framework import serializers

from posts.models import  Post

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title =serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200)
    no_of_likes = serializers.IntegerField(default=10)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Post.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance




