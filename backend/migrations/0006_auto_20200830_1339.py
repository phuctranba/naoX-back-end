# Generated by Django 3.1 on 2020-08-30 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20200830_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysisresults',
            name='CREATE_DATE',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='analysisresults',
            name='UPDATE_DATE',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='unitanalysis',
            name='ACTIVE',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='unitanalysis',
            name='CAMPAIGN_ID',
            field=models.UUIDField(),
        ),
        migrations.AlterField(
            model_name='unitanalysis',
            name='CREATE_DATE',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='unitanalysis',
            name='KEY_MAIN',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='unitanalysis',
            name='KEY_PLACE',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='unitanalysis',
            name='NAME',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='unitanalysis',
            name='UPDATE_DATE',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='unitanalysis',
            name='VERSION',
            field=models.IntegerField(default=0),
        ),
    ]
