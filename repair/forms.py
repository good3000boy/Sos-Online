from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Div
from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from django.utils.translation import gettext_lazy as _
from crispy_forms.bootstrap import StrictButton, InlineField, InlineRadios
from django import forms
from .models import PostRep, PostAlarm, PostTable,PostLed, PostDigital, PostElectric, PostTV, PostPhone, PostRefrigerator, PostIphone, PostMonitor, PostCCTV, PostMobile

which = [
    ('کامپیوتر زمینی', 'کامپیوتر زمینی'),
    ('لپ تاپ', 'لپ تاپ'),

]

request = [
    ('درخواست تعمیر در منزل را دارم', 'درخواست تعمیر در منزل را دارم'),
    ('درخواست ارسال دستگاه به شرکت جهت تعمیر را دارم', 'درخواست ارسال دستگاه به شرکت جهت تعمیر را دارم'),

]



class PostRepForm(forms.ModelForm):
    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))

    kind = forms.ChoiceField(label='سیستم', widget=forms.RadioSelect(attrs={'placeholder': 'نوع دستگاه'}),
                                choices=which)
    req = forms.ChoiceField(label='نوع درخواست', widget=forms.RadioSelect(attrs={'placeholder': 'نوع درخواست'}),
                                 choices=request)
    bio = forms.CharField(label= 'توضیح مختصر درباره ایراد دستگاه'    ,widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostRep
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

class PostAlarmForm(forms.ModelForm):
    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label= 'توضیح مختصر درباره ایراد دستگاه'    ,widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostAlarm
        fields = ('phoneNum', 'address',
                  'bio','agree' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
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

class PostTableForm(forms.ModelForm):
    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label= 'توضیح مختصر درباره ایراد دستگاه'    ,widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostTable
        fields = ('phoneNum', 'address',
                  'bio','agree' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
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

class PostLedForm(forms.ModelForm):
    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label= 'توضیح مختصر درباره ایراد دستگاه'    ,widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostLed
        fields = ('phoneNum', 'address',
                  'bio','agree' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
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

class PostDigitalForm(forms.ModelForm):
    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label= 'توضیح مختصر درباره ایراد دستگاه'    ,widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostDigital
        fields = ('phoneNum', 'address',
                  'bio','agree' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
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

class PostElectricForm(forms.ModelForm):
    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label= 'توضیح مختصر درباره ایراد دستگاه'    ,widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostElectric
        fields = ('phoneNum', 'address',
                  'bio','agree' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
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

class PostTVForm(forms.ModelForm):
    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label= 'توضیح مختصر درباره ایراد دستگاه'    ,widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostTV
        fields = ('phoneNum', 'address',
                  'bio','agree' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
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

class PostPhoneForm(forms.ModelForm):
    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label= 'توضیح مختصر درباره ایراد دستگاه'    ,widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostPhone
        fields = ('phoneNum', 'address',
                  'bio','agree' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
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

class PostRefrigeratorForm(forms.ModelForm):
    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label= 'توضیح مختصر درباره ایراد دستگاه'    ,widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostRefrigerator
        fields = ('phoneNum', 'address',
                  'bio','agree' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
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

class PostIphoneForm(forms.ModelForm):
    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label= 'توضیح مختصر درباره ایراد دستگاه'    ,widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostIphone
        fields = ('phoneNum', 'address',
                  'bio','agree' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
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

class PostMonitorForm(forms.ModelForm):
    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label= 'توضیح مختصر درباره ایراد دستگاه'    ,widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostMonitor
        fields = ('phoneNum', 'address',
                  'bio','agree' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
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

class PostCCTVForm(forms.ModelForm):
    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label= 'توضیح مختصر درباره ایراد دستگاه'    ,widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostCCTV
        fields = ('phoneNum', 'address',
                  'bio','agree' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
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

class PostMobileForm(forms.ModelForm):
    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    kind = forms.CharField(label=' نوع گوشی', widget=forms.TextInput)
    bio = forms.CharField(label= 'توضیح مختصر درباره ایراد دستگاه'    ,widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    agree = forms.BooleanField(initial=True, label='با کلیه شرایط شرکت موافقم')

    class Meta:
        model = PostMobile
        fields = ('kind', 'phoneNum', 'address',
                  'bio','agree' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'kind',
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

