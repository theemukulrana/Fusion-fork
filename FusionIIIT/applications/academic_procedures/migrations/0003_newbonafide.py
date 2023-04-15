# Generated by Django 3.1.5 on 2023-04-15 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_procedures', '0002_duetype_newdue'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewBonafide',
            fields=[
                ('purpose', models.CharField(max_length=255)),
                ('roll_no', models.CharField(max_length=50)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('check', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'new_bonafide',
            },
        ),
    ]
