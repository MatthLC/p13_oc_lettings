# Generated by Django 3.0 on 2022-06-10 13:45

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0003_auto_20220610_1542'),
    ]

    state_operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999)])),
                ('street', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(2)])),
                ('zip_code', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99999)])),
                ('country_iso_code', models.CharField(max_length=3, validators=[django.core.validators.MinLengthValidator(3)])),
            ],
            options={
                'db_table' : 'lettings_Address',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Letting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lettings.Address')),
            ],
            options={
                'db_table' : 'lettings_Letting',
            },
            bases=(models.Model,),
        ),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations)
    ]
