# Generated by Django 4.2.2 on 2023-09-16 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0002_alter_proveedor_email_comprasenc_comprasdet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comprasenc',
            old_name='Proveedor',
            new_name='proveedor',
        ),
        migrations.AlterField(
            model_name='comprasenc',
            name='fecha_factura',
            field=models.DateField(blank=True, null=True),
        ),
    ]
