# Twitch-Gotcha

Catch popular streamers visiting your twitch channel and notifying you via Telegram.

### Prerequisites

Since you need it running 24/7, I recommend using [Supervisord](http://supervisord.org/)

### Installing


```
# git clone https://github.com/wMw9/twitch-gotcha.git
# cd ./twitch-gotcha
```

Rename cfg.py.sample to cfg.py

```
# mv cfg.py.sample cfg.py 
```

Edit cfg.py by putting your own TOKENs and API keys there

Since this bot uses Telegram to notify you, create your own here [t.me/BotFather](https://t.me/BotFather)

Now install required python packages by running

```
# pip install -r requirements.txt
```

Ready, steady, go

```
# python3 twitch-gotcha.py
```
Or you can use Docker
```
# docker-compose up -d --build
```

## Built With

* [Requests](http://docs.python-requests.org/en/master/) — Python HTTP for Humans.
* [Arrow](http://arrow.readthedocs.io/en/latest/) — Better dates and times for Python

## Authors

* **Ivan wmw** — [t.me/wmwofficial](https://t.me/wmwofficial)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
