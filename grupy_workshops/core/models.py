from django.db import models


class Workshops(models.Model):
    workshop = models.CharField("Workshop", max_length=50)
    votos = models.PositiveSmallIntegerField("Votos", null=True, blank=True)
    agendado = models.BooleanField(default=False)
    realizado = models.BooleanField(default=False)
    palestrante = models.OneToOneField('Palestrantes', null=True, blank=True,
                                        on_delete=models.CASCADE, related_name="tutor")
    local = models.OneToOneField("Locais", null=True, blank=True, on_delete=models.CASCADE,
                                 related_name="locwork")
    endereco = models.OneToOneField("Locais", null=True, blank=True, on_delete=models.CASCADE,
                                    related_name="endwork")
    data = models.OneToOneField("Locais", null=True, blank=True, on_delete=models.CASCADE,
                                related_name="datawork")
    hora = models.OneToOneField("Locais", null=True, blank=True, on_delete=models.CASCADE,
                                related_name="horawork")
    total_participantes = models.PositiveSmallIntegerField("Total de Participantes",
                                           null=True, blank=True)

    class Meta:
        verbose_name = "workshop"
        verbose_name_plural = "workshops"
        ordering = ['workshop']

        db_table = "workshops"

    def __str__(self):
        return self.workshop


class Palestrantes(models.Model):
    palestrante = models.CharField("Palestrantes", max_length=100)
    id_telegram = models.PositiveIntegerField("Id Telegram", blank=True, null=True)

    class Meta:
        verbose_name = "palestrante"
        verbose_name_plural = "palestrantes"
        ordering = ['palestrante']

        db_table = "palestrantes"

    def __str__(self):
        return self.palestrante


class Interessados(models.Model):
    nome = models.CharField("Nome", max_length=100)
    id_telegram = models.PositiveIntegerField("Id Telegram")
    assunto_votado = models.CharField("Assunto Votado", max_length=50)
    data_votacao = models.DateTimeField("Data da Votação", auto_now_add=True)

    class Meta:
        verbose_name = "interessado"
        verbose_name_plural = "interessados"
        ordering = ['nome']

        db_table = "interessados"

    def __str__(self):
        return self.nome


class Locais(models.Model):
    local = models.CharField("Local", max_length=30, null=True, blank=True, default="A definir")
    endereco = models.CharField("Endereço", max_length=200, null=True, blank=True)
    nome_contato = models.CharField("Nome do Contato", max_length=50, null=True, blank=True)
    dados_contato = models.CharField("Dados do Contato", max_length=100, null=True, blank=True)
    data = models.DateField("Data do Workshop", auto_now_add=False, blank=True, null=True)
    hora = models.TimeField("Hora do Workshop", auto_now_add=False, blank=True, null=True)
    # workshop =

    class Meta:
        verbose_name = "local"
        verbose_name_plural = "locais"
        ordering = ['local']

        db_table = "locais"

    def __str__(self):
        return self.local


class Interactions(models.Model):
    input = models.CharField(max_length=30)
    script = models.TextField()
    output = models.TextField()

    class Meta:
        verbose_name = "interação"
        verbose_name_plural = "interações"
        ordering = ['input']

        db_table = "interactions"

    def __str__(self):
        return self.input
