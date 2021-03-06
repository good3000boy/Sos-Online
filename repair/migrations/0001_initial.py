# Generated by Django 3.1 on 2021-02-09 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostRep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', multiselectfield.db.fields.MultiSelectField(choices=[('کامپیوتر زمینی', 'کامپیوتر زمینی'), ('لپ تاپ', 'لپ تاپ')], default=('کامپیوتر زمینی', 'کامپیوتر زمینی'), max_length=21, verbose_name='نوع کامپیوتر ')),
                ('req', multiselectfield.db.fields.MultiSelectField(choices=[('درخواست تعمیر در منزل را دارم', 'درخواست تعمیر در منزل را دارم'), ('درخواست ارسال دستگاه به شرکت جهت تعمیر را دارم', 'درخواست ارسال دستگاه به شرکت جهت تعمیر را دارم')], default=('درخواست تعمیر در منزل را دارم', 'درخواست تعمیر در منزل را دارم'), max_length=76, verbose_name='درخواست ')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='توضیح مختضر درباره ایراد دستگاه')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
