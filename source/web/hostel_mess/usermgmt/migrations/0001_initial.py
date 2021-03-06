# Generated by Django 2.2.7 on 2019-11-26 22:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('mealType', models.CharField(choices=[('B', 'breakfast'), ('L', 'lunch'), ('S', 'snacks'), ('D', 'dinner')], max_length=1, primary_key=True, serialize=False)),
                ('price', models.IntegerField(choices=[(30, 'breakfast'), (60, 'lunch'), (30, 'snacks'), (60, 'dinner')], default=60)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cardNo', models.TextField(blank=True, max_length=15)),
                ('phoneNo', models.IntegerField(blank=True)),
                ('foodType', models.CharField(choices=[('v', 'veg'), ('nv', 'nonveg'), ('j', 'jain')], default='v', max_length=2)),
                ('roomNo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='rebateReq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromDate', models.DateField(auto_now_add=True, help_text='format : DDMMYYYY', max_length=10, null=True)),
                ('toDate', models.DateField(auto_now_add=True, help_text='format : DDMMYYYY', max_length=10, null=True)),
                ('status', models.CharField(choices=[('Y', 'yes'), ('N', 'no'), ('W', 'wait')], max_length=1)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usermgmt.Student')),
            ],
        ),
        migrations.CreateModel(
            name='overheadReq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, help_text='format : DDMMYYYY', max_length=10, null=True)),
                ('status', models.CharField(choices=[('Y', 'yes'), ('N', 'no'), ('W', 'wait')], max_length=1)),
                ('count', models.IntegerField(default=1)),
                ('mealType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usermgmt.Meal')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usermgmt.Student')),
            ],
        ),
    ]
