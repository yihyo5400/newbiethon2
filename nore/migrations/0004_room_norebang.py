# Generated by Django 2.2.1 on 2019-05-04 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nore', '0003_room_ages'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='norebang',
            field=models.CharField(choices=[('1', '수노래방'), ('2', '라이브노래방'), ('3', '딩기딩기노래방'), ('1', '씽씽노래방')], default='1', max_length=30),
            preserve_default=False,
        ),
    ]
