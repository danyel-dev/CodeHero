# Generated by Django 3.2.7 on 2021-09-17 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagem',
            field=models.ImageField(default=1, upload_to='post_img/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]