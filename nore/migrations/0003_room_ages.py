# Generated by Django 2.2.1 on 2019-05-04 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nore', '0002_room_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='ages',
            field=models.CharField(choices=[('10대', '10대'), ('20대', '20대'), ('30대', '30대'), ('40대', '40대'), ('50대', '50대')], default='10대', max_length=10),
            preserve_default=False,
        ),
    ]
