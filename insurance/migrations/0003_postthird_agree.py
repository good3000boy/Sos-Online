# Generated by Django 3.1 on 2021-02-12 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0002_postthird'),
    ]

    operations = [
        migrations.AddField(
            model_name='postthird',
            name='agree',
            field=models.BooleanField(default=True, verbose_name='با کلیه شرایط شرکت موافقم'),
        ),
    ]
