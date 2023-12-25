# Generated by Django 5.0 on 2023-12-22 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('short_size', models.CharField(choices=[('S', 'Small'), ('L', 'Litle'), ('M', 'Middle')], max_length=1)),
                ('image', models.ImageField(blank=True, upload_to='image_product')),
            ],
        ),
    ]
