# Generated by Django 5.0.4 on 2024-05-04 17:20

import ckeditor.fields
import common.utils
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
                ('special_offer', models.BooleanField(default=False, verbose_name='special offer')),
                ('short_desc', models.TextField(verbose_name='short description')),
                ('desc', ckeditor.fields.RichTextField(verbose_name='description')),
                ('expires_in', models.DateTimeField(verbose_name='expires in')),
                ('percentage', models.PositiveSmallIntegerField(verbose_name='percentage')),
                ('in_discount', models.BooleanField(default=False, verbose_name='in discount')),
            ],
            options={
                'verbose_name': 'action',
                'verbose_name_plural': 'actions',
            },
        ),
        migrations.CreateModel(
            name='ActionTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
            ],
            options={
                'verbose_name': 'action tag',
                'verbose_name_plural': 'action tags',
            },
        ),
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
            ],
            options={
                'verbose_name': 'article category',
                'verbose_name_plural': 'article categories',
            },
        ),
        migrations.CreateModel(
            name='ContactChiefDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20, validators=[common.utils.validate_phone_number], verbose_name='phone number')),
                ('full_name', models.CharField(max_length=120, verbose_name='full name')),
                ('message', models.TextField(verbose_name='message')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
            ],
            options={
                'verbose_name': 'contact chief doctor',
                'verbose_name_plural': 'contact chief doctors',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=120, verbose_name='address')),
                ('phone_number', models.CharField(max_length=20, validators=[common.utils.validate_phone_number], verbose_name='phone number')),
                ('work_time', models.CharField(max_length=120, verbose_name='work time')),
                ('telegram', models.URLField(validators=[django.core.validators.RegexValidator('^https?:\\/\\/t\\.me\\/[A-Za-z0-9_]{5,}$')], verbose_name='telegram')),
                ('instagram', models.URLField(validators=[django.core.validators.RegexValidator('^https?:\\/\\/www\\.instagram\\.com\\/[A-Za-z0-9_]{5,}$')], verbose_name='instagram')),
                ('facebook', models.URLField(validators=[django.core.validators.RegexValidator('^https?:\\/\\/www\\.facebook\\.com\\/[A-Za-z0-9_]{5,}$')], verbose_name='facebook')),
                ('vkontact', models.URLField(validators=[django.core.validators.RegexValidator('^https?:\\/\\/vk\\.com\\/[A-Za-z0-9_]{5,}$')], verbose_name='vkontact')),
                ('location', models.URLField(verbose_name='location')),
            ],
            options={
                'verbose_name': 'Contacts',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='NewsTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
            ],
            options={
                'verbose_name': 'news tag',
                'verbose_name_plural': 'news tags',
            },
        ),
        migrations.CreateModel(
            name='OnlineAppointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20, verbose_name='phone number')),
                ('full_name', models.CharField(max_length=120, verbose_name='full name')),
                ('book_date', models.DateField(verbose_name='book date')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
            ],
            options={
                'verbose_name': 'online appointment',
                'verbose_name_plural': 'online appointments',
            },
        ),
        migrations.CreateModel(
            name='PhotoGalleryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
            ],
        ),
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', ckeditor.fields.RichTextField(verbose_name='summary')),
                ('video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.media', verbose_name='video')),
            ],
            options={
                'verbose_name': 'about us',
                'verbose_name_plural': 'about us',
            },
        ),
        migrations.CreateModel(
            name='ActionImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='action_images', to='clinics.action', verbose_name='action')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.media', verbose_name='image')),
            ],
            options={
                'verbose_name': 'action image',
                'verbose_name_plural': 'action images',
            },
        ),
        migrations.AddField(
            model_name='action',
            name='tags',
            field=models.ManyToManyField(blank=True, to='clinics.actiontag', verbose_name='action tag'),
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
                ('desc', ckeditor.fields.RichTextField(verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('published', models.BooleanField(default=False, verbose_name='published')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.media')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='clinics.articlecategory')),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': 'articles',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120, verbose_name='full name')),
                ('text', models.TextField(verbose_name='text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('phone_number', models.CharField(max_length=20, validators=[common.utils.validate_phone_number], verbose_name='phone number')),
                ('is_view', models.BooleanField(default=False, verbose_name='is view')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.media')),
            ],
            options={
                'verbose_name': 'feedback',
                'verbose_name_plural': 'feedbacks',
            },
        ),
        migrations.CreateModel(
            name='HomeSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
                ('desc', models.TextField(verbose_name='description')),
                ('file', models.ForeignKey(help_text='image or gif', on_delete=django.db.models.deletion.CASCADE, to='common.media')),
            ],
            options={
                'verbose_name': 'home slider',
                'verbose_name_plural': 'home sliders',
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.media', verbose_name='photo')),
            ],
            options={
                'verbose_name': 'license',
                'verbose_name_plural': 'licences',
            },
        ),
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.media')),
            ],
            options={
                'verbose_name': 'news category',
                'verbose_name_plural': 'news categories',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
                ('desc', ckeditor.fields.RichTextField(verbose_name='text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('special_offer', models.BooleanField(default=False, verbose_name='special offer')),
                ('published', models.BooleanField(default=False, verbose_name='published')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.media')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinics.newscategory')),
                ('tags', models.ManyToManyField(blank=True, to='clinics.newstag', verbose_name='news tag')),
            ],
            options={
                'verbose_name': 'news',
                'verbose_name_plural': 'news',
            },
        ),
        migrations.CreateModel(
            name='PhotoGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.media', verbose_name='photo')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinics.photogallerycategory', verbose_name='category')),
            ],
            options={
                'verbose_name': 'photo gallery',
                'verbose_name_plural': 'photo galleries',
            },
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120, verbose_name='full name')),
                ('position', models.CharField(max_length=120, verbose_name='position')),
                ('about', ckeditor.fields.RichTextField(verbose_name='about')),
                ('certificates', ckeditor.fields.RichTextField(verbose_name='certificate')),
                ('experience_in_company', models.CharField(max_length=10, verbose_name='experience in company')),
                ('experience_in_field', models.CharField(max_length=10, verbose_name='experience in field')),
                ('experience_in_years', models.CharField(max_length=10, verbose_name='experience in years')),
                ('photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.media')),
            ],
            options={
                'verbose_name': 'specialist',
                'verbose_name_plural': 'specialists',
            },
        ),
        migrations.CreateModel(
            name='Diploma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.media', verbose_name='file')),
                ('specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diplomas', to='clinics.specialist')),
            ],
            options={
                'verbose_name': 'diploma',
                'verbose_name_plural': 'diplomas',
            },
        ),
        migrations.CreateModel(
            name='StoryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.media')),
            ],
            options={
                'verbose_name': 'story category',
                'verbose_name_plural': 'story categories',
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
                ('order', models.IntegerField(verbose_name='order')),
                ('published', models.BooleanField(default=False, verbose_name='published')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.media', verbose_name='video')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', to='clinics.storycategory')),
            ],
            options={
                'verbose_name': 'story',
                'verbose_name_plural': 'stories',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='title')),
                ('responsibilities', ckeditor.fields.RichTextField(verbose_name='responsibilities')),
                ('requirements', ckeditor.fields.RichTextField(verbose_name='requirements')),
                ('conditions', ckeditor.fields.RichTextField(verbose_name='conditions')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.media')),
            ],
            options={
                'verbose_name': 'vacancy',
                'verbose_name_plural': 'vacancies',
            },
        ),
        migrations.CreateModel(
            name='StoryProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', to='products.product', verbose_name='product')),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='clinics.story')),
            ],
            options={
                'verbose_name': 'story product',
                'verbose_name_plural': 'story products',
                'unique_together': {('story', 'product')},
            },
        ),
    ]
