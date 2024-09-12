# OXYGEN MINER AUTO

Oxygen Miner Telegram Mini App Bot

For README in Bahasa Indonesia: [![en](https://img.shields.io/badge/README-id-red.svg)](https://github.com/dzuhri-auto/oxygen/blob/master/README.id.md)

## Feature

- Auto Collect Food
- Auto Claim Daily Check-in
- Auto Open Box
- Auto Use Item from Box (deactivated by default)
- Auto Claim Combo (using .env)
- Auto Upgrade Boost
- Auto Clear Mission / Tasks
- Auto Play Game (need 1 referral)

## .env Settings

| Name | Description | Default |
| --- | ----------- | --------- |
| API_KEY | Custom API KEY | |
| MAX_FOOD_LVL | Maximum level to auto upgrade food boost | 50 |
| MAX_OXY_LVL | Maximum level to auto upgrade oxy boost | 50 |
| TASK_CODES | Task or mission id | ["okx","tappc_c","tappc_p","oxy-yt","oxy-tg", "join_tw","oxy-chat", "oxy-chat-en", "join_ds", "join_guild", "acki", "vp_pig","vp_qqq"] |
| AUTO_USE_ITEM | Auto use item from box | False |
| RANDOM_PLAY_GAME | Randomize how many to play ufo game | [2, 5]|
| GAME_SCORES | Randomize score for each play ufo game | [80, 100] |
| USE_RANDOM_DELAY_IN_RUN | Activate delay before start the bot | True |
| RANDOM_DELAY_IN_RUN | Randomize delay seconds before start the bot | [1, 15] |
| USE_PROXY_FROM_FILE | For using proxy | False |

## Preparation

Make sure you already install:

- [Python](https://www.python.org/downloads/release/python-31014/) **version 3.10**

## Request API KEY

This script use custom API KEY, The API KEY itself is for rent only

you can chat me, [Irham](https://t.me/irhamdz) to ask how much the rent price !

## Install

Clone to your PC / VPS:

```shell
git clone https://github.com/dzuhri-auto/oxygen.git
```

Go inside to the folder:

```shell
cd oxygen
```

Then use this command for automatic install:

**Windows** :

```shell
windows\install.bat
```

**Mac / Linux / VPS** :

```shell
sudo chmod +x ubuntu/install.sh ubuntu/run.sh ubuntu/update.sh
```

```shell
./ubuntu/install.sh
```

***note : dont forget to edit file `.env` and `profiles.json`***

## Format profiles.json

the `profile.json` need to have this format:

```shell
# 1 account
[
    {
        "session_name": "account-1",
        "tg-id":"<tg-id>",
        "secret": "<secret>",
        "cookie":"<cookie>"
    }
]


# multi account
[
    {
        "session_name": "account-1",
        "tg-id":"<tg-id>",
        "secret": "<secret>",
        "cookie":"<cookie>"
    },
    {
        "session_name": "account-2",
        "tg-id":"<tg-id>",
        "secret": "<secret>",
        "cookie":"<cookie>"
    }
]
```

for `tg-id` , `secret` and `cookie` you can get from:

- Open oxygen miner bot in telegram web chrome
- Open developer console chrome
- Open tab `network`
- Filter `login`
- Check the request and copy `tg-id` , `secret` dan `cookie`.
<img width="1370" alt="Screenshot 2024-09-12 at 04 32 43" src="https://github.com/user-attachments/assets/f8efa9b4-04ae-4697-8206-0980df99a09b">

## Update API KEY

After install we can update using API KEY:

**Windows** :

```shell
$filePath = ".env"
$searchPattern = "^API_KEY="
$replacement = 'API_KEY="YOUR API KEY"'

(Get-Content $filePath) -replace $searchPattern + '.*', $replacement | Set-Content $filePath
```

**Mac / Linux / VPS** :

```shell
sed -i~ '/^API_KEY=/s/=.*/="YOUR API KEY"/' .env

# example if your API KEY = "aisjiqiqssq"
# sed -i~ '/^API_KEY=/s/=.*/="aisjiqiqssq"/' .env
```

## Start Bot

For run the bot:

**Windows** :

```shell
windows\run.bat
```

**Mac / Linux / VPS** :

```shell
./ubuntu/run.sh
```

## Update Bot

For update the bot:

**Windows** :

```shell
windows\update.bat
```

**Mac / Linux / VPS** :

```shell
./ubuntu/update.sh
```
