# Generated by Django 4.2.7 on 2024-01-26 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empolyees',
            name='image',
            field=models.ImageField(null=True, upload_to='image'),
        ),
    ]