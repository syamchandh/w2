# Generated by Django 4.0.3 on 2022-03-31 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0002_remove_productdetails_designation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productdetails',
            old_name='Qualification',
            new_name='Gend',
        ),
        migrations.RenameField(
            model_name='productdetails',
            old_name='gender',
            new_name='Quali',
        ),
    ]
