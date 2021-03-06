# Generated by Django 2.1.4 on 2019-06-30 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_img', models.ImageField(upload_to='pics')),
                ('banner_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Destinations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('offer', models.BooleanField(default=False)),
                ('date', models.DateTimeField()),
                ('published', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='News_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('heading', models.CharField(max_length=100)),
                ('news_img', models.ImageField(upload_to='pics')),
                ('categories', models.CharField(max_length=100)),
                ('news_desc', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.TextField()),
                ('test_img', models.ImageField(upload_to='pics')),
                ('test_desc', models.TextField()),
            ],
        ),
    ]
