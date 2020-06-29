from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={"placeholder": "Your Title"}))
    description = forms.CharField(
                                required=False,
                                widget=forms.Textarea(
                                    attrs={
                                        "placeholder": "Your description",
                                        "class": "new-class-name two",
                                        "rows":20,
                                        "cols":100
                                    }
                                )
                            )   
    price = forms.DecimalField()
    
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    def clean_title(self, *args, **kargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("This is not a valid title")
        if not "news" in title:
            raise forms.ValidationError("This is not a valid title")
        return title

class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your Title"}))
    description = forms.CharField(
                                required=False,
                                widget=forms.Textarea(
                                    attrs={
                                        "placeholder": "Your description",
                                        "class": "new-class-name two",
                                        "rows":20,
                                        "cols":100
                                    }
                                )
                            )   
    price = forms.DecimalField()
