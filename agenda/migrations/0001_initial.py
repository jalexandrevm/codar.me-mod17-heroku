# Generated by Django 4.0.3 on 2022-03-25 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_horario', models.DateField()),
                ('nome_cliente', models.CharField(max_length=100)),
                ('email_cliente', models.EmailField(max_length=254)),
                ('telefone_cliente', models.CharField(max_length=100)),
            ],
        ),
    ]
