# Generated by Django 2.2.12 on 2021-02-09 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mutaions_commits', '0003_auto_20210209_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mutationcommit',
            name='error',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]