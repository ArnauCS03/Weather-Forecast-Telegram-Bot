# Weather Forecast Telegram Bot

This repository showcases my project on creating a Telegram bot focused on weather forecasting, powered by the OpenWeather API using Python. It serves as an excellent learning opportunity for understanding API interactions and building a practical Telegram bot.<br>

---
## Overview

- OpenWeather API Integration: The bot uses the [OpenWeather API](https://openweathermap.org/api) to provide real-time weather information for different cities.<br><br>

- Interactive Telegram Experience: Users can receive weather forecasts for predefined cities or input a specific city name directly.<br><br>


# Prerequisites

Before running the bot, ensure you have the following:

- OpenWeather API Key: Obtain your API key from OpenWeather and save it in a file named *OWM_key.txt*<br><br>

- Telegram Bot Token: Create a Telegram bot and get your bot token. Save the token in a file named *token.txt*

Note: Make sure to keep both files (OWM_key.txt and token.txt) private and never share them publicly.
In this project i created the files empty, so you can try it locally.<br><br>

## Running the Bot

To run the bot, follow these simple steps:

Clone the repository:

```
git clone [https://github.com/your-username/WeatherForecastBot.git](https://github.com/ArnauCS03/Weather-Forecast-Telegram-Bot.git)
cd Weather-Forecast-Telegram-Bot
``` 

Install the required Python packages:

```
pip3 install python-telegram-bot requests
```

Place your OpenWeather API key in *OWM_key.txt* and your Telegram bot token in *token.txt*.

Run the bot script:

```
python3 OpenWeather.py
```

## Usage

Once the bot is running, you can interact with it on Telegram:

- Start the bot by sending /start to get a list of predefined cities and weather information.

- Type the name of a city to get the current weather conditions directly or clik one of the cities predefined.


## Learning Resources

To learn the basics of creating your first simple Telegram bot, check out this tutorial:  [Lliçons Jutge Telegram](https://lliçons.jutge.org/python/telegram.html)

## Bot Link

You can access the bot on Telegram by following this link: [PrevisioTempsBot](https://t.me/PrevisioTempsBot). Please note that it might not respond since the Python script is not currently running.

Feel free to explore the code, learn from it, and customize it to suit your needs. <br><br>

---
## Screenshots
<br><br>
![Screenshot from 2024-02-11 16-04-53](https://github.com/ArnauCS03/Weather-Forecast-Telegram-Bot/assets/95536223/e2a898cd-ca7d-45b2-8fb6-08d729b4aeec)<br><br>

![Screenshot from 2024-02-11 16-25-23](https://github.com/ArnauCS03/Weather-Forecast-Telegram-Bot/assets/95536223/ca4d80da-9f1b-484f-90b0-890c2b0009d8)
<br><br>


