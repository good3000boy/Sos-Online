# Generated by Django 3.1 on 2021-02-11 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('repair', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostTV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='توضیح مختضر درباره ایراد دستگاه')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='توضیح مختضر درباره ایراد دستگاه')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostRefrigerator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='توضیح مختضر درباره ایراد دستگاه')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostPhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='توضیح مختضر درباره ایراد دستگاه')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostMonitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='توضیح مختضر درباره ایراد دستگاه')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostLed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='توضیح مختضر درباره ایراد دستگاه')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostIphone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='توضیح مختضر درباره ایراد دستگاه')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostElectric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='توضیح مختضر درباره ایراد دستگاه')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostDigital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='توضیح مختضر درباره ایراد دستگاه')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostCCTV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='توضیح مختضر درباره ایراد دستگاه')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostAlarm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='توضیح مختضر درباره ایراد دستگاه')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
