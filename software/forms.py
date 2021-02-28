from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from django.utils.translation import gettext_lazy as _
from crispy_forms.bootstrap import StrictButton, InlineField
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Div
from crispy_forms.bootstrap import StrictButton, InlineField, InlineRadios
from .models import PostSoft, PostNS, PostGIS, PostLinux, PostMatlab, Post3dMax, PostAutocadSoft


which = [
    ('کامپیوتر زمینی', 'کامپیوتر زمینی'),
    ('لپ تاپ', 'لپ تاپ'),

]

request = [
    ('درخواست تعمیر در منزل را دارم', 'درخواست تعمیر در منزل را دارم'),
    ('درخواست ارسال دستگاه به شرکت جهت تعمیر را دارم', 'درخواست ارسال دستگاه به شرکت جهت تعمیر را دارم'),

]

class PostSoftForm(forms.ModelForm):
    post = forms.CharField()

    class Meta:
        model = PostSoft
        fields = ('post',)

class PostAutocadSoftForm(forms.ModelForm):
    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))

    kind = forms.ChoiceField(label='سیستم', widget=forms.RadioSelect(attrs={'placeholder': 'نوع دستگاه'}),
                                choices=which)
    req = forms.ChoiceField(label='نوع درخواست', widget=forms.RadioSelect(attrs={'placeholder': 'نوع درخواست'}),
                                 choices=request)
    bio = forms.CharField(label= 'توضیح مختصر درباره ایراد دستگاه'    ,widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostAutocadSoft
        fields = ('kind', 'req', 'phoneNum', 'address',
                  'bio','agree' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('kind'),
            InlineRadios('req'),
            Row(
                Column('phoneNum', css_class='form-group col-md-4 mb-0'),
                Column('address', css_class='form-group col-md-8 mb-0'),

                css_class='form-row'
            ),
            Row(
                Column('bio', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            'agree',

            Submit('submit', 'ثبت'),
        )

class Post3dMaxForm(forms.ModelForm):
    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))

    kind = forms.ChoiceField(label='سیستم', widget=forms.RadioSelect(attrs={'placeholder': 'نوع دستگاه'}),
                                choices=which)
    req = forms.ChoiceField(label='نوع درخواست', widget=forms.RadioSelect(attrs={'placeholder': 'نوع درخواست'}),
                                 choices=request)
    bio = forms.CharField(label= 'توضیح مختصر درباره ایراد دستگاه'    ,widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = Post3dMax
        fields = ('kind', 'req', 'phoneNum', 'address',
                  'bio','agree' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('kind'),
            InlineRadios('req'),
            Row(
                Column('phoneNum', css_class='form-group col-md-4 mb-0'),
                Column('address', css_class='form-group col-md-8 mb-0'),

                css_class='form-row'
            ),
            Row(
                Column('bio', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            'agree',

            Submit('submit', 'ثبت'),
        )

class PostGISForm(forms.ModelForm):
    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))

    kind = forms.ChoiceField(label='سیستم', widget=forms.RadioSelect(attrs={'placeholder': 'نوع دستگاه'}),
                                choices=which)
    req = forms.ChoiceField(label='نوع درخواست', widget=forms.RadioSelect(attrs={'placeholder': 'نوع درخواست'}),
                                 choices=request)
    bio = forms.CharField(label= 'توضیح مختصر درباره ایراد دستگاه'    ,widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostGIS
        fields = ('kind', 'req', 'phoneNum', 'address',
                  'bio','agree' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('kind'),
            InlineRadios('req'),
            Row(
                Column('phoneNum', css_class='form-group col-md-4 mb-0'),
                Column('address', css_class='form-group col-md-8 mb-0'),

                css_class='form-row'
            ),
            Row(
                Column('bio', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            'agree',

            Submit('submit', 'ثبت'),
        )

class PostNSForm(forms.ModelForm):
    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))

    kind = forms.ChoiceField(label='سیستم', widget=forms.RadioSelect(attrs={'placeholder': 'نوع دستگاه'}),
                                choices=which)
    req = forms.ChoiceField(label='نوع درخواست', widget=forms.RadioSelect(attrs={'placeholder': 'نوع درخواست'}),
                                 choices=request)
    bio = forms.CharField(label= 'توضیح مختصر درباره ایراد دستگاه'    ,widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostNS
        fields = ('kind', 'req', 'phoneNum', 'address',
                  'bio','agree' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('kind'),
            InlineRadios('req'),
            Row(
                Column('phoneNum', css_class='form-group col-md-4 mb-0'),
                Column('address', css_class='form-group col-md-8 mb-0'),

                css_class='form-row'
            ),
            Row(
                Column('bio', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            'agree',

            Submit('submit', 'ثبت'),
        )

class PostMatlabForm(forms.ModelForm):
    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))

    kind = forms.ChoiceField(label='سیستم', widget=forms.RadioSelect(attrs={'placeholder': 'نوع دستگاه'}),
                                choices=which)
    req = forms.ChoiceField(label='نوع درخواست', widget=forms.RadioSelect(attrs={'placeholder': 'نوع درخواست'}),
                                 choices=request)
    bio = forms.CharField(label= 'توضیح مختصر درباره ایراد دستگاه'    ,widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostMatlab
        fields = ('kind', 'req', 'phoneNum', 'address',
                  'bio','agree' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('kind'),
            InlineRadios('req'),
            Row(
                Column('phoneNum', css_class='form-group col-md-4 mb-0'),
                Column('address', css_class='form-group col-md-8 mb-0'),

                css_class='form-row'
            ),
            Row(
                Column('bio', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            'agree',

            Submit('submit', 'ثبت'),
        )

class PostLinuxForm(forms.ModelForm):
    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))

    kind = forms.ChoiceField(label='سیستم', widget=forms.RadioSelect(attrs={'placeholder': 'نوع دستگاه'}),
                                choices=which)
    req = forms.ChoiceField(label='نوع درخواست', widget=forms.RadioSelect(attrs={'placeholder': 'نوع درخواست'}),
                                 choices=request)
    bio = forms.CharField(label= 'توضیح مختصر درباره ایراد دستگاه'    ,widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostLinux
        fields = ('kind', 'req', 'phoneNum', 'address',
                  'bio','agree' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('kind'),
            InlineRadios('req'),
            Row(
                Column('phoneNum', css_class='form-group col-md-4 mb-0'),
                Column('address', css_class='form-group col-md-8 mb-0'),

                css_class='form-row'
            ),
            Row(
                Column('bio', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            'agree',

            Submit('submit', 'ثبت'),
        )