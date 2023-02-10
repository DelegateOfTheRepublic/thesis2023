# Generated by Django 4.1.5 on 2023-01-26 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_app', '0009_alter_studyday_day_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studyday',
            name='day_number',
            field=models.CharField(choices=[('0', 'Понедельник'), ('1', 'Вторник'), ('2', 'Среда'), ('3', 'Четверг'), ('4', 'Пятница'), ('5', 'Суббота')], max_length=1),
        ),
    ]