# Generated by Django 4.0.5 on 2022-07-03 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyze_txt', '0004_textinput_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textinput',
            name='case_sensitive',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
