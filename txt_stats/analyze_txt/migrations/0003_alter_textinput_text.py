# Generated by Django 4.0.5 on 2022-07-01 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyze_txt', '0002_rename_textinputs_textinput'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textinput',
            name='text',
            field=models.TextField(),
        ),
    ]
