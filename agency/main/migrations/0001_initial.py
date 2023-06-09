# Generated by Django 4.2.1 on 2023-05-14 00:32

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
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('series', models.CharField(max_length=4)),
                ('number', models.CharField(max_length=6)),
                ('phone', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('type_category', models.CharField(choices=[('ПРОДАЖА', 'Продажа'), ('АРЕНДА', 'Аренда')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('series', models.CharField(max_length=4)),
                ('number', models.CharField(max_length=6)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('series', models.CharField(max_length=4)),
                ('number', models.CharField(max_length=6)),
                ('phone', models.CharField(max_length=20)),
                ('experience', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='RealEstate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_rooms', models.IntegerField()),
                ('metro', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('total_area', models.CharField(max_length=10)),
                ('floor', models.CharField(max_length=4)),
                ('type_real_estate', models.CharField(choices=[('ПРОДАЖА', 'Продажа'), ('АРЕНДА', 'Аренда')], max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.owner')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_order', models.DateTimeField(auto_now_add=True)),
                ('order_status', models.CharField(max_length=50)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.buyer')),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.discount')),
                ('real_estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.realestate')),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.realtor')),
            ],
        ),
    ]
