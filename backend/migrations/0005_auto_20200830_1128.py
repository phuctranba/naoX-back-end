# Generated by Django 3.1 on 2020-08-30 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20200830_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysisresults',
            name='UNIT_ANALYSIS_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.unitanalysis'),
        ),
    ]
