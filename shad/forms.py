from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from django.utils.translation import gettext_lazy as _
from crispy_forms.bootstrap import StrictButton, InlineField
from django import forms
from .models import  PostShad


FAVORITE_CHOICES_LESSON = [
    ('حضوری', 'حضوری'),
    ('آنلاین', 'آنلاین')
]


class PostShadForm(forms.ModelForm):
    way = forms.ChoiceField(label='نوع تدریس',widget=forms.RadioSelect, choices=FAVORITE_CHOICES_LESSON, )

    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label='توضیح درباره ایراد نرم افزار',
                          widget=forms.Textarea(attrs={'rows': 3}))
    agree = forms.BooleanField(initial=True)
    class Meta:
        model = PostShad

        fields = ('way', 'phoneNum', 'address', 'bio', 'agree', )