from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from django.utils.translation import gettext_lazy as _
from crispy_forms.bootstrap import StrictButton, InlineField, InlineRadios
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Div
from .models import PostEdu, PostEnglish, PostNet, PostIcdl, PostPhoto, PostPython, PostVideo, PostBasicComputer,\
    PostAdvancedComputer, PostSecondaryComputer, PostBourse, PostDesign, PostOffice, PostPhotoShop, PostAccounting, PostAutoCad


FAVORITE_CHOICES = [
    ('computer', 'کامپیوتر'),
    ('internet', 'اینترنت'),
    ('program', 'برنامه نویسی'),
    ('photoshop', 'فتوشاپ'),
    ('office', 'آفیس'),
    ('english', 'زبان انگلیسی'),
    ('colculate', 'حسابداری'),
]

FAVORITE_CHOICES_LESSON = [
    ('حضوری', 'حضوری'),
    ('آنلاین', 'آنلاین')
]


class PostEduForm(forms.ModelForm):
    kind = forms.ChoiceField(label='درس مورد نظر',widget=forms.RadioSelect, choices=FAVORITE_CHOICES)
    way = forms.ChoiceField(label='نوع تدریس',widget=forms.RadioSelect, choices=FAVORITE_CHOICES_LESSON, )

    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label='توضیحات',
                          widget=forms.Textarea(attrs={'rows': 3}))
    agree = forms.BooleanField(initial=True)
    class Meta:
        model = PostEdu
        fields = ('kind','way', 'phoneNum', 'address', 'bio', 'agree', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('kind'),
            InlineRadios('way'),
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

class PostEnglishForm(forms.ModelForm):
    way = forms.ChoiceField(label='نوع تدریس',widget=forms.RadioSelect, choices=FAVORITE_CHOICES_LESSON, )

    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label='توضیحات',
                          widget=forms.Textarea(attrs={'rows': 3}))
    agree = forms.BooleanField(initial=True)
    class Meta:
        model = PostEnglish
        fields = ('way', 'phoneNum', 'address', 'bio', 'agree', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('way'),
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

class PostPythonForm(forms.ModelForm):
    way = forms.ChoiceField(label='نوع تدریس',widget=forms.RadioSelect, choices=FAVORITE_CHOICES_LESSON, )

    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label='توضیحات',
                          widget=forms.Textarea(attrs={'rows': 3}))
    agree = forms.BooleanField(initial=True)
    class Meta:
        model = PostPython
        fields = ('way', 'phoneNum', 'address', 'bio', 'agree', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('way'),
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

class PostDesignForm(forms.ModelForm):
    way = forms.ChoiceField(label='نوع تدریس',widget=forms.RadioSelect, choices=FAVORITE_CHOICES_LESSON, )

    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label='توضیحات',
                          widget=forms.Textarea(attrs={'rows': 3}))
    agree = forms.BooleanField(initial=True)
    class Meta:
        model = PostDesign
        fields = ('way', 'phoneNum', 'address', 'bio', 'agree', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('way'),
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

class PostBourseForm(forms.ModelForm):
    way = forms.ChoiceField(label='نوع تدریس',widget=forms.RadioSelect, choices=FAVORITE_CHOICES_LESSON, )

    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label='توضیحات',
                          widget=forms.Textarea(attrs={'rows': 3}))
    agree = forms.BooleanField(initial=True)
    class Meta:
        model = PostBourse
        fields = ('way', 'phoneNum', 'address', 'bio', 'agree', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('way'),
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

class PostPhotoForm(forms.ModelForm):
    way = forms.ChoiceField(label='نوع تدریس',widget=forms.RadioSelect, choices=FAVORITE_CHOICES_LESSON, )

    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label='توضیحات',
                          widget=forms.Textarea(attrs={'rows': 3}))
    agree = forms.BooleanField(initial=True)
    class Meta:
        model = PostPhoto
        fields = ('way', 'phoneNum', 'address', 'bio', 'agree', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('way'),
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

class PostPhotoShopForm(forms.ModelForm):
    way = forms.ChoiceField(label='نوع تدریس',widget=forms.RadioSelect, choices=FAVORITE_CHOICES_LESSON, )

    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label='توضیحات',
                          widget=forms.Textarea(attrs={'rows': 3}))
    agree = forms.BooleanField(initial=True)
    class Meta:
        model = PostPhotoShop
        fields = ('way', 'phoneNum', 'address', 'bio', 'agree', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('way'),
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

class PostOfficeForm(forms.ModelForm):
    way = forms.ChoiceField(label='نوع تدریس',widget=forms.RadioSelect, choices=FAVORITE_CHOICES_LESSON, )

    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label='توضیحات',
                          widget=forms.Textarea(attrs={'rows': 3}))
    agree = forms.BooleanField(initial=True)
    class Meta:
        model = PostOffice
        fields = ('way', 'phoneNum', 'address', 'bio', 'agree', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('way'),
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

class PostAutoCadForm(forms.ModelForm):
    way = forms.ChoiceField(label='نوع تدریس',widget=forms.RadioSelect, choices=FAVORITE_CHOICES_LESSON, )

    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label='توضیحات',
                          widget=forms.Textarea(attrs={'rows': 3}))
    agree = forms.BooleanField(initial=True)
    class Meta:
        model = PostAutoCad
        fields = ('way', 'phoneNum', 'address', 'bio', 'agree', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('way'),
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

class PostAccountingForm(forms.ModelForm):
    way = forms.ChoiceField(label='نوع تدریس',widget=forms.RadioSelect, choices=FAVORITE_CHOICES_LESSON, )

    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label='توضیحات',
                          widget=forms.Textarea(attrs={'rows': 3}))
    agree = forms.BooleanField(initial=True)
    class Meta:
        model = PostAccounting
        fields = ('way', 'phoneNum', 'address', 'bio', 'agree', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('way'),
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

class PostVideoForm(forms.ModelForm):
    way = forms.ChoiceField(label='نوع تدریس',widget=forms.RadioSelect, choices=FAVORITE_CHOICES_LESSON, )

    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label='توضیحات',
                          widget=forms.Textarea(attrs={'rows': 3}))
    agree = forms.BooleanField(initial=True)
    class Meta:
        model = PostVideo
        fields = ('way', 'phoneNum', 'address', 'bio', 'agree', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('way'),
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

class PostBasicComputerForm(forms.ModelForm):
    way = forms.ChoiceField(label='نوع تدریس',widget=forms.RadioSelect, choices=FAVORITE_CHOICES_LESSON, )

    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label='توضیحات',
                          widget=forms.Textarea(attrs={'rows': 3}))
    agree = forms.BooleanField(initial=True)
    class Meta:
        model = PostBasicComputer
        fields = ('way', 'phoneNum', 'address', 'bio', 'agree', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('way'),
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

class PostSecondaryComputerForm(forms.ModelForm):
    way = forms.ChoiceField(label='نوع تدریس',widget=forms.RadioSelect, choices=FAVORITE_CHOICES_LESSON, )

    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label='توضیحات',
                          widget=forms.Textarea(attrs={'rows': 3}))
    agree = forms.BooleanField(initial=True)
    class Meta:
        model = PostSecondaryComputer
        fields = ('way', 'phoneNum', 'address', 'bio', 'agree', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('way'),
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

class PostAdvancedComputerForm(forms.ModelForm):
    way = forms.ChoiceField(label='نوع تدریس',widget=forms.RadioSelect, choices=FAVORITE_CHOICES_LESSON, )

    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label='توضیحات',
                          widget=forms.Textarea(attrs={'rows': 3}))
    agree = forms.BooleanField(initial=True)
    class Meta:
        model = PostAdvancedComputer
        fields = ('way', 'phoneNum', 'address', 'bio', 'agree', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('way'),
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

class PostNetForm(forms.ModelForm):
    way = forms.ChoiceField(label='نوع تدریس',widget=forms.RadioSelect, choices=FAVORITE_CHOICES_LESSON, )

    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label='توضیحات',
                          widget=forms.Textarea(attrs={'rows': 3}))
    agree = forms.BooleanField(initial=True)
    class Meta:
        model = PostNet
        fields = ('way', 'phoneNum', 'address', 'bio', 'agree', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('way'),
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

class PostIcdlForm(forms.ModelForm):
    way = forms.ChoiceField(label='نوع تدریس',widget=forms.RadioSelect, choices=FAVORITE_CHOICES_LESSON, )

    phoneNum = forms.IntegerField(label='تلفن ضروری', widget=forms.NumberInput(attrs={'placeholder': 'تلفن ضروری'}))
    address = forms.CharField(label='آدرس دقیق', widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس دقیق'}))
    bio = forms.CharField(label='توضیحات',
                          widget=forms.Textarea(attrs={'rows': 3}))
    agree = forms.BooleanField(initial=True)
    class Meta:
        model = PostIcdl
        fields = ('way', 'phoneNum', 'address', 'bio', 'agree', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios('way'),
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
