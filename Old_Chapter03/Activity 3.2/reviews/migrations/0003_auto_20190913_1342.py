# Generated by Django 3.0a1 on 2019-09-13 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_remove_publisher_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(help_text='The name of the Publisher.', max_length=255),
        ),
    ]
