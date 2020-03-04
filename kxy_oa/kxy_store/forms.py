from django import forms
from .models import Product
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['text','quantity','unit','price','store']
        labels = {'text':'产品名称','quantity':'产品数量','unit':'产品单位','price':'产品单价','store':'所属仓库'}