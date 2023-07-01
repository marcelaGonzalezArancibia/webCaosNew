# Generated by Django 4.2.1 on 2023-06-24 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webCaosNew', '0010_alter_galeria_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='objcarrito',
            fields=[
                ('idobjeto', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_objeto', models.CharField(max_length=60)),
                ('precio', models.IntegerField()),
                ('imagen', models.ImageField(default='fotos/default.png', null=True, upload_to='fotos')),
            ],
        ),
    ]
