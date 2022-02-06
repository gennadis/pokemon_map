from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.CharField(
        verbose_name="Название на русском",
        max_length=200,
    )
    title_en = models.CharField(
        verbose_name="Название на английском",
        max_length=200,
        null=True,
        blank=True,
    )
    title_jp = models.CharField(
        verbose_name="Название на японском",
        max_length=200,
        null=True,
        blank=True,
    )
    image = models.ImageField(
        verbose_name="Изображение",
        upload_to="pokemons",
        blank=True,
        null=True,
    )
    description = models.TextField(
        verbose_name="Описание",
        null=True,
        blank=True,
    )
    evolved_from = models.ForeignKey(
        "self",
        verbose_name="Эволюционировал из",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="evolutions",
    )

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        verbose_name="Покемон",
        on_delete=models.CASCADE,
    )
    lat = models.FloatField(verbose_name="Широта")
    lon = models.FloatField(verbose_name="Долгота")
    appeared_at = models.DateTimeField(verbose_name="Время появления")
    disappeared_at = models.DateTimeField(verbose_name="Время исчезновения")
    level = models.IntegerField(verbose_name="Уровень")
    health = models.IntegerField(verbose_name="Здоровье")
    strength = models.IntegerField(verbose_name="Сила")
    defence = models.IntegerField(verbose_name="Защита")
    stamina = models.IntegerField(verbose_name="Выносливость")

    def __str__(self):
        return f"{self.pokemon} @ ({self.lat}, {self.lon})"
