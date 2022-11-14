# Generated by Django 4.1.3 on 2022-11-14 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0002_vagas_email_alter_vagas_empresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('prioridade', models.CharField(choices=[('B', 'Baixa'), ('A', 'Alta'), ('U', 'Urgente')], max_length=1)),
                ('data', models.DateField()),
                ('realizada', models.BooleanField(default=False)),
                ('vaga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.vagas')),
            ],
        ),
    ]