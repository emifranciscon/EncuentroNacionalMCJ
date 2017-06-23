# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-06-15 01:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diocesis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cupo', models.PositiveIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FichaMedica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asma', models.BooleanField(default=False)),
                ('enfisema', models.BooleanField(default=False)),
                ('broquitis_cronica', models.BooleanField(default=False)),
                ('alergias', models.CharField(blank=True, max_length=500, null=True)),
                ('otras_respiratorias', models.CharField(blank=True, max_length=500, null=True)),
                ('hipertension', models.BooleanField(default=False)),
                ('hipotension', models.BooleanField(default=False)),
                ('infarto_cardiaco', models.BooleanField(default=False)),
                ('disritmia_cardiaca', models.BooleanField(default=False)),
                ('malformacion_corazon', models.BooleanField(default=False)),
                ('otras_circulatorias', models.CharField(blank=True, max_length=500, null=True)),
                ('dolor_ciatico', models.BooleanField(default=False)),
                ('escoliosis', models.BooleanField(default=False)),
                ('miastenia', models.BooleanField(default=False)),
                ('otras_musculoesque', models.CharField(blank=True, max_length=500, null=True)),
                ('diabetes', models.BooleanField(default=False)),
                ('hipertiroidismo', models.BooleanField(default=False)),
                ('otras_hormonales', models.CharField(blank=True, max_length=500, null=True)),
                ('medicacion_actual', models.BooleanField(default=False)),
                ('comprimidos', models.CharField(blank=True, max_length=500, null=True)),
                ('inyectables', models.CharField(blank=True, max_length=500, null=True)),
                ('dificultad_leer', models.BooleanField(default=False)),
                ('vision_doble', models.BooleanField(default=False)),
                ('dificultad_colores', models.BooleanField(default=False)),
                ('dificultad_colores_desc', models.CharField(blank=True, max_length=500, null=True)),
                ('dificultad_oir', models.BooleanField(default=False)),
                ('epilepsia', models.BooleanField(default=False)),
                ('derrame', models.BooleanField(default=False)),
                ('derrame_desc', models.CharField(blank=True, max_length=500, null=True)),
                ('jaquecas', models.BooleanField(default=False)),
                ('otras_nerviosas', models.CharField(blank=True, max_length=500, null=True)),
                ('vertigo', models.BooleanField(default=False)),
                ('claustrofobia', models.BooleanField(default=False)),
                ('aragnofobia', models.BooleanField(default=False)),
                ('otras_enfermedades', models.CharField(blank=True, max_length=500, null=True)),
                ('fuma', models.BooleanField(default=False)),
                ('nadar', models.BooleanField(default=False)),
                ('peso', models.CharField(blank=True, max_length=100, null=True)),
                ('altura', models.CharField(blank=True, max_length=100, null=True)),
                ('grupo_sanguineo', models.CharField(blank=True, max_length=50, null=True)),
                ('ser_att_medica', models.CharField(blank=True, max_length=500, null=True)),
                ('medico_cabecera', models.CharField(blank=True, max_length=500, null=True)),
                ('hospital_derivacion', models.CharField(blank=True, max_length=500, null=True)),
                ('aclaracion', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('num_doc', models.PositiveIntegerField(unique=True)),
                ('email_personal', models.EmailField(max_length=254)),
                ('tel_emergencia', models.CharField(max_length=100)),
                ('tel_personal', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('talle', models.CharField(blank=True, choices=[('NO', 'NO'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], default='NO', max_length=2, null=True)),
                ('descripcion_dieta', models.CharField(blank=True, max_length=500, null=True)),
                ('num_eslabon', models.PositiveIntegerField()),
                ('fecha_eslabon', models.DateField()),
                ('email_contacto', models.EmailField(max_length=254)),
                ('pago_retiro', models.BooleanField(default=False)),
                ('pago_remera', models.BooleanField(default=False)),
                ('descripcion_familia', models.CharField(blank=True, max_length=500, null=True)),
                ('descripcion_registro', models.CharField(blank=True, max_length=500, null=True)),
                ('diocesis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.Diocesis')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.Estado')),
                ('medical_record', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='person.FichaMedica')),
            ],
        ),
        migrations.CreateModel(
            name='Responsable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('diocesis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.Diocesis')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
