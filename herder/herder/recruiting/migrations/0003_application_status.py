# Generated by Django 4.2.7 on 2023-12-10 11:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recruiting", "0002_alter_application_options_application_alts_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="application",
            name="status",
            field=models.CharField(
                choices=[("P", "Pending"), ("A", "Accepted"), ("R", "Rejected"), ("W", "Withdrawn")],
                default="P",
                max_length=1,
            ),
        ),
    ]
