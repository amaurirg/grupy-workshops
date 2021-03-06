# Generated by Django 2.1.2 on 2018-11-04 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20181103_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palestrantes',
            name='id_telegram',
            field=models.PositiveIntegerField(blank=True, max_length=20, null=True, verbose_name='Id Telegram'),
        ),
        migrations.AlterField(
            model_name='workshops',
            name='total_participantes',
            field=models.PositiveSmallIntegerField(blank=True, max_length=4, null=True, verbose_name='Total de Participantes'),
        ),
        migrations.AlterField(
            model_name='workshops',
            name='votos',
            field=models.PositiveSmallIntegerField(blank=True, max_length=4, null=True, verbose_name='Votos'),
        ),
    ]
