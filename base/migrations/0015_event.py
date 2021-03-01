# Generated by Django 3.0.8 on 2021-02-21 10:44

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20210205_0426'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200)),
                ('sub_headline', models.CharField(blank=True, max_length=200, null=True)),
                ('thumbnail', models.ImageField(blank=True, default='/images/placeholder.png', null=True, upload_to='images')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('createdp', models.DateTimeField(auto_now_add=True, null=True)),
                ('tags', models.ManyToManyField(blank=True, null=True, to='base.Tag')),
            ],
        ),
    ]