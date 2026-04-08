from django import forms
from .models import Task

class CreateNewTask(forms.Form):
    Product = forms.CharField(label="Producto",max_length=200,widget=forms.TextInput(attrs={'class':'Product'}))
    descripcion = forms.CharField(label="Drescripcion del pedido",widget = forms.Textarea(attrs={'class':'descripcion'}))
    estado = forms.ChoiceField(label="Estado",choices=Task.ESTADOS,initial='Sin_previo',widget=forms.Select(attrs={'class':'estado'}))
    
    