# Generated by Django 2.2.7 on 2019-11-27 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usermgmt', '0005_auto_20191127_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rebatereq',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usermgmt.Student'),
        ),
    ]
