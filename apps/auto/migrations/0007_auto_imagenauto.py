# Generated by Django 3.1.2 on 2020-10-31 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0006_auto_20201028_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='imagenAuto',
            field=models.FileField(default=None, upload_to='imagenAuto'),
        ),
    ]
