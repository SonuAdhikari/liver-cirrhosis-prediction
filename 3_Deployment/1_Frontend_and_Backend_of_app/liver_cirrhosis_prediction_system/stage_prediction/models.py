from django.db import models
from django import forms

# Create your models here.
class Input(models.Model):
    input1 = models.IntegerField(
        null=True,
        default=None
    )
    input2 = models.IntegerField(
        null=True,
        default=None
    )

class InputForm(forms.ModelForm):
    class Meta:
        # models = Input # Typing wrong, model with s!
        model = Input    # Typing correct, model without s
        fields = '__all__'
        labels = {
            'input1': 'INPUT 1',
            'input2': 'INPUT 2'
        }

class Output(models.Model):
    output1 = models.IntegerField(
        null=True,
        default=None
    )