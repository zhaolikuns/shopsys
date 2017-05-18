from django import forms

from .models import *

class ProdectAdminForm(forms.ModelForm):

    # 自定义字段
    def clean_price(self):
        if self.cleaned_data['price'] <=0:
            return forms.ValidationError("价格必须大于0")
        else:
            return self.cleaned_data['price']

    class Meta:
        model = Product
        exclude = []