# Generated by Django 3.0.2 on 2020-01-24 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datadd',
            fields=[
                ('Name', models.CharField(max_length=100)),
                ('ID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Year', models.IntegerField()),
                ('Dept', models.CharField(max_length=50)),
                ('Mbno', models.CharField(max_length=20)),
                ('Gender', models.CharField(max_length=20)),
                ('Gmail', models.CharField(max_length=100)),
                ('Roomalloted', models.CharField(max_length=20)),
                ('AmountPaid', models.IntegerField()),
                ('Academicyear', models.IntegerField()),
                ('ParentMbno', models.IntegerField()),
                ('CautionDeposit', models.CharField(max_length=50)),
            ],
        ),
    ]
