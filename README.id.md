# OXYGEN MINER AUTO

Oxygen Miner Telegram Mini App Bot

For README in English: [![en](https://img.shields.io/badge/README-en-red.svg)](https://github.com/dzuhri-auto/oxygen/blob/master/README.md)

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

## Persiapan

Pastikan kamu sudah install:

- [Python](https://www.python.org/downloads/release/python-31014/) **version 3.10**

## Request API KEY

Script ini butuh custom API KEY , API KEY nya cuma disewakan only.

Chat [Irham](https://t.me/irhamdz) "bang mau sewa api key", buat harga sewa nya !

## Install

git clone ke pc / vps kamu:

```shell
git clone https://github.com/dzuhri-auto/oxygen.git
```

Masuk ke folder nya

```shell
cd oxygen
```

Lalu bisa pake command dibawah untuk otomatis install:

**Windows** :

```shell
windows\install.bat
```

**Mac / Linux / VPS** :

```shell
sudo chmod +x ubuntu/install.sh ubuntu/run.sh ubuntu/update.sh
```

```shell
source ./ubuntu/install.sh
```

***note : jangan lupa di isi file `.env` dan `profiles.json` nya***

## Format profiles.json

profile.json harus isi seperti ini

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

untuk `tg-id` , `secret` dan `cookie` kamu bisa dapet dari:

- Buka oxygen miner bot in telegram web chrome
- Buka developer console chrome
- Buka tab `network`
- filter `login`
- Liat request nya copy `tg-id` , `secret` dan `cookie`.
<img width="1370" alt="Screenshot 2024-09-12 at 04 32 43" src="https://github.com/user-attachments/assets/f8efa9b4-04ae-4697-8206-0980df99a09b">


## Update API KEY

Setelah install lalu kita update API KEY kita:

**Windows** :

```shell
$filePath = ".env"
$searchPattern = "^API_KEY="
$replacement = 'API_KEY="GANTI PAKE API KEY KAMU"'

(Get-Content $filePath) -replace $searchPattern + '.*', $replacement | Set-Content $filePath
```

**Mac / Linux / VPS** :

```shell
sed -i~ '/^API_KEY=/s/=.*/="GANTI PAKE API KEY KAMU"/' .env

# contoh misalkan API KEY kamu "aisjiqiqssq"
# sed -i~ '/^API_KEY=/s/=.*/="aisjiqiqssq"/' .env
```

## Start Bot

Untuk menjalankan bot bisa pake command dibawah ini:

**Windows** :

```shell
windows\run.bat
```

**Mac / Linux / VPS** :

```shell
./ubuntu/run.sh
```

## Update Bot

Untuk update bot bisa pake command dibawah ini:

**Windows** :

```shell
windows\update.bat
```

**Mac / Linux / VPS** :

```shell
./ubuntu/update.sh
```
