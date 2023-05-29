# Generated by Django 4.2.1 on 2023-05-29 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_request_delete_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='realestate',
            name='description',
            field=models.TextField(default='Очень крутое описание, хорошая квартира на селмаше ростова, тут много пивняков и шаурмичных, спокойный район и нет нефоров, приглашаю, большая квартира и рядом самокат можно взять. круто'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='buyer',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(0, 'Ж'), (1, 'М')], default=0, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='number',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='series',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='surname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
