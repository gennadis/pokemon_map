import folium
from django.http import HttpResponseNotFound
from django.shortcuts import render

from pokemon_entities.models import Pokemon, PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision"
    "/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832"
    "&fill=transparent"
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for pokemon_entity in PokemonEntity.objects.all():
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            request.build_absolute_uri(pokemon_entity.pokemon.image.url),
        )

    pokemons_on_page = [
        {
            "pokemon_id": pokemon.pk,
            "img_url": pokemon.image.url,
            "title_ru": pokemon.title_ru,
        }
        for pokemon in Pokemon.objects.all()
    ]

    return render(
        request,
        "mainpage.html",
        context={
            "map": folium_map._repr_html_(),
            "pokemons": pokemons_on_page,
        },
    )


def show_pokemon(request, pokemon_id):
    try:
        pokemon = Pokemon.objects.get(pk=pokemon_id)
        pokemon_attributes = {
            "pokemon_id": pokemon.pk,
            "title_ru": pokemon.title_ru,
            "title_en": pokemon.title_en,
            "title_jp": pokemon.title_jp,
            "img_url": request.build_absolute_uri(pokemon.image.url),
            "description": pokemon.description,
        }

    except Pokemon.DoesNotExist:
        return HttpResponseNotFound("<h1>Такой покемон не найден</h1>")

    else:
        folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
        for pokemon_entity in PokemonEntity.objects.filter(pokemon=pokemon):
            add_pokemon(
                folium_map,
                pokemon_entity.lat,
                pokemon_entity.lon,
                request.build_absolute_uri(pokemon_entity.pokemon.image.url),
            )

        return render(
            request,
            "pokemon.html",
            context={"map": folium_map._repr_html_(), "pokemon": pokemon_attributes},
        )
