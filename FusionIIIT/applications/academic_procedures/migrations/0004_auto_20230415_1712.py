# Generated by Django 3.1.5 on 2023-04-15 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_procedures', '0003_newbonafide'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonafide',
            name='purpose',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='bonafide',
            name='student_name',
            field=models.CharField(max_length=100),
        ),
    ]
