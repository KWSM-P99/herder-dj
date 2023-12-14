# Generated by Django 4.2.7 on 2023-12-10 11:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recruiting", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="application",
            options={"ordering": ["-created_at"], "verbose_name_plural": "applications"},
        ),
        migrations.AddField(
            model_name="application",
            name="alts",
            field=models.TextField(
                blank=True,
                default="I declined to answer.",
                help_text="What are the names and levels of your alts and would you like these characters invited to the guild as well?",
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="characteristics",
            field=models.TextField(
                blank=True,
                default="I declined to answer.",
                help_text="What sorts of characteristics will you bring (or hope to bring) to Kittens?",
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="class_name",
            field=models.CharField(
                blank=True,
                choices=[
                    ("WAR", "Warrior"),
                    ("ROG", "Rogue"),
                    ("CLR", "Cleric"),
                    ("RNG", "Ranger"),
                    ("SHD", "Shadow Knight"),
                    ("DRU", "Druid"),
                    ("MNK", "Monk"),
                    ("BRD", "Bard"),
                    ("PAL", "Paladin"),
                    ("SHM", "Shaman"),
                    ("NEC", "Necromancer"),
                    ("ENC", "Enchanter"),
                    ("WIZ", "Wizard"),
                    ("MAG", "Magician"),
                    ("BER", "Berserker"),
                ],
                default="WAR",
                max_length=3,
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="comments",
            field=models.TextField(
                blank=True, default="I declined to answer.", help_text="Additional comments you'd like to add"
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="expectations",
            field=models.TextField(
                blank=True,
                default="I declined to answer.",
                help_text="What are your expectations of being a member of Kittens Who Say Meow, and what can Kittens Who Say Meow expect from you?",
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="group_in_fireplace",
            field=models.TextField(
                blank=True,
                default="I declined to answer.",
                help_text="Your group is in the Fireplace in Unrest, and another group moves to the hallway leading downstairs and starts pulling monsters over your group without saying anything. How do you react?",
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="grouped_with_anyone",
            field=models.TextField(
                blank=True,
                default="I declined to answer.",
                help_text="Have you grouped or spent quality time with any Kittens?",
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="know_anyone",
            field=models.TextField(
                blank=True, default="I declined to answer.", help_text="Do you know anyone in Kittens?"
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="level",
            field=models.IntegerField(blank=True, default=15, help_text="What is your character's level?"),
        ),
        migrations.AddField(
            model_name="application",
            name="main_character",
            field=models.CharField(blank=True, help_text="What is your character's name?", max_length=64),
        ),
        migrations.AddField(
            model_name="application",
            name="reason",
            field=models.TextField(
                blank=True,
                default="I declined to answer.",
                help_text="Why would you like to join Kittens Who Say Meow?",
            ),
        ),
    ]
