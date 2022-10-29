from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Product, Review


def length_grade_validator(string):
    if 0 > int(string) > 6:
        raise ValidationError("Score should be no more than 5")
    return string


def max_length_validator(string):
    if len(string) < 3:
        raise ValidationError("The number of characters must be more than 2!")
    return string


class ProductForm(forms.ModelForm):
    title = forms.CharField(max_length=100, required=True, label="Title", validators=(max_length_validator, ))
    description = forms.CharField(max_length=2000, required=False, label="Description",  widget=widgets.Textarea)

    class Meta:
        model = Product
        fields = ('title', 'category', 'description', 'image')


class ReviewForm(forms.ModelForm):
    grade = forms.CharField(max_length=1, required=True, label='Grade', validators=(length_grade_validator, ))

    class Meta:
        model = Review
        fields = ('text', 'grade')
