from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['email','address','name']
        widgets = {
            'name' : forms.TextInput(attrs={'type':'text',
                            'class':'form-control',
                            'placeholder':'Enter your name'}),
            'email' : forms.EmailInput(attrs={'type':'email',
                            'class':'form-control',
                            'placeholder':'Enter email'}),
            'address' : forms.TextInput(attrs={'type':'text',
                            'class':'form-control',
                            'placeholder':'Enter shipping address'})
        }
