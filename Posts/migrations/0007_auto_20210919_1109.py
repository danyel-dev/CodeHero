# Generated by Django 3.2.7 on 2021-09-19 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0006_alter_post_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='user',
        ),
        migrations.AddField(
            model_name='comentario',
            name='nome',
            field=models.CharField(default=1, max_length=50, verbose_name='Nome'),
            preserve_default=False,
        ),
    ]
