from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apalabrados import views as local_views
from games import views as games_views

urlpatterns = [
    path('', games_views.start_game, name='start_game'),
    path('list_alphanumeric/', games_views.list_alphanumeric, name='list_alphanumeric'),
    path('list_number/', games_views.list_number, name='list_number'),
    path('list_special_char/', games_views.list_special_char, name='list_special_char')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
