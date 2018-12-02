# Generated by Django 2.1.3 on 2018-12-02 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GameFinder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GameFinder.User')),
            ],
        ),
    ]