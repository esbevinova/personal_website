# Generated by Django 3.0.1 on 2019-12-29 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infoapp', '0002_auto_20191229_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='technology',
            field=models.TextField(),
        ),
    ]
