from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import PostInt, PostAdsl
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Div
from crispy_forms.bootstrap import StrictButton, InlineField, InlineRadios

service = [
    ('ADSL', 'ADSL'),
    ('VDSL', 'Vdsl'),
    ('فیبرنوری', 'فیبرنوری'),
    ('بی سیم', 'بی سیم'),
    ('مارشال', 'مارشال'),
]

industry = [
    ('مخابرات', 'مخابرات'),
    ('ماکس نت', 'ماکس نت'),
    ('شاتل', 'شاتل'),
    ('آسیا تک', 'آسیا تک'),
    ('های وب', 'های وب'),
]

band = [
    ('1 M', ' M 1'),
    ('2 M', ' M 2'),
    ('4 M', ' M 4'),
    ('8 M', ' M 8'),
    ('16 M', ' M 16'),
    ('100 M', ' M 100'),
]

time = [
    ('ماهانه', 'ماهانه'),
    ('3 ماهه', '3 ماهه'),
    ('6 ماهه', '6 ماهه'),
    ('سالانه', 'سالانه'),
]

capacity = [
    ('10 G', '10 G'),
    ('20 G', '20 G'),
    ('30 G', '30 G'),
    ('100 G', '100 G'),
]

modem = [
    ('بی سیم تک آنتنه', 'بی سیم تک آنتنه'),
    ('بی سیم دو آنتنه', 'بی سیم دو آنتنه'),
    ('فیبرنوری', 'فیبرنوری'),
    ('سیم کارت خور', 'سیم کارت خور'),
]

class PostIntForm(forms.ModelForm):

    first_name = forms.CharField(label= 'نام' ,widget=forms.TextInput(attrs={'placeholder': 'نام'}))
    last_name = forms.CharField(label= 'نام خانوادگی' ,widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی'}))
    phoneNum = forms.IntegerField(label= 'تلفن ثابت' ,widget=forms.NumberInput( attrs = {'placeholder': 'تلفن ثابت'}))
    address = forms.CharField(label= 'آدرس دقیق' ,widget=forms.Textarea(attrs={'rows': 3, 'placeholder' : 'آدرس دقیق'}))
    service = forms.ChoiceField(label= 'سرویس' ,widget=forms.RadioSelect(attrs={'placeholder': 'سرویس'}), choices=service)
    industry = forms.ChoiceField(label= 'شرکت' ,widget=forms.RadioSelect(attrs={'placeholder': 'شرکت'}), choices=industry)
    band = forms.ChoiceField(label= 'پهنای باند' ,widget=forms.RadioSelect(attrs={'placeholder': 'پهنای باند'}), choices=band)
    time = forms.ChoiceField(label= 'مدت زمان' ,widget=forms.RadioSelect(attrs={'placeholder': 'مدت زمان'}), choices=time)
    capacity = forms.ChoiceField(label= 'حجم سرویس' ,widget=forms.RadioSelect(attrs={'placeholder': 'حجم سرویس'}), choices=capacity)
    modem = forms.ChoiceField(label= 'مودم' ,widget=forms.RadioSelect(attrs={'placeholder': 'مودم'}), choices=modem)

    class Meta:
        model = PostInt
        fields = ('first_name', 'last_name', 'phoneNum', 'address',
                  'service', 'industry', 'band', 'time', 'capacity', 'modem', )

class PostAdslForm(forms.ModelForm):

    first_name = forms.CharField(label= 'نام' ,widget=forms.TextInput(attrs={'placeholder': 'نام'}))
    last_name = forms.CharField(label= 'نام خانوادگی' ,widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی'}))
    phoneNum = forms.IntegerField(label= 'تلفن ثابت' ,widget=forms.NumberInput( attrs = {'placeholder': 'تلفن ثابت'}))
    address = forms.CharField(label= 'آدرس دقیق' ,widget=forms.Textarea(attrs={'rows': 3, 'placeholder' : 'آدرس دقیق'}))
    service = forms.ChoiceField(label= 'سرویس' ,widget=forms.RadioSelect(attrs={'placeholder': 'سرویس'}), choices=service)
    industry = forms.ChoiceField(label= 'شرکت' ,widget=forms.RadioSelect(attrs={'placeholder': 'شرکت'}), choices=industry)
    band = forms.ChoiceField(label= 'پهنای باند' ,widget=forms.RadioSelect(attrs={'placeholder': 'پهنای باند'}), choices=band)
    time = forms.ChoiceField(label= 'مدت زمان' ,widget=forms.RadioSelect(attrs={'placeholder': 'مدت زمان'}), choices=time)
    capacity = forms.ChoiceField(label= 'حجم سرویس' ,widget=forms.RadioSelect(attrs={'placeholder': 'حجم سرویس'}), choices=capacity)
    modem = forms.ChoiceField(label= 'مودم' ,widget=forms.RadioSelect(attrs={'placeholder': 'مودم'}), choices=modem)
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')
    class Meta:
        model = PostAdsl
        fields = ('first_name', 'last_name', 'phoneNum', 'address',
                  'service', 'industry', 'band', 'time', 'capacity', 'modem','agree', )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-4 mb-0'),
                Column('last_name', css_class='form-group col-md-8 mb-0'),

                css_class='form-row'
            ),
            Row(
                Column('phoneNum', css_class='form-group col-md-4 mb-0'),
                Column('address', css_class='form-group col-md-8 mb-0'),

                css_class='form-row'
            ),
            InlineRadios('service'),
            InlineRadios('industry'),
            InlineRadios('band'),
            InlineRadios('time'),
            InlineRadios('capacity'),
            InlineRadios('modem'),
            'agree',

            Submit('submit', 'ثبت درخواست'),
        )