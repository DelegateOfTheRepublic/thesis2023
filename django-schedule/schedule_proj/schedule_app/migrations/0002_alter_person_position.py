# Generated by Django 4.1.5 on 2023-01-21 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='schedule_app.position'),
        ),
    ]