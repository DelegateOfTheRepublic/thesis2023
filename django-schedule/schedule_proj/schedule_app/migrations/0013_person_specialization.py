# Generated by Django 4.1.5 on 2023-01-27 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_app', '0012_alter_studyday_study_format'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='specialization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='schedule_app.specialization'),
        ),
    ]
