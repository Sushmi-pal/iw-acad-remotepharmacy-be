# Generated by Django 3.1 on 2020-08-11 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='medicine_pic')),
                ('desc', models.TextField()),
                ('price', models.CharField(max_length=30)),
                ('in_stock', models.CharField(max_length=30)),
                ('prod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='datahandle.category')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('num_of_items_purchased', models.IntegerField()),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datahandle.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_in_cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datahandle.order')),
                ('usercart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]