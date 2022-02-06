# Pokemon map

![screenshot](media/Screenshot.png)

## Предметная область
Сайт для помощи по игре [Pokemon GO](https://www.pokemongo.com/en-us/). Это игра про ловлю [покемонов](https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%BA%D0%B5%D0%BC%D0%BE%D0%BD).

Суть игры в том, что на карте периодически появляются покемоны, на определённый промежуток времени. Каждый игрок может поймать себе покемона, и пополнить свою личную коллекцию.

На карте может быть сразу несколько особей одного и того же покемона: например, 3 Бульбазавра. Каждую особь могут поймать сразу несколько игроков. Если игрок поймал себе особь покемона, она исчезает для него, но остаётся для других.

В игре есть механика эволюции. Покемон одного вида может "эволюционировать" в другого. Так, например, Бульбазавр превращается в Ивизавра, а тот превращается в Венузавра.


## Setup
1. Clone project
```bash
git clone https://github.com/gennadis/pokemon_map.git
cd pokemon_map
```

2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install requirements
```bash
pip install -r requirements.txt
```

4. Create database
```bash
python manage.py migrate
```

5. Create Django superuser
```bash
python manage.py createsuperuser
```

6. Import test `fixtures` into database
```bash
python manage.py loaddata data.json
```

7. Run local server
```bash
python manage.py runserver
```

8. Open `Pokemon map` at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

9. Open `admin` panel if needed at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)