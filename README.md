## [Media Search bot](https://github.com/Mahesh0253/Media-Search-bot)

* Index channel files for inline search.
* When you going to post file on telegram channel this bot will save that in database, So you and your subscribers can easily search that in inline mode.
* This bot supports document, video and audio file formats with caption.

### Installation

#### Easy Way
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

#### Hard Way

```sh
python3 -m venv env
. ./env/bin/activate
pip install -r requirements.txt
# <Create info.py with variables as given below>
python bot.py
```
Check `sample_info.py` before editing `info.py` file

#### Variables

##### Required Variables
* `BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.

* `API_ID`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `API_HASH`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `CHANNELS`: Username or id of channel. Separate multiple channels by space
* `ADMINS`: Username or id of Admin. Separate multiple Admins by space
* `DATABASE_URI`: [mongoDB](https://www.mongodb.com) URI. Get this value from [mongoDB](https://www.mongodb.com). For more help watch this [video](https://youtu.be/VQnmcBnguPY)
* `DATABASE_NAME`: Name of the database in [mongoDB](https://www.mongodb.com). For more help watch this [video](https://youtu.be/VQnmcBnguPY)

##### Optional Variables
* `COLLECTION_NAME`: Name of the collections. Defaults to Telegram_files. If you going to use same database, then use different collection name for each bot
* `MAX_RESULTS`: Maximum limit for inline search results
* `CACHE_TIME`: The maximum amount of time in seconds that the result of the inline query may be cached on the server

### How to use?
* First add this bot in channel as a Admin
* Then whenever you post file, bot will save that in database, So you can easily search whenever you want.

### Admin commands
```
channel - Get basic infomation about channels
total - Show total of saved files
delete - Delete file from database
logger - Get log file
```
### Contributions
Contributions are welcome.

### Thanks to [Pyrogram](https://github.com/pyrogram/pyrogram)

### License
Code released under [The GNU General Public License](LICENSE).
