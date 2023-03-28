# Generated by Django 4.1.7 on 2023-03-25 08:00

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShopeeItem',
            fields=[
                ('itemid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('shopid', models.BigIntegerField()),
                ('currency', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('stock', models.BigIntegerField(blank=True, null=True)),
                ('sold', models.BigIntegerField(blank=True, null=True)),
                ('historical_sold', models.BigIntegerField(blank=True, null=True)),
                ('liked_count', models.BigIntegerField(blank=True, null=True)),
                ('brand', models.CharField(blank=True, max_length=255, null=True)),
                ('cmt_count', models.BigIntegerField(blank=True, null=True)),
                ('item_status', models.CharField(blank=True, max_length=255, null=True)),
                ('price', models.BigIntegerField(blank=True, null=True)),
                ('price_min', models.BigIntegerField(blank=True, null=True)),
                ('price_max', models.BigIntegerField(blank=True, null=True)),
                ('price_before_discount', models.BigIntegerField(blank=True, null=True)),
                ('show_discount', models.BigIntegerField(blank=True, null=True)),
                ('raw_discount', models.BigIntegerField(blank=True, null=True)),
                ('is_official_shop', models.CharField(blank=True, max_length=100, null=True)),
                ('avatar', models.CharField(blank=True, max_length=255, null=True)),
                ('shop_location', models.CharField(blank=True, max_length=255, null=True)),
            ],
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(blank=True, max_length=150, null=True)),
                ('itemid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.shopeeitem')),
            ],
        ),
    ]