from django.db import models


class Workshops(models.Model):
    workshop = models.CharField("Workshop", max_length=50, null=True, blank=True)
    votos = models.CharField("Votos", max_length=4, null=True, blank=True, default='0')
    agendado = models.BooleanField(default=False)
    realizado = models.BooleanField(default=False)
    # local =
    # endereco =
    total_participantes = models.CharField("Total de Participantes",
                                         max_length=4, null=False, blank=True, default='0')
    # palestrantes =

    class Meta:
        # verbose_name = "Workshop"
        verbose_name_plural = "workshops"
        ordering = ['workshop']

    def __str__(self):
        return self.workshop


class Palestrantes(models.Model):
    palestrante = models.CharField("Palestrantes", max_length=100, null=True, blank=True)
    id_telegram = models.CharField("Id Telegram", max_length=20, null=False, blank=True, default='0')

    class Meta:
        verbose_name_plural = "palestrantes"
        ordering = ['palestrante']

    def __str__(self):
        return self.palestrante


class Interessados(models.Model):
    nome = models.CharField("Nome", max_length=100, null=True, blank=True)
    id_telegram = models.CharField("Id Telegram", max_length=20, null=False, blank=True, default='0')
    assunto_votado = models.CharField("Assunto Votado", max_length=50, null=False, blank=True)
    data_votacao = models.DateTimeField("Data da Votação", null=True, auto_now_add=True)

    class Meta:
        verbose_name_plural = "interessados"
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Locais(models.Model):
    local = models.CharField("Local", max_length=30, null=True, blank=True)
    endereco = models.CharField("Endereço", max_length=200, null=False, blank=True)
    data = models.DateField("Data do Workshop", auto_now_add=False)
    hora = models.TimeField("Hora do Workshop", auto_now_add=False)
    # workshop =

    class Meta:
        verbose_name_plural = "locais"
        ordering = ['local']

    def __str__(self):
        return self.local