[![@CulturalCodeBot](https://img.shields.io/badge/Telegram-%40CulturalCodeBot-blue?style=flat-square)](https://t.me/CulturalCodeBot)
[![MIT License](https://img.shields.io/github/license/ratery/cultural-code-bot?style=flat-square)](https://github.com/Ratery/cultural-code-bot/blob/main/LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/ratery/cultural-code-bot?style=flat-square)](https://github.com/Ratery/cultural-code-bot/commits)

# Cultural code bot
A simple Telegram bot for lyceum project.
Uses asynchronous [aiogram](https://github.com/aiogram/aiogram) framework. <br>
This bot is intended to work only in DMs.

## Features
- Easy to use navigation menu with buttons
- `/quiz` command to pass the test of knowledge of the etiquette rules
- Menu to view information about the basic etiquette rules by topics

## Technologies
- [aiogram](https://github.com/aiogram/aiogram) — interaction with Telegram Bot API
- [cachetools](https://cachetools.readthedocs.io/en/stable) — implementation of throttling to prevent flooding

## Installation instructions
**Python 3.8 or higher is required**

1. Clone the repository:
```bash
$ git clone https://github.com/Ratery/cultural-code-bot
$ cd cultural-code-bot
```

2. Install dependencies:
```bash
$ pip install -r requirements.txt
```

3. Create and set up the `.env` file:
```env
BOT_TOKEN = <YOUR_TOKEN>
```

4. Run the bot:
```bash
$ python bot.py
```

**Note:** We do not provide support for self-hosting.

## License
MIT — see [LICENSE](https://github.com/Ratery/cultural-code-bot/blob/main/LICENSE) file for details.