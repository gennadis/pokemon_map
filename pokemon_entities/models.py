from django.db import models


class Pokemon(models.Model):
    title_ru = models.CharField(
        verbose_name="Название на русском",
        max_length=200,
    )
    title_en = models.CharField(
        verbose_name="Название на английском",
        max_length=200,
        blank=True,
    )
    title_jp = models.CharField(
        verbose_name="Название на японском",
        max_length=200,
        blank=True,
    )
    image = models.ImageField(
        verbose_name="Изображение",
        upload_to="pokemons",
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
    )
    evolved_from = models.ForeignKey(
        "self",
        verbose_name="Эволюционировал из",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="next_evolution",
    )

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        verbose_name="Покемон",
        on_delete=models.CASCADE,
        related_name="pokemons",
    )
    lat = models.FloatField(verbose_name="Широта")
    lon = models.FloatField(verbose_name="Долгота")

    appeared_at = models.DateTimeField(
        verbose_name="Время появления", null=True, blank=True
    )
    disappeared_at = models.DateTimeField(
        verbose_name="Время исчезновения", null=True, blank=True
    )

    level = models.IntegerField(verbose_name="Уровень", null=True, blank=True)
    health = models.IntegerField(verbose_name="Здоровье", null=True, blank=True)
    strength = models.IntegerField(verbose_name="Сила", null=True, blank=True)
    defence = models.IntegerField(verbose_name="Защита", null=True, blank=True)
    stamina = models.IntegerField(verbose_name="Выносливость", null=True, blank=True)

    def __str__(self):
        return f"{self.pokemon} @ ({self.lat}, {self.lon})"
