# Generated by Django 3.2.18 on 2023-04-04 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(help_text='Specify a type of data.', max_length=255, unique=True, verbose_name='data type')),
            ],
            options={
                'verbose_name': 'data type',
                'verbose_name_plural': 'data types',
                'db_table': 'laboratory_data_type',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the manufacturer.', max_length=255, unique=True, verbose_name='name')),
                ('location', models.CharField(help_text='Location of the manufacturer. E.g. country, city etc.', max_length=255, verbose_name='location')),
            ],
            options={
                'verbose_name': 'manufacturer',
                'verbose_name_plural': 'manufacturers',
                'db_table': 'laboratory_manufacturer',
            },
        ),
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the laboratory or collection of instruments.', max_length=255, verbose_name='name')),
                ('description', models.TextField(help_text='A short description of the laboratory. Try to include information such as the purpose of the laboratory, what data does it collect, where it is located, etc.', verbose_name='description')),
                ('contact_name', models.CharField(help_text='Full name of the laboratory point-of-contact.', max_length=255, verbose_name='contact name')),
                ('contact_email', models.EmailField(blank=True, help_text='A point-of-contact email to get in touch with the laboratory.', max_length=254, null=True, verbose_name='contact email')),
                ('outputs', models.ManyToManyField(help_text='Types of data that this laboratory outputs.', to='laboratory.DataType', verbose_name='output types')),
            ],
            options={
                'verbose_name': 'laboratory',
                'verbose_name_plural': 'laboratories',
                'db_table': 'laboratory_laboratory',
            },
        ),
        migrations.CreateModel(
            name='InstrumentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(help_text='The type of instrument.', max_length=255, verbose_name='instrument type')),
                ('model', models.CharField(help_text='Specific model name of this instrument type.', max_length=255, verbose_name='instrument model')),
                ('year_manufactured', models.PositiveSmallIntegerField(help_text='Year of manufacture of the instrument.', verbose_name='year manufactured')),
                ('description', models.TextField(help_text='Provide a short description of this particular instrument type.', verbose_name='description')),
                ('collects', models.ManyToManyField(help_text='Types of data that this instrument collects.', to='laboratory.DataType', verbose_name='collects')),
                ('manufacturer', models.ForeignKey(blank=True, help_text='The manufacturer of the instrument.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='instruments', to='laboratory.manufacturer', verbose_name='manufacturer')),
            ],
            options={
                'verbose_name': 'instrument type',
                'verbose_name_plural': 'instrument types',
                'db_table': 'laboratory_instrument_type',
                'unique_together': {('manufacturer', 'model', 'year_manufactured')},
            },
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_id', models.CharField(help_text='Unique internal ID of the instrument used by the laboratory. Required to distinguish multiple instruments of the same type in a single laboratory.', max_length=255, verbose_name='internal ID')),
                ('laboratory', models.ForeignKey(blank=True, help_text='The laboratory to which the instrument belongs.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='instruments', to='laboratory.laboratory', verbose_name='laboratory')),
                ('type', models.ForeignKey(help_text='The laboratory to which the instrument belongs.', on_delete=django.db.models.deletion.PROTECT, related_name='instruments', to='laboratory.instrumenttype', verbose_name='instrument type')),
            ],
            options={
                'verbose_name': 'instrument',
                'verbose_name_plural': 'instruments',
                'db_table': 'laboratory_instrument',
                'default_related_name': 'instruments',
                'unique_together': {('laboratory', 'type', 'internal_id')},
            },
        ),
    ]