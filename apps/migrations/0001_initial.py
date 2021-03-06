# Generated by Django 2.0.7 on 2018-07-11 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('singer_name', models.CharField(max_length=50)),
                ('goldSong', models.CharField(blank=True, max_length=50)),
                ('silverSong', models.CharField(blank=True, max_length=50)),
                ('bronzeSong', models.CharField(blank=True, max_length=50)),
                ('hitokoto', models.CharField(blank=True, max_length=50)),
                ('sore', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=50)),
                ('hitokoto', models.CharField(blank=True, max_length=50)),
                ('sore', models.IntegerField(default=0)),
                ('singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Singer')),
            ],
        ),
    ]
