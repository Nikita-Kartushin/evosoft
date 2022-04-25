# Generated by Django 4.0.4 on 2022-04-25 21:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('diaries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='expiration',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='diary',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]