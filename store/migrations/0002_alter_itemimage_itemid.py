# Generated by Django 4.1.7 on 2023-03-29 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemimage',
            name='itemid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='store.shopeeitem'),
        ),
    ]