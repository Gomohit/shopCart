# Generated by Django 4.2.6 on 2023-10-12 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_category_product_image_product_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('person_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=12)),
                ('desc', models.CharField(default=0, max_length=500)),
            ],
        ),
    ]
