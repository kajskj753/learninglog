# Generated by Django 2.0.2 on 2019-03-30 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_auto_20190329_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='data_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]
