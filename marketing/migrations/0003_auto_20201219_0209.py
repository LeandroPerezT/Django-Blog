# Generated by Django 3.1.4 on 2020-12-19 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0002_hero'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='name',
            field=models.CharField(default=True, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hero',
            name='featured',
            field=models.BooleanField(),
        ),
    ]
