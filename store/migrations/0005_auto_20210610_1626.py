# Generated by Django 3.1.7 on 2021-06-10 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20210608_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='picture',
            field=models.ImageField(blank=True, default='#imageurl', null=True, upload_to='item_pics'),
        ),
    ]
