# Generated by Django 2.2.2 on 2019-07-05 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('information_about_author', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gmail', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_publication', models.DateTimeField(verbose_name='date published')),
                ('post_text', models.CharField(max_length=1000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_publication', models.DateTimeField(verbose_name='date published')),
                ('text', models.CharField(max_length=500)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.User')),
            ],
        ),
    ]
