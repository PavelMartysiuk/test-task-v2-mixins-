from .models import Book
from .serializers import BooksSerializer
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets


class BooksAPI(mixins.ListModelMixin, mixins.CreateModelMixin,
               viewsets.GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    serializer_classes = {
        'list': BooksSerializer,

    }

    def get_serializer_class(self):
        """Func chooses serializer"""
        return self.serializer_classes.get(self.action,
                                           self.serializer_class)

    def get(self, request):
        """"Func retrieves all record from bd"""
        return self.list(request)

    def post(self, request):
        """Func adds new book"""
        return self.create(request)


class BookAPI(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
              mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer

    def get(self, request, pk):
        """Func retrieves one book by pk"""
        return self.retrieve(request, pk)

    def put(self, request, pk):
        """Func edits book info """
        return self.update(request, pk)

    def delete(self, request, pk):
        """Func removes current book """
        return self.destroy(request, pk)
