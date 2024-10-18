# Generated by Django 5.1.2 on 2024-10-18 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postagens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('conteudo', models.TextField()),
                ('data_publicacao', models.DateTimeField(auto_now_add=True)),
                ('autor', models.CharField(max_length=50)),
            ],
        ),
    ]