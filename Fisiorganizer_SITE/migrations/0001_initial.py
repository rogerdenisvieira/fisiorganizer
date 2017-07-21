# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-20 14:25
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
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('surname', models.CharField(blank=True, max_length=150)),
                ('address', models.CharField(blank=True, max_length=150)),
                ('city', models.CharField(max_length=25)),
                ('cellphone', models.PositiveIntegerField()),
                ('CEP', models.PositiveIntegerField(blank=True, null=True)),
                ('age', models.IntegerField()),
                ('details', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('reference', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseEquipment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fisiorganizer_SITE.Equipment')),
                ('id_exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fisiorganizer_SITE.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='ExerciseFocus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fisiorganizer_SITE.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Focus',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Modality',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('id_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fisiorganizer_SITE.Customer')),
                ('id_instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_modality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fisiorganizer_SITE.Modality')),
            ],
        ),
        migrations.CreateModel(
            name='SessionExercise',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('alias', models.CharField(max_length=150)),
                ('id_exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fisiorganizer_SITE.Exercise')),
                ('id_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fisiorganizer_SITE.Session')),
            ],
        ),
        migrations.CreateModel(
            name='UserExtra',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('attempts', models.PositiveIntegerField(default=0)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='exercisefocus',
            name='id_focus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fisiorganizer_SITE.Focus'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='id_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fisiorganizer_SITE.Level'),
        ),
    ]