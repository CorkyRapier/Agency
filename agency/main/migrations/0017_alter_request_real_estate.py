# Generated by Django 4.2.1 on 2023-05-29 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_realestate_description_alter_buyer_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='real_estate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='e_request', to='main.realestate'),
        ),
    ]
