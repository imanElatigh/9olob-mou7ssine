# Generated by Django 4.1.7 on 2024-03-11 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asso', '0004_post_delete_userassiocitionprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chatbot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('response', models.TextField()),
            ],
        ),
    ]