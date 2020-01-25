# Generated by Django 3.0.2 on 2020-01-22 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Başlıq')),
                ('content', models.CharField(max_length=3000, verbose_name='İçəriyi')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Paylaşım tarixi')),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('post_image', models.FileField(blank=True, null=True, upload_to='', verbose_name='Şəkil əlavə edin')),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Postun Sahibi ')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_id', models.IntegerField()),
                ('comment_author', models.CharField(max_length=100, verbose_name='Müəllif')),
                ('comment_content', models.CharField(max_length=1000, verbose_name='Komment')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='user.Posts', verbose_name='Paylaşım')),
            ],
            options={
                'ordering': ['-comment_date'],
            },
        ),
    ]