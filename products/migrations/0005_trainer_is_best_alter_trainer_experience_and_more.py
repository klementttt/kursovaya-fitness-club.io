# Generated by Django 5.0.4 on 2024-06-28 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_trainer_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='is_best',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='experience',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='trainers/'),
        ),
    ]
