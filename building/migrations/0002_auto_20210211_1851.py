# Generated by Django 3.1 on 2021-02-11 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('building', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostBuil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', multiselectfield.db.fields.MultiSelectField(choices=[('نوسازی', 'نوسازی'), ('ساخت', 'ساخت')], default=('نوسازی', 'نوسازی'), max_length=11, verbose_name='نوع سازه ')),
                ('area', models.CharField(default='', max_length=11, verbose_name='متراژ')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق محل')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='شرح درخواست')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='PostCom',
        ),
    ]
