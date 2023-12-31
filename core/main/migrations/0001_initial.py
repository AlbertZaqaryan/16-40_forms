# Generated by Django 4.2.7 on 2023-12-01 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Category name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Sub category name')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_categ', to='main.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Product name')),
                ('price', models.PositiveIntegerField(verbose_name='Product price')),
                ('image', models.ImageField(upload_to='products', verbose_name='Product image')),
                ('active', models.BooleanField(verbose_name='Product active')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat_prod', to='main.subcategory')),
            ],
        ),
    ]
