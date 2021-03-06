# Generated by Django 2.2.4 on 2019-08-04 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_auto_20190802_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_account',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='user_account',
            name='nickname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='group_account',
            name='group_money',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
