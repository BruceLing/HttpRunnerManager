# Generated by Django 2.0.3 on 2018-04-24 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ApiManager', '0002_remove_moduleinfo_lifting_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moduleinfo',
            name='status',
        ),
        migrations.RemoveField(
            model_name='projectinfo',
            name='status',
        ),
        migrations.RemoveField(
            model_name='testcaseinfo',
            name='status',
        ),
        migrations.RemoveField(
            model_name='testreports',
            name='status',
        ),
    ]