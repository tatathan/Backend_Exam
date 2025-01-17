# Generated by Django 5.0.4 on 2024-07-21 22:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_classroom_school_alter_student_classroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='school',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.school'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='year',
            field=models.PositiveIntegerField(),
        ),
    ]
