# Generated by Django 2.2.3 on 2019-08-02 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20190802_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group_account',
            name='use',
            field=models.ManyToManyField(to='mainapp.User_account'),
        ),
    ]
