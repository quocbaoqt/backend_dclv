# Generated by Django 2.2.5 on 2019-12-15 10:16

from decimal import Decimal
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import lvtn_apps.utils.method_utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=15, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999999999999)])),
                ('status', models.TextField()),
                ('city', models.TextField()),
                ('district', models.TextField()),
                ('address', models.TextField()),
                ('notes', models.TextField()),
                ('living_rooms', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=50)),
                ('dinning_rooms', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=50)),
                ('bed_rooms', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=50)),
                ('bath_rooms', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=50)),
                ('toilets', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=50)),
                ('kitchen', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], default='0', max_length=50)),
                ('furnitures', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, size=12)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('image_1', models.FileField(blank=True, null=True, upload_to=lvtn_apps.utils.method_utils.generate_name_image, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg', 'svg'])])),
                ('image_2', models.FileField(blank=True, null=True, upload_to=lvtn_apps.utils.method_utils.generate_name_image, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg', 'svg'])])),
                ('image_3', models.FileField(blank=True, null=True, upload_to=lvtn_apps.utils.method_utils.generate_name_image, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg', 'svg'])])),
                ('image_4', models.FileField(blank=True, null=True, upload_to=lvtn_apps.utils.method_utils.generate_name_image, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg', 'svg'])])),
                ('image_5', models.FileField(blank=True, null=True, upload_to=lvtn_apps.utils.method_utils.generate_name_image, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg', 'svg'])])),
                ('image_6', models.FileField(blank=True, null=True, upload_to=lvtn_apps.utils.method_utils.generate_name_image, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg', 'svg'])])),
                ('image_7', models.FileField(blank=True, null=True, upload_to=lvtn_apps.utils.method_utils.generate_name_image, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg', 'svg'])])),
                ('image_8', models.FileField(blank=True, null=True, upload_to=lvtn_apps.utils.method_utils.generate_name_image, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg', 'svg'])])),
                ('cover', models.FileField(blank=True, null=True, upload_to=lvtn_apps.utils.method_utils.generate_name_image, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg', 'svg'])])),
            ],
        ),
        migrations.CreateModel(
            name='ApartmentServices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cost', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=15, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(999999999999)])),
                ('apartment', models.ForeignKey(db_column='apartment_id', on_delete=django.db.models.deletion.CASCADE, related_name='apartment_services', to='apartment.Apartment')),
            ],
        ),
    ]