# Generated by Django 4.0.1 on 2022-04-06 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(max_length=1000),
        ),
        migrations.DeleteModel(
            name='Position',
        ),
    ]
