from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'books', views.BooksAPI)
urlpatterns = router.urls
