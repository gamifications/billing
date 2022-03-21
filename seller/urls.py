from django.urls import include, path

from seller.views import sellers_view, entrylist_view, entry_view, ajax_pdf
app_name='seller'

urlpatterns = [
    path('', entry_view, name='entry'),
    path('entrylist/', entrylist_view, name='entrylist'),
    path('sellers/', sellers_view, name='sellers'),
    
    path('generate_pdf/', ajax_pdf),
]