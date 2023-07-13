# Generated by Django 3.2.4 on 2023-07-13 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customerDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Customer Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Customer Email')),
                ('available_bal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='transactionDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Transactions Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Transaction Email')),
                ('debitted_amt', models.IntegerField()),
                ('credited_amt', models.IntegerField()),
                ('account_bal', models.IntegerField()),
            ],
        ),
    ]
