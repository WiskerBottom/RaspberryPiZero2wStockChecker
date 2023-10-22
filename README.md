# RaspberryPiZero2wStockChecker
A selenium script to check whether Raspberry Pi Zero 2w is in stock on a short list of websites. It will email you with a link to where you can buy the Pi if it is in stock.

Where it checks:
Vilros
Chicagodist
Pishop
Canakit
Adafruit

You will need to replace YOUR_BOT_EMAIL_HERE@GMAIL.COM, YOUR_BOT_PASSWORD and WHO_YOU_WANT_TO_RECIEVE_NOTIFICATIONS@GMAIL.COM with your own info.
This script does not run schedule itself, it simply checks if there is any stock when run and then stops. I recommend using crontab to automatically run it every hour.
