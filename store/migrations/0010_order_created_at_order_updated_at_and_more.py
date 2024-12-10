# Generated by Django 5.1.1 on 2024-10-04 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_cart_item_created_at_cart_item_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2024-02-02'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='order_item',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2024-02-02'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order_item',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]