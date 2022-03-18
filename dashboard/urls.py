from django.urls import include, path

from dashboard.views import products_view
app_name='dashboard'

urlpatterns = [
    path('products/', products_view, name='products'),
]