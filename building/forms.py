from crispy_forms.helper import FormHelper
from crispy_forms.layout import Row, Column, Layout, Submit
from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from django.utils.translation import gettext_lazy as _
from crispy_forms.bootstrap import StrictButton, InlineField, InlineRadios
from django import forms
from .models import PostBuild, PostKanaf, PostCabinet, PostJosh, PostMap, PostPipe, PostWire


which = [
    ('نوسازی', 'نوسازی'),
    ('ساخت', 'ساخت'),

]
kanaf = [
    ('آپارتمان', 'آپارتمان'),
    ('ویلا', 'ویلا'),

]

class PostBuildForm(forms.ModelForm):
    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق محل'}))

    kind = forms.ChoiceField(label='نوع سازه', widget=forms.RadioSelect(attrs={'placeholder': 'نوع سازه'}),
                                choices=which)
    area = forms.IntegerField(label='متراژ', widget=forms.NumberInput)
    bio = forms.CharField(label= 'شرح درخواست'    ,widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostBuild
        fields = ('kind', 'area', 'phoneNum', 'address',
                  'bio','agree' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('kind', style='padding-left: 200ps;'),
            Row(
                Column('phoneNum', css_class='form-group col-md-4 mb-0'),
                Column('address', css_class='form-group col-md-8 mb-0'),

                css_class='form-row'
            ),
            Row(
                Column('area', css_class='form-group col-md-2 mb-0'),
                Column('bio', css_class='form-group col-md-10 mb-0'),
                css_class='form-row'
            ),
            'agree',


            Submit('submit', 'ثبت درخواست',css_class='form-group col-md-4 mb-0'),
        )


class PostKanafForm(forms.ModelForm):
    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق محل'}))

    kind = forms.ChoiceField(label='نوع سازه', widget=forms.RadioSelect(attrs={'placeholder': 'نوع سازه'}),
                                choices=kanaf)
    area = forms.IntegerField(label='متراژ', widget=forms.NumberInput)
    bio = forms.CharField(label= 'شرح درخواست' ,widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostKanaf
        fields = ('kind', 'area', 'phoneNum', 'address',
                  'bio','agree' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('kind'),
            Row(
                Column('phoneNum', css_class='form-group col-md-4 mb-0'),
                Column('address', css_class='form-group col-md-8 mb-0'),

                css_class='form-row'
            ),
            Row(
                Column('area', css_class='form-group col-md-2 mb-0'),
                Column('bio', css_class='form-group col-md-10 mb-0'),
                css_class='form-row'
            ),
            'agree',

            Submit('submit', 'ثبت'),
        )

class PostCabinetForm(forms.ModelForm):
    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق محل'}))

    kind = forms.ChoiceField(label='نوع سازه', widget=forms.RadioSelect(attrs={'placeholder': 'نوع سازه'}),
                                choices=kanaf)
    area = forms.IntegerField(label='متراژ', widget=forms.NumberInput)
    bio = forms.CharField(label='شرح درخواست' ,widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostCabinet
        fields = ('kind', 'area', 'phoneNum', 'address',
                  'bio','agree' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('kind'),
            Row(
                Column('phoneNum', css_class='form-group col-md-4 mb-0'),
                Column('address', css_class='form-group col-md-8 mb-0'),

                css_class='form-row'
            ),
            Row(
                Column('area', css_class='form-group col-md-2 mb-0'),
                Column('bio', css_class='form-group col-md-10 mb-0'),
                css_class='form-row'
            ),
            'agree',

            Submit('submit', 'ثبت'),
        )

class PostJoshForm(forms.ModelForm):
    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق محل'}))

    kind = forms.ChoiceField(label='نوع سازه', widget=forms.RadioSelect(attrs={'placeholder': 'نوع سازه'}),
                                choices=kanaf)
    area = forms.IntegerField(label='متراژ', widget=forms.NumberInput)
    bio = forms.CharField(label='شرح درخواست' ,widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostJosh
        fields = ('kind', 'area', 'phoneNum', 'address',
                  'bio','agree' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('kind'),
            Row(
                Column('phoneNum', css_class='form-group col-md-4 mb-0'),
                Column('address', css_class='form-group col-md-8 mb-0'),

                css_class='form-row'
            ),
            Row(
                Column('area', css_class='form-group col-md-2 mb-0'),
                Column('bio', css_class='form-group col-md-10 mb-0'),
                css_class='form-row'
            ),
            'agree',

            Submit('submit', 'ثبت'),
        )

class PostMapForm(forms.ModelForm):
    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق محل'}))

    kind = forms.ChoiceField(label='نوع سازه', widget=forms.RadioSelect(attrs={'placeholder': 'نوع سازه'}),
                                choices=kanaf)
    area = forms.IntegerField(label='متراژ', widget=forms.NumberInput)
    bio = forms.CharField(label='شرح درخواست' ,widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostMap
        fields = ('kind', 'area', 'phoneNum', 'address',
                  'bio','agree' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('kind'),
            Row(
                Column('phoneNum', css_class='form-group col-md-4 mb-0'),
                Column('address', css_class='form-group col-md-8 mb-0'),

                css_class='form-row'
            ),
            Row(
                Column('area', css_class='form-group col-md-2 mb-0'),
                Column('bio', css_class='form-group col-md-10 mb-0'),
                css_class='form-row'
            ),
            'agree',

            Submit('submit', 'ثبت'),
        )

class PostPipeForm(forms.ModelForm):
    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق محل'}))

    kind = forms.ChoiceField(label='نوع سازه', widget=forms.RadioSelect(attrs={'placeholder': 'نوع سازه'}),
                                choices=kanaf)
    area = forms.IntegerField(label='متراژ', widget=forms.NumberInput)
    bio = forms.CharField(label='شرح درخواست' ,widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostPipe
        fields = ('kind', 'area', 'phoneNum', 'address',
                  'bio','agree' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('kind'),
            Row(
                Column('phoneNum', css_class='form-group col-md-4 mb-0'),
                Column('address', css_class='form-group col-md-8 mb-0'),

                css_class='form-row'
            ),
            Row(
                Column('area', css_class='form-group col-md-2 mb-0'),
                Column('bio', css_class='form-group col-md-10 mb-0'),
                css_class='form-row'
            ),
            'agree',

            Submit('submit', 'ثبت'),
        )

class PostWireForm(forms.ModelForm):
    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق محل'}))

    kind = forms.ChoiceField(label='نوع سازه', widget=forms.RadioSelect(attrs={'placeholder': 'نوع سازه'}),
                                choices=kanaf)
    area = forms.IntegerField(label='متراژ', widget=forms.NumberInput)
    bio = forms.CharField(label='شرح درخواست' ,widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostWire
        fields = ('kind', 'area', 'phoneNum', 'address',
                  'bio','agree' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('kind'),
            Row(
                Column('phoneNum', css_class='form-group col-md-4 mb-0'),
                Column('address', css_class='form-group col-md-8 mb-0'),

                css_class='form-row'
            ),
            Row(
                Column('area', css_class='form-group col-md-2 mb-0'),
                Column('bio', css_class='form-group col-md-10 mb-0'),
                css_class='form-row'
            ),
            'agree',

            Submit('submit', 'ثبت'),
        )