# Generated by Django 4.2.4 on 2023-09-04 03:01

import app_cad_usuarios.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Usuario",
            fields=[
                ("id_usuario", models.AutoField(primary_key=True, serialize=False)),
                ("nome", models.CharField(max_length=100, verbose_name="Nome")),
                (
                    "idade",
                    models.PositiveIntegerField(
                        help_text="Informe a idade com no máximo 3 digitos.",
                        validators=[app_cad_usuarios.models.validacao_max_digits],
                        verbose_name="Idade",
                    ),
                ),
                ("email", models.EmailField(max_length=100, verbose_name="Email")),
                ("telefone", models.CharField(max_length=13, verbose_name="Telefone")),
                (
                    "data_cadastro",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Data do Cadastro"
                    ),
                ),
            ],
            options={
                "db_table": "Usuario",
            },
        ),
    ]
