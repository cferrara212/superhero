from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'superheroes'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:hero_id>/',views.detail, name='detail'),
    path('new/', views.create, name='create'),
    path('delete/<int:hero_id>/', views.delete, name="delete" ),
    path('edit/<int:hero_id>/', views.edit, name="edit")
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    