# Generated by Django 5.0.1 on 2024-01-08 15:37

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("admin_interface", "0030_theme_collapsible_stacked_inlines_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="theme",
            name="css_body_background_color",
            field=colorfield.fields.ColorField(
                blank=True,
                default="#fff",
                help_text="#fff",
                image_field=None,
                max_length=10,
                samples=None,
                verbose_name="background color",
            ),
        ),
        migrations.AddField(
            model_name="theme",
            name="css_body_foreground_color",
            field=colorfield.fields.ColorField(
                blank=True,
                default="#333",
                help_text="#333",
                image_field=None,
                max_length=10,
                samples=None,
                verbose_name="foreground color",
            ),
        ),
        migrations.AddField(
            model_name="theme",
            name="css_body_loud_color",
            field=colorfield.fields.ColorField(
                blank=True,
                default="#000",
                help_text="#000",
                image_field=None,
                max_length=10,
                samples=None,
                verbose_name="loud color",
            ),
        ),
        migrations.AddField(
            model_name="theme",
            name="css_body_quiet_color",
            field=colorfield.fields.ColorField(
                blank=True,
                default="#666",
                help_text="#666",
                image_field=None,
                max_length=10,
                samples=None,
                verbose_name="quiet color",
            ),
        ),
    ]
