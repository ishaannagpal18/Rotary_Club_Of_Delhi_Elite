# Generated by Django 3.2.7 on 2022-02-26 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0004_contactform_contactlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('video', models.ImageField(upload_to='Upload')),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]