# Generated by Django 4.2.7 on 2023-11-28 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='yugioh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('power', models.CharField(max_length=100)),
                ('defense', models.CharField(max_length=100)),
                ('foto', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='yugioh1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last', models.CharField(max_length=100)),
                ('test', models.CharField(max_length=100)),
                ('prueba', models.CharField(max_length=100)),
                ('cards', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.yugioh')),
            ],
        ),
    ]
