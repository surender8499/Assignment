# Generated by Django 2.2.10 on 2020-06-26 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='user_id',
            field=models.IntegerField(default=2035),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='members',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]