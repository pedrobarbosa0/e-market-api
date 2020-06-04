# Generated by Django 3.0.6 on 2020-06-03 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("usuario", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Carrinho",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="carrinhos", to="usuario.Cliente"
                    ),
                ),
                (
                    "estabelecimento",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="carrinhos",
                        to="usuario.Estabelecimento",
                    ),
                ),
            ],
        ),
    ]
