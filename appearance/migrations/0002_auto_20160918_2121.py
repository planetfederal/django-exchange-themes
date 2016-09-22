from __future__ import unicode_literals
from django.db import migrations


def load_themes(apps, schema_editor):
    Theme = apps.get_model("appearance", "Theme")
    theme_geoint = Theme(
        name="GEOINT",
        description="GEOINT Services Theme",
        default_theme=True,
        active_theme=False,
        title=" ",
        tagline="A Platform for Geospatial Collaboration",
        running_hex="0f1a2c",
        running_text_hex="ffffff",
        running_link_hex="506a94",
        pb_text="Boundless Spatial",
        pb_link="http://boundlessgeo.com/",
        docs_link="https://boundlessgeo.github.io/exchange-documentation/",
        background_logo="theme/img/geoint-background.png",
        primary_logo="theme/img/geoint-primary-logo.png",
        banner_logo="theme/img/geoint-banner-logo.png"
    )
    theme_geoint.save()


class Migration(migrations.Migration):

    dependencies = [
        ('appearance', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_themes),
    ]
