# Generated by Django 5.0.2 on 2024-04-29 06:10

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AdminApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('card_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('cvv', models.CharField(max_length=10)),
                ('expiry', models.CharField(max_length=10)),
                ('balance', models.FloatField(default=10000)),
            ],
            options={
                'db_table': 'Payment',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Status',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
            ],
            options={
                'db_table': 'UserInfo',
            },
        ),
        migrations.CreateModel(
            name='Order_Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_order', models.DateField(default=datetime.datetime(2024, 4, 29, 11, 40, 57, 449813))),
                ('amount', models.FloatField(default=1000)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='UserApp.userinfo')),
            ],
            options={
                'db_table': 'OrderMaster',
            },
        ),
        migrations.CreateModel(
            name='MyCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
                ('cake', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='AdminApp.cake')),
                ('order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UserApp.order_master')),
                ('status', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='UserApp.status')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='UserApp.userinfo')),
            ],
            options={
                'db_table': 'MyCart',
            },
        ),
    ]
