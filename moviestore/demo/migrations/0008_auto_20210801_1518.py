# Generated by Django 3.2.4 on 2021-08-01 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_alter_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='docs',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]