# Generated by Django 4.0.4 on 2023-10-14 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automail', '0014_emailcampaigntemplate_smtp_error_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailcampaign',
            name='discontinued',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='emailconfiguration',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
