# Generated by Django 3.0.6 on 2020-06-05 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssuranceMaladie', '0002_assurance_archive'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assurance',
            old_name='Tarif',
            new_name='baseRemb',
        ),
        migrations.RenameField(
            model_name='assurance',
            old_name='natureActe',
            new_name='manierExecuter',
        ),
        migrations.AddField(
            model_name='assurance',
            name='prestation',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
