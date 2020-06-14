# Generated by Django 2.2.6 on 2020-06-14 04:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'verbose_name': 'Ingredient', 'verbose_name_plural': 'Ingredients'},
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterModelTable(
            name='ingredient',
            table='ingredient',
        ),
    ]
