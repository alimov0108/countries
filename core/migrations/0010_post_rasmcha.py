# Generated by Django 4.1.3 on 2022-12-07 13:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_post_kubok_post_lop_post_mening_post_raqam_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rasmcha',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
