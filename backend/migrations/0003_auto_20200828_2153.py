# Generated by Django 3.1 on 2020-08-28 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20200819_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysisresults',
            name='UNIT_ANALYSIS_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.unitanalysis'),
        ),
    ]
