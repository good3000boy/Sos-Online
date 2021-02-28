# Generated by Django 3.1 on 2021-02-12 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('education', '0002_auto_20210209_2046'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('way', models.CharField(choices=[('حضوری', 'حضوری'), ('آنلاین', 'آنلاین')], default=('حضوری', 'حضوری'), max_length=6, verbose_name='روش تدریس')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='توضیحات')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostSecondaryComputer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('way', models.CharField(choices=[('حضوری', 'حضوری'), ('آنلاین', 'آنلاین')], default=('حضوری', 'حضوری'), max_length=6, verbose_name='روش تدریس')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='توضیحات')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostPython',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('way', models.CharField(choices=[('حضوری', 'حضوری'), ('آنلاین', 'آنلاین')], default=('حضوری', 'حضوری'), max_length=6, verbose_name='روش تدریس')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='توضیحات')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostPhotoShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('way', models.CharField(choices=[('حضوری', 'حضوری'), ('آنلاین', 'آنلاین')], default=('حضوری', 'حضوری'), max_length=6, verbose_name='روش تدریس')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='توضیحات')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('way', models.CharField(choices=[('حضوری', 'حضوری'), ('آنلاین', 'آنلاین')], default=('حضوری', 'حضوری'), max_length=6, verbose_name='روش تدریس')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='توضیحات')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostOffice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('way', models.CharField(choices=[('حضوری', 'حضوری'), ('آنلاین', 'آنلاین')], default=('حضوری', 'حضوری'), max_length=6, verbose_name='روش تدریس')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='توضیحات')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostNet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('way', models.CharField(choices=[('حضوری', 'حضوری'), ('آنلاین', 'آنلاین')], default=('حضوری', 'حضوری'), max_length=6, verbose_name='روش تدریس')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='توضیحات')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostIcdl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('way', models.CharField(choices=[('حضوری', 'حضوری'), ('آنلاین', 'آنلاین')], default=('حضوری', 'حضوری'), max_length=6, verbose_name='روش تدریس')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='توضیحات')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostEnglish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('way', models.CharField(choices=[('حضوری', 'حضوری'), ('آنلاین', 'آنلاین')], default=('حضوری', 'حضوری'), max_length=6, verbose_name='روش تدریس')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='توضیحات')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostDesign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('way', models.CharField(choices=[('حضوری', 'حضوری'), ('آنلاین', 'آنلاین')], default=('حضوری', 'حضوری'), max_length=6, verbose_name='روش تدریس')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='توضیحات')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostBourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('way', models.CharField(choices=[('حضوری', 'حضوری'), ('آنلاین', 'آنلاین')], default=('حضوری', 'حضوری'), max_length=6, verbose_name='روش تدریس')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='توضیحات')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostBasicComputer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('way', models.CharField(choices=[('حضوری', 'حضوری'), ('آنلاین', 'آنلاین')], default=('حضوری', 'حضوری'), max_length=6, verbose_name='روش تدریس')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='توضیحات')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostAutoCad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('way', models.CharField(choices=[('حضوری', 'حضوری'), ('آنلاین', 'آنلاین')], default=('حضوری', 'حضوری'), max_length=6, verbose_name='روش تدریس')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='توضیحات')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostAdvancedComputer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('way', models.CharField(choices=[('حضوری', 'حضوری'), ('آنلاین', 'آنلاین')], default=('حضوری', 'حضوری'), max_length=6, verbose_name='روش تدریس')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='توضیحات')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostAccounting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('way', models.CharField(choices=[('حضوری', 'حضوری'), ('آنلاین', 'آنلاین')], default=('حضوری', 'حضوری'), max_length=6, verbose_name='روش تدریس')),
                ('phoneNum', models.CharField(default='', max_length=11, verbose_name='تلفن ضروری')),
                ('address', models.TextField(default='', max_length=200, verbose_name='آدرس دقیق')),
                ('bio', models.TextField(default='', max_length=500, verbose_name='توضیحات')),
                ('agree', models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]