# Generated by Django 5.0.4 on 2024-05-04 17:20

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='only_medias/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'mp4', 'avi', 'mov', 'gif', 'webp', 'pdf', 'doc', 'docx', 'mpeg'])], verbose_name='File')),
                ('file_type', models.CharField(choices=[('image', 'Image'), ('video', 'Video'), ('document', 'document'), ('gif', 'Gif'), ('other', 'Other')], max_length=10, verbose_name='File Type')),
            ],
            options={
                'verbose_name': 'Media',
                'verbose_name_plural': 'Media',
            },
        ),
        migrations.CreateModel(
            name='CommonSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_phone_number', models.CharField(max_length=20, verbose_name='Main Phone Number')),
                ('our_clinic_text', models.TextField(verbose_name='Our Clinic Text')),
                ('contact_page_back_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_page_back_image', to='common.media', verbose_name='Contacts Page Back Image')),
                ('product_page_back_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_page_back_image', to='common.media', verbose_name='Product Page Back Image')),
                ('service_page_back_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_page_back_image', to='common.media', verbose_name='Service Page Back Image')),
                ('vacancy_page_back_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancy_page_back_image', to='common.media', verbose_name='Vacancy Page Back Image')),
            ],
            options={
                'verbose_name': 'Common Settings',
                'verbose_name_plural': 'Common Settings',
            },
        ),
    ]
