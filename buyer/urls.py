from django.urls import include, path
from django.views.generic import TemplateView

from buyer.views import buyers_view, entrylist_view, entry_view
app_name='buyer'

urlpatterns = [
    path('', entry_view, name='entry'),
    path('entrylist/', entrylist_view, name='entrylist'),
    path('buyers/', buyers_view, name='buyers'),
    
    
]