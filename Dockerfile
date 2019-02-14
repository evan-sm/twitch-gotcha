FROM python:3.7-alpine

RUN apk update \
    && apk add --no-cache \
    && mkdir -p /app

WORKDIR /app
COPY ./app/ .
RUN pip install -r requirements.txt
#RUN git clone -b develop --single-branch https://github.com/Twentysix26/Red-DiscordBot.git
#RUN pip install -U https://github.com/Rapptz/discord.py@rewrite#egg=discord.py


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#RUN pip install --no-cache-dir virtualenv

#COPY . .

#CMD ["python3", "/app/app/app.py"]

ENTRYPOINT ["python", "/app/twitch-gotcha.py"]


#ENTRYPOINT ["expect", "/app/redbot.exp"]
#CMD ["python", "/app/app/Red-DiscordBot/launcher.py"]
