FROM python:3-slim-buster

RUN pip install --upgrade pip

ENV USER botx
ENV HOME /home/$USER
ENV BOT $HOME/media-search-bot

RUN useradd -m $USER
RUN mkdir -p $BOT
RUN chown $USER:$USER $BOT
USER $USER
WORKDIR $BOT


COPY requirements.txt requirements.txt
RUN pip install --user --no-cache-dir -r requirements.txt

COPY . .

CMD python3 bot.py
