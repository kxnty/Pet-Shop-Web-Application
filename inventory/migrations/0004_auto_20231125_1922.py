# Generated by Django 3.0.7 on 2023-11-25 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_receipt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='p_price',
            field=models.IntegerField(),
        ),
    ]
