from rest_framework import serializers


class BlogArticleSerializer(serializers.Serializer):
    title = serializers.CharField()
    slug = serializers.SlugField()
    content = serializers.CharField()
    publication_datetime = serializers.DateTimeField()
    status = serializers.BooleanField()
    full_name = serializers.CharField()
