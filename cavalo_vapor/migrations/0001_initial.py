# Generated by Django 3.1.6 on 2021-02-21 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=200)),
                ('cep', models.CharField(max_length=9)),
                ('bairro', models.CharField(max_length=150)),
                ('number', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Caminhao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('potencia', models.SmallIntegerField()),
                ('eixos', models.SmallIntegerField()),
                ('litros', models.SmallIntegerField(blank=True)),
                ('autonomia', models.SmallIntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('cnpj', models.CharField(max_length=18, primary_key=True, serialize=False)),
                ('ano_fundacao', models.CharField(blank=True, max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('uf', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Filial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.adress')),
                ('cnpj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Frete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('avaliacao_empresa', models.SmallIntegerField(default=0)),
                ('tipo_de_carga', models.CharField(max_length=150)),
                ('data_hora_carga', models.DateTimeField()),
                ('carga', models.CharField(max_length=150)),
                ('avaliacao_caminhoneiro', models.SmallIntegerField(default=0)),
                ('valor', models.CharField(max_length=20)),
                ('tipo_reboque', models.TextField()),
                ('status_fretes', models.CharField(max_length=50)),
                ('data_hora_prazo', models.DateTimeField()),
                ('distancia', models.SmallIntegerField()),
                ('data_hora_descarga', models.DateTimeField(blank=True)),
                ('descricao_status', models.TextField()),
                ('peso_incial', models.SmallIntegerField()),
                ('tempo_de_candidato', models.SmallIntegerField(default=168)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.IntegerField()),
                ('genero', models.CharField(blank=True, max_length=1)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('data_nascimento', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Integrante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permissao', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('marca', models.CharField(max_length=150, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField()),
                ('open_close', models.CharField(default=1, max_length=1)),
                ('titulo', models.CharField(max_length=150)),
                ('texto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Carreta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_carreta', models.CharField(max_length=100)),
                ('eixos', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Reboque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_reboque', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soma_avaliacoes', models.IntegerField(default=0)),
                ('foto_capa', models.CharField(blank=True, max_length=200)),
                ('logo', models.CharField(blank=True, max_length=200)),
                ('qtd_avaliacoes', models.IntegerField(default=0)),
                ('descricao', models.TextField(blank=True)),
                ('modo_preferencia', models.CharField(default=0, max_length=1)),
                ('nome', models.CharField(max_length=200)),
                ('senha', models.CharField(max_length=64)),
                ('login', models.CharField(max_length=150, unique=True)),
                ('admin', models.BooleanField(default=False, max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=15)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Sala_favorita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.sala')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='sala',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.usuario'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField()),
                ('texto', models.TextField()),
                ('integrante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.integrante')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.sala')),
            ],
        ),
        migrations.CreateModel(
            name='Notificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField()),
                ('texto', models.TextField()),
                ('titulo', models.CharField(max_length=150)),
                ('cnpj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.estado')),
            ],
        ),
        migrations.AddField(
            model_name='integrante',
            name='sala',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.sala'),
        ),
        migrations.AddField(
            model_name='integrante',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.usuario'),
        ),
        migrations.CreateModel(
            name='Funcionario_Filial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.filial')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.funcionario')),
            ],
        ),
        migrations.AddField(
            model_name='funcionario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.usuario'),
        ),
        migrations.CreateModel(
            name='Frete_Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente_prestador', models.CharField(max_length=40)),
                ('frete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.frete')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='filial',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.usuario'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.usuario'),
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('email', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('email_de_recuperacao', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Destinatarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notificacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.notificacao')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Carreta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso_max', models.SmallIntegerField()),
                ('eixos', models.SmallIntegerField()),
                ('volume_max', models.SmallIntegerField()),
                ('comprimento', models.FloatField(blank=True)),
                ('tipo_de_carreta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.tipo_carreta')),
                ('tipo_de_reboque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.tipo_reboque')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caminhao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.caminhao')),
                ('carreta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.carreta')),
                ('frete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.frete')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Caminhoneiro',
            fields=[
                ('cpf', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('data_nascimento', models.DateField(blank=True)),
                ('genero', models.CharField(blank=True, max_length=1)),
                ('adrees', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.adress')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='caminhao',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.marca'),
        ),
        migrations.AddField(
            model_name='caminhao',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.usuario'),
        ),
        migrations.CreateModel(
            name='Adress_Frete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carga_descarga', models.CharField(max_length=1)),
                ('adress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.adress')),
                ('frete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.frete')),
            ],
        ),
        migrations.AddField(
            model_name='adress',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.estado'),
        ),
        migrations.AddField(
            model_name='adress',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cavalo_vapor.municipio'),
        ),
    ]
