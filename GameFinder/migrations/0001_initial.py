# Generated by Django 2.1.3 on 2018-12-02 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('FirstName', models.CharField(help_text='Enter First Name', max_length=16)),
                ('LastName', models.CharField(help_text='Enter Last Name', max_length=16)),
                ('last_active', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]