# Generated by Django 4.1.5 on 2023-01-26 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_app', '0005_person_study_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='study_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='schedule_app.studygroup'),
        ),
    ]