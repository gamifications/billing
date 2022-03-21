from weasyprint import HTML
from django.template.loader import render_to_string
from django.conf import settings

from django.db.models import Sum, F
class GeneratePDF:
    def __init__(self, url):
        self.pdf_name = 'seller_invoice.pdf'
        self.url =  f"{url}{settings.MEDIA_URL}{self.pdf_name}"

    def generate(self, entry, items):
        context = {
            'address_from':'Sample from Address\nSummaya manzil\n678686 Paruvassery\nKerala',
            'entry':entry,
            'items':items,
            'total':items.aggregate(total=Sum(F('unit_price')+F('labour_commn')))['total'],
        }
        
        html = HTML(string=render_to_string('pdf/seller_invoice.html', context))
        html.write_pdf(f'{settings.MEDIA_ROOT}/{self.pdf_name}')