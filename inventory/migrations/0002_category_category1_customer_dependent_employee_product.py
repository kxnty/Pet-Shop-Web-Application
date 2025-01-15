# Generated by Django 3.0.7 on 2023-11-19 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Category1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'types of food',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('c_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=100)),
                ('c_phone', models.CharField(max_length=100)),
                ('c_address', models.CharField(max_length=100)),
                ('c_mail', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Dependent',
            fields=[
                ('d_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('d_name', models.CharField(max_length=100)),
                ('d_relation', models.CharField(max_length=100)),
                ('d_phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('em_id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('em_name', models.CharField(max_length=100)),
                ('em_phone', models.CharField(max_length=100)),
                ('em_address', models.CharField(max_length=100)),
                ('em_mail', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('p_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=100)),
                ('p_company', models.CharField(max_length=100)),
                ('p_price', models.CharField(max_length=100)),
                ('p_number', models.IntegerField()),
                ('p_cat', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventory.Category1')),
                ('p_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='inventory.Category')),
            ],
        ),
    ]
