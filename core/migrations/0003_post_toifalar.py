# Generated by Django 4.1.3 on 2022-12-05 14:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post_date_alter_post_name_alter_post_yaratgan'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='toifalar',
            field=models.CharField(default=django.utils.timezone.now, max_length=55),
            preserve_default=False,
        ),
    ]