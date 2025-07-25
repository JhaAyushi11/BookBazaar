# Generated by Django 4.0 on 2023-09-19 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0006_auto_20200812_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='', upload_to='media/profile_pics'),
        ),
        migrations.AlterField(
            model_name='book',
            name='stream',
            field=models.CharField(choices=[('Medical', 'Medical'), ('Humanities', 'Humanities'), ('Commerce', 'Commerce'), ('Engineering', 'Engineering')], default='Engineering', max_length=15),
        ),
    ]
