from .models import Book
from .serializers import BooksSerializer, BookSerializer
from rest_framework import generics, mixins, viewsets


class BooksAPI(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
               mixins.UpdateModelMixin, mixins.DestroyModelMixin,
               viewsets.GenericViewSet):
    queryset = Book.objects.all()
    default_serializer_class = BookSerializer
    serializer_classes = {
        'list': BooksSerializer,

    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action,
                                           self.default_serializer_class)

    def get(self, request, *args, **kwargs):

        if 'pk' not in self.kwargs:
            return self.list(request, *args, **kwargs)
        else:
            self.retrieve(request, *args, **kwargs)
