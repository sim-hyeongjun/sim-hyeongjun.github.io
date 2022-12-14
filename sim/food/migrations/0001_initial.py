# Generated by Django 4.0.7 on 2022-09-28 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import food.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='zip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='One Line Description')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='OWNER')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='TITLE')),
                ('description', models.TextField(blank=True, verbose_name='food describe')),
                ('image', food.fields.ThumbnailImageField(upload_to='food/%Y%m')),
                ('upload_dt', models.DateField(auto_now_add=True, verbose_name='Upload Date')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='OWNER')),
                ('zip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.zip')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]