# Generated by Django 4.2.7 on 2023-12-11 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_rename_ref_animal_categoria_ref_tipoproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.FileField(upload_to='productos/img_producto'),
        ),
    ]
