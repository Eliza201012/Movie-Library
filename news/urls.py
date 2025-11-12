from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import create_news, news_list, news_detail, update_news, delete_news

urlpatterns = [
    path("create_news/", create_news, name="create_news"),
    path("news_list/", news_list, name="news_list"),
    path("news_detail/<int:id>/", news_detail, name="news_detail"),
    path("update_news/<int:id>/", update_news, name="update_news"),
    path("delete_news/<int:id>/", delete_news, name="delete_news")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)