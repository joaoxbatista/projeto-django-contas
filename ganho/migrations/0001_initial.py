# Generated by Django 3.0 on 2019-12-13 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ganho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now=True, verbose_name='data_criacao')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8)),
                ('descricao', models.TextField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ganhos', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'ganhos',
            },
        ),
    ]
