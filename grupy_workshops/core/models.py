from django.db import models


class Workshops(models.Model):
    workshop = models.CharField("Workshop", max_length=50)
    votos = models.CharField("Votos", max_length=4)
    agendado = models.BooleanField(default=False)
    realizado = models.BooleanField(default=False)
    # local =
    # endereco =
    num_participantes = models.CharField("Número de Participantes", max_length=4)
    # palestrantes =


class Palestrantes(models.Model):
    palestrante = models.CharField("Palestrantes", max_length=100)
    id_telegram = models.CharField("Id Telegram", max_length=20)


class Interessados(models.Model):
    nome = models.CharField("Nome", max_length=100)
    id_telegram = models.CharField("Id Telegram", max_length=20)
    assunto_votado = models.CharField("Assunto Votado", max_length=50)


class Locais(models.Model):
    local = models.CharField("Local", max_length=30)
    endereco = models.CharField("Endereço", max_length=200)
    data = models.DateField("Data do Workshop")
    # workshop =