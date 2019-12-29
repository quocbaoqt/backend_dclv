# Generated by Django 2.2.5 on 2019-12-29 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apartment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApartmentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('studio', 'Studio'), ('duplex_house', 'Duplex House'), ('apartment', 'Apartment')], default='studio', max_length=50, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ApartmentLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.TextField()),
                ('district', models.TextField()),
                ('address', models.TextField()),
                ('notes', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('apartment', models.ForeignKey(db_column='apartment_id', on_delete=django.db.models.deletion.CASCADE, related_name='apartment_location', to='apartment.Apartment')),
            ],
        ),
    ]
