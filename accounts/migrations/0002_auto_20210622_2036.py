# Generated by Django 3.2 on 2021-06-22 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='tweet',
            new_name='found',
        ),
        migrations.RenameField(
            model_name='tweet',
            old_name='depression',
            new_name='not_found',
        ),
        migrations.AddField(
            model_name='tweet',
            name='username',
            field=models.CharField(default='username', max_length=200),
        ),
    ]
