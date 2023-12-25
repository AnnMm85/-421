from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import *

app_name = 'main'

urlpatterns = [
                  path('', views.index, name='index'),
                  path('accounts/login/', BBLoginView.as_view(), name='login'),
                  path('accounts/register/', RegisterUserView.as_view(), name='register'),
                  path('accounts/logout/', views.logout_view, name='logout'),
                  path('accounts/profile', ProfileListView.as_view(), name='profile'),
                  path('products/', ProductListView.as_view(), name='products'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# path('products/detail', ProductsView.as_view(), name='products'),
