from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from library_api import views
from django.views.generic import TemplateView


# Register our API endpoints
router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'stock', views.StockViewSet)

urlpatterns = [
    path('',
        TemplateView.as_view(template_name="application.html"),
        name='app'
    ), # We added our application template view renderer
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls), # std admin
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')) # Auth framework
]
