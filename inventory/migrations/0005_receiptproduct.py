# Generated by Django 3.0.7 on 2023-11-26 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20231125_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceiptProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Product')),
                ('receipt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Receipt')),
            ],
        ),
    ]
