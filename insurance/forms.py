from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from django.utils.translation import gettext_lazy as _
from crispy_forms.bootstrap import StrictButton, InlineField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django import forms
from .models import PostIns, PostThird, PostDoctor, PostBody, PostFire, PostOmar, PostBarbarry, PostAccident, PostResponsibility



class PostInsForm(forms.ModelForm):
    post = forms.CharField()

    class Meta:
        model = PostIns
        fields = ('post',)


class PostThirdForm(forms.ModelForm):
    address = forms.CharField(label='آدرس', widget=forms.TextInput)
    city = forms.CharField(label='شهر', widget=forms.TextInput)
    age = forms.IntegerField(label='سن', widget=forms.TextInput(attrs={'placeholder': '--/--/----'}))
    mobile = forms.IntegerField(label='موبایل', widget=forms.NumberInput)
    kind = forms.CharField(label='نوع خودرو', widget=forms.TextInput)
    model = forms.CharField(label='مدل خودرو', widget=forms.TextInput)
    system = forms.CharField(label='سیستم خودرو',widget=forms.TextInput)
    birth_of_insurance = forms.IntegerField(label='تاریخ بیمه', widget=forms.TextInput(attrs={'placeholder': '--/--/----'}))
    years_of_sale = forms.IntegerField(label=' تخفیف (سال)', widget=forms.NumberInput)
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')
    class Meta:
        model = PostThird
        fields = ('address', 'age', 'mobile', 'city', 'birth_of_insurance', 'years_of_sale','agree',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('kind', css_class='form-group col-md-4 mb-0'),
                Column('model', css_class='form-group col-md-4 mb-0'),
                Column('system', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('birth_of_insurance', css_class='form-group col-md-4 mb-0'),
                Column('years_of_sale', css_class='form-group col-md-4 mb-0'),
                Column('age', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('mobile', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(

                Column('address', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            'agree',

            Submit('submit', 'ثبت درخواست'),
        )

class PostBodyForm(forms.ModelForm):
    address = forms.CharField(label='آدرس', widget=forms.TextInput)
    city = forms.CharField(label='شهر', widget=forms.TextInput)
    age = forms.IntegerField(label='سن', widget=forms.TextInput(attrs={'placeholder': '--/--/----'}))
    mobile = forms.IntegerField(label='موبایل', widget=forms.NumberInput)
    kind = forms.CharField(label='نوع خودرو', widget=forms.TextInput)
    model = forms.CharField(label='مدل خودرو', widget=forms.TextInput)
    system = forms.CharField(label='سیستم خودرو',widget=forms.TextInput)
    birth_of_insurance = forms.IntegerField(label='تاریخ بیمه', widget=forms.TextInput(attrs={'placeholder': '--/--/----'}))
    years_of_sale = forms.IntegerField(label=' تخفیف (سال)', widget=forms.NumberInput)
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostBody
        fields = ('address', 'age', 'mobile', 'city', 'birth_of_insurance', 'years_of_sale','agree',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('kind', css_class='form-group col-md-4 mb-0'),
                Column('model', css_class='form-group col-md-4 mb-0'),
                Column('system', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('birth_of_insurance', css_class='form-group col-md-4 mb-0'),
                Column('years_of_sale', css_class='form-group col-md-4 mb-0'),
                Column('age', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('mobile', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(

                Column('address', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            'agree',

            Submit('submit', 'ثبت درخواست'),
        )

class PostResponsibilityForm(forms.ModelForm):
    address = forms.CharField(label='آدرس', widget=forms.TextInput)
    city = forms.CharField(label='شهر', widget=forms.TextInput)
    age = forms.IntegerField(label='سن', widget=forms.TextInput(attrs={'placeholder': '--/--/----'}))
    mobile = forms.IntegerField(label='موبایل', widget=forms.NumberInput)
    kind = forms.CharField(label='نوع خودرو', widget=forms.TextInput)
    model = forms.CharField(label='مدل خودرو', widget=forms.TextInput)
    system = forms.CharField(label='سیستم خودرو',widget=forms.TextInput)
    birth_of_insurance = forms.IntegerField(label='تاریخ بیمه', widget=forms.TextInput(attrs={'placeholder': '--/--/----'}))
    years_of_sale = forms.IntegerField(label='تخفیف (سال)', widget=forms.NumberInput)
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostResponsibility
        fields = ('address', 'age', 'mobile', 'city', 'birth_of_insurance', 'years_of_sale','agree',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('kind', css_class='form-group col-md-4 mb-0'),
                Column('model', css_class='form-group col-md-4 mb-0'),
                Column('system', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('birth_of_insurance', css_class='form-group col-md-4 mb-0'),
                Column('years_of_sale', css_class='form-group col-md-4 mb-0'),
                Column('age', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('mobile', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(

                Column('address', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            'agree',

            Submit('submit', 'ثبت درخواست'),
        )

class PostOmarForm(forms.ModelForm):
    address = forms.CharField(label='آدرس', widget=forms.TextInput)
    city = forms.CharField(label='شهر', widget=forms.TextInput)
    age = forms.IntegerField(label='سن', widget=forms.TextInput(attrs={'placeholder': '--/--/----'}))
    mobile = forms.IntegerField(label='موبایل', widget=forms.NumberInput)
    kind = forms.CharField(label='نوع خودرو', widget=forms.TextInput)
    model = forms.CharField(label='مدل خودرو', widget=forms.TextInput)
    system = forms.CharField(label='سیستم خودرو',widget=forms.TextInput)
    birth_of_insurance = forms.IntegerField(label='تاریخ بیمه', widget=forms.TextInput(attrs={'placeholder': '--/--/----'}))
    years_of_sale = forms.IntegerField(label='تخفیف (سال)', widget=forms.NumberInput)
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostOmar
        fields = ('address', 'age', 'mobile', 'city', 'birth_of_insurance', 'years_of_sale','agree',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('kind', css_class='form-group col-md-4 mb-0'),
                Column('model', css_class='form-group col-md-4 mb-0'),
                Column('system', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('birth_of_insurance', css_class='form-group col-md-4 mb-0'),
                Column('years_of_sale', css_class='form-group col-md-4 mb-0'),
                Column('age', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('mobile', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(

                Column('address', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            'agree',

            Submit('submit', 'ثبت درخواست'),
        )

class PostAccidentForm(forms.ModelForm):
    address = forms.CharField(label='آدرس', widget=forms.TextInput)
    city = forms.CharField(label='شهر', widget=forms.TextInput)
    age = forms.IntegerField(label='سن', widget=forms.TextInput(attrs={'placeholder': '--/--/----'}))
    mobile = forms.IntegerField(label='موبایل', widget=forms.NumberInput)
    kind = forms.CharField(label='نوع خودرو', widget=forms.TextInput)
    model = forms.CharField(label='مدل خودرو', widget=forms.TextInput)
    system = forms.CharField(label='سیستم خودرو',widget=forms.TextInput)
    birth_of_insurance = forms.IntegerField(label='تاریخ بیمه', widget=forms.TextInput(attrs={'placeholder': '--/--/----'}))
    years_of_sale = forms.IntegerField(label='تخفیف (سال)', widget=forms.NumberInput)
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostAccident
        fields = ('address', 'age', 'mobile', 'city', 'birth_of_insurance', 'years_of_sale','agree',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('kind', css_class='form-group col-md-4 mb-0'),
                Column('model', css_class='form-group col-md-4 mb-0'),
                Column('system', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('birth_of_insurance', css_class='form-group col-md-4 mb-0'),
                Column('years_of_sale', css_class='form-group col-md-4 mb-0'),
                Column('age', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('mobile', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(

                Column('address', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            'agree',

            Submit('submit', 'ثبت درخواست'),
        )

class PostFireForm(forms.ModelForm):
    address = forms.CharField(label='آدرس', widget=forms.TextInput)
    city = forms.CharField(label='شهر', widget=forms.TextInput)
    age = forms.IntegerField(label='سن', widget=forms.TextInput(attrs={'placeholder': '--/--/----'}))
    mobile = forms.IntegerField(label='موبایل', widget=forms.NumberInput)
    kind = forms.CharField(label='نوع خودرو', widget=forms.TextInput)
    model = forms.CharField(label='مدل خودرو', widget=forms.TextInput)
    system = forms.CharField(label='سیستم خودرو',widget=forms.TextInput)
    birth_of_insurance = forms.IntegerField(label='تاریخ بیمه', widget=forms.TextInput(attrs={'placeholder': '--/--/----'}))
    years_of_sale = forms.IntegerField(label='تخفیف (سال)', widget=forms.NumberInput)
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostFire
        fields = ('address', 'age', 'mobile', 'city', 'birth_of_insurance', 'years_of_sale','agree',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('kind', css_class='form-group col-md-4 mb-0'),
                Column('model', css_class='form-group col-md-4 mb-0'),
                Column('system', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('birth_of_insurance', css_class='form-group col-md-4 mb-0'),
                Column('years_of_sale', css_class='form-group col-md-4 mb-0'),
                Column('age', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('mobile', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(

                Column('address', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            'agree',

            Submit('submit', 'ثبت درخواست'),
        )

class PostBarbarryForm(forms.ModelForm):
    address = forms.CharField(label='آدرس', widget=forms.TextInput)
    city = forms.CharField(label='شهر', widget=forms.TextInput)
    age = forms.IntegerField(label='سن', widget=forms.TextInput(attrs={'placeholder': '--/--/----'}))
    mobile = forms.IntegerField(label='موبایل', widget=forms.NumberInput)
    kind = forms.CharField(label='نوع خودرو', widget=forms.TextInput)
    model = forms.CharField(label='مدل خودرو', widget=forms.TextInput)
    system = forms.CharField(label='سیستم خودرو',widget=forms.TextInput)
    birth_of_insurance = forms.IntegerField(label='تاریخ بیمه', widget=forms.TextInput(attrs={'placeholder': '--/--/----'}))
    years_of_sale = forms.IntegerField(label='تخفیف (سال)', widget=forms.NumberInput)
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostBarbarry
        fields = ('address', 'age', 'mobile', 'city', 'birth_of_insurance', 'years_of_sale','agree',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('kind', css_class='form-group col-md-4 mb-0'),
                Column('model', css_class='form-group col-md-4 mb-0'),
                Column('system', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('birth_of_insurance', css_class='form-group col-md-4 mb-0'),
                Column('years_of_sale', css_class='form-group col-md-4 mb-0'),
                Column('age', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('mobile', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(

                Column('address', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            'agree',

            Submit('submit', 'ثبت درخواست'),
        )

class PostDoctorForm(forms.ModelForm):
    address = forms.CharField(label='آدرس', widget=forms.TextInput)
    city = forms.CharField(label='شهر', widget=forms.TextInput)
    age = forms.IntegerField(label='سن', widget=forms.TextInput(attrs={'placeholder': '--/--/----'}))
    mobile = forms.IntegerField(label='موبایل', widget=forms.NumberInput)
    kind = forms.CharField(label='نوع خودرو', widget=forms.TextInput)
    model = forms.CharField(label='مدل خودرو', widget=forms.TextInput)
    system = forms.CharField(label='سیستم خودرو',widget=forms.TextInput)
    birth_of_insurance = forms.IntegerField(label='تاریخ بیمه', widget=forms.TextInput(attrs={'placeholder': '--/--/----'}))
    years_of_sale = forms.IntegerField(label='تخفیف (سال)', widget=forms.NumberInput)
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostDoctor
        fields = ('address', 'age', 'mobile', 'city', 'birth_of_insurance', 'years_of_sale','agree',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('kind', css_class='form-group col-md-4 mb-0'),
                Column('model', css_class='form-group col-md-4 mb-0'),
                Column('system', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('birth_of_insurance', css_class='form-group col-md-4 mb-0'),
                Column('years_of_sale', css_class='form-group col-md-4 mb-0'),
                Column('age', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('mobile', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(

                Column('address', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            'agree',

            Submit('submit', 'ثبت درخواست'),
        )