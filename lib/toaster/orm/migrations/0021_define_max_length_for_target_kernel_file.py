# -*- coding: utf-8 -*-
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0020_models_bigautofield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='targetkernelfile',
            name='file_name', 
            field=models.CharField(max_length=1024)
        ),
        migrations.AlterField(
            model_name='targetsdkfile',
            name='file_name', 
            field=models.CharField(max_length=1024)
        ),
    ]
