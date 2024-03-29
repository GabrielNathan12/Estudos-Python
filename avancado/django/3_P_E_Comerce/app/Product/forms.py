from django.forms.models import BaseInlineFormSet

class VariationRequired(BaseInlineFormSet):
    def _construct_form(self, i, **kwargs):
        form = super(VariationRequired, self)._construct_form(i, **kwargs)
        form.empty_permitted = False
        return form