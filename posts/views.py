from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from . import models, serializers


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PostSerializer
    queryset = models.Post.objects.all()

    @action(methods=["POST"], detail=True)
    def upvote(self, request, pk):
        """ Upvote the post """

        post = self.get_object()
        post.upvotes += 1
        post.save(update_fields=["upvotes"])

        return Response({"detail": "upvoted"})


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer
    queryset = models.Comment.objects.all()
