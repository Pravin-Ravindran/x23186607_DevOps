# Generated by Django 2.1.15 on 2024-03-15 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewNest', '0004_remove_pet_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
