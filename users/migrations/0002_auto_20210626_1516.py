# Generated by Django 3.2.3 on 2021-06-26 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='default.PNG', null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=19)),
                ('expire_date', models.DateField()),
                ('cvv', models.CharField(max_length=4)),
                ('type', models.CharField(choices=[('Visa', 'Visa'), ('Debit', 'Debit'), ('MasterCard', 'Master Card'), ('AmericanExpress', 'American Express')], max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255, null=True)),
                ('province', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('street', models.CharField(max_length=255, null=True)),
                ('apartment_number', models.FloatField(max_length=10, null=True)),
                ('postal_code', models.CharField(max_length=10, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
