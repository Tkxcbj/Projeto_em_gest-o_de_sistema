# Generated by Django 4.1.2 on 2022-11-12 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veiculos', '0002_rename_utima_localizacao_veiculo_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='cor',
            field=models.CharField(max_length=10, null=True, verbose_name='Cor do veículo'),
        ),
        migrations.AlterField(
            model_name='veiculo',
            name='foto_carro',
            field=models.ImageField(upload_to='main/carros/%Y/%m/%d/', verbose_name='Imagem do Veículo'),
        ),
        migrations.CreateModel(
            name='VeiculoHistorico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.TimeField(auto_now=True)),
                ('latitude', models.CharField(max_length=20, null=True)),
                ('longitude', models.CharField(max_length=20, null=True)),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veiculos.veiculo')),
            ],
        ),
    ]
