# Generated by Django 4.2.7 on 2023-12-30 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_orderitem_created_at_orderitem_updated_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
