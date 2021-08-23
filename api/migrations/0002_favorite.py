# Generated by Django 3.2.5 on 2021-08-19 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='favorite_task', to='api.task')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='profile', to='api.profile')),
            ],
        ),
    ]
