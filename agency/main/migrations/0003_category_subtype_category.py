# Generated by Django 4.2.1 on 2023-05-14 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_buyer_gender_owner_gender_realtor_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='subtype_category',
            field=models.CharField(choices=[('ЖИЛАЯ', 'Жилая'), ('ЗАГОРОДНАЯ', 'Загородная'), ('КОММЕРЧЕСКАЯ', 'Коммерческая')], default='ЖИЛАЯ', max_length=20),
        ),
    ]
