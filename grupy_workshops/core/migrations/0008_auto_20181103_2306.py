# Generated by Django 2.1.2 on 2018-11-04 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20181103_2256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workshops',
            name='palestrantes',
        ),
        migrations.AddField(
            model_name='workshops',
            name='palestrante',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tutor', to='core.Palestrantes'),
        ),
    ]
