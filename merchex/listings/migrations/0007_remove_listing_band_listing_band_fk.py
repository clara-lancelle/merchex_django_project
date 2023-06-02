# Generated by Django 4.2.1 on 2023-06-01 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_rename_band_fk_listing_band'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='band',
        ),
        migrations.AddField(
            model_name='listing',
            name='band_fk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.band'),
        ),
    ]
