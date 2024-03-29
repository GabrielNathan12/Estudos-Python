from django.contrib import admin
from .forms import VariationRequired
from . import models


class VariationInline(admin.TabularInline):
    model = models.Variation
    formset = VariationRequired
    min_num = 1
    extra = 0
    can_delete = True


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['name', 'description_long',
                    'get_price_formact', 'get_price_formact_promo']
    inlines = [
        VariationInline
    ]


admin.site.register(models.Product, ProdutoAdmin)
admin.site.register(models.Variation)