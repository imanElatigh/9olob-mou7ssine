# Generated by Django 4.1.7 on 2024-03-11 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asso', '0005_chatbot'),
    ]

    operations = [
        migrations.AddField(
            model_name='associationuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
