# Generated by Django 2.0 on 2018-05-17 04:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0003_auto_20180504_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=200)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='date reserved')),
            ],
        ),
        migrations.AlterField(
            model_name='productos',
            name='image',
            field=models.ImageField(default='img/photos/default.png', upload_to='img/photos/'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.Productos'),
        ),
    ]