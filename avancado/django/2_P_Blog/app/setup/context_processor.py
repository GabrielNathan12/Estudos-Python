from django.http import HttpRequest
from setup.models import SiteSetup


def context_processor_example(request:HttpRequest):
    return {
        'example':'Exemplo'
    }

def site_setup(request:HttpRequest):
    data = SiteSetup.objects.order_by('-id').first()
    return {
        'site_setup': data
    }