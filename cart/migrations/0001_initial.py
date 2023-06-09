# Generated by Django 4.1.7 on 2023-03-29 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0002_alter_itemimage_itemid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('totalcost', models.BigIntegerField()),
                ('is_odered', models.BooleanField(default=False)),
                ('is_finished', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
               
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('quantity', models.IntegerField()),
                ('price', models.BigIntegerField()),
                ('itemid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='store.shopeeitem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cart.order')),
            ],
        ),
    ]
