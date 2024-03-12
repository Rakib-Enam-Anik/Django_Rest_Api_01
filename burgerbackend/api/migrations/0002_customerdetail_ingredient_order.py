# Generated by Django 5.0.2 on 2024-03-11 10:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliveryAddress', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=20)),
                ('paymentType', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salad', models.IntegerField(default=0)),
                ('cheese', models.IntegerField(default=0)),
                ('meat', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(default='0', max_length=10)),
                ('orderTime', models.CharField(blank=True, max_length=40)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.customerdetail')),
                ('ingredients', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.ingredient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]