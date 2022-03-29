from django.urls import include, path
from django.views.generic import TemplateView

from buyer.views import (buyers_view, entrylist_view, entry_view, accounting_view,
    ajax_pdf, buyer_update_view)
app_name='buyer'

urlpatterns = [
    path('', entry_view, name='entry'),
    path('entrylist/', entrylist_view, name='entrylist'),
    path('accounting/', accounting_view, name='accounting'),
    path('buyers/', buyers_view, name='buyers'),
    path('edit/<int:pk>/', buyer_update_view, name="buyer-update"), 

    
    path('generate_pdf/', ajax_pdf),
]