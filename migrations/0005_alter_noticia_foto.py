# Generated by Django 4.2 on 2023-05-19 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webCaosNew', '0004_alter_noticia_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='foto',
            field=models.ImageField(default='media/fotos/defaut.png', null=True, upload_to='media/fotos'),
        ),
    ]
