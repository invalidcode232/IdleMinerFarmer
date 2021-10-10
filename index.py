from core.discord import Discord
from core.autominer import Autominer
import threading
import json

print("               __          _____                                   \r\n_____   __ ___/  |_  _____/ ____\\____ _______  _____   ___________ \r\n\\__  \\ |  |  \\   __\\/  _ \\   __\\\\__  \\\\_  __ \\/     \\_/ __ \\_  __ \\\r\n / __ \\|  |  /|  | (  <_> )  |   / __ \\|  | \\/  Y Y  \\  ___/|  | \\/\r\n(____  /____/ |__|  \\____/|__|  (____  /__|  |__|_|  /\\___  >__|   \r\n     \\/                              \\/            \\/     \\/      ")
print("\nMade with <3 by invalidcode#7810")

with open("config/config.json", "r") as json_data:
    config = json.load(json_data)

    client = Discord(config['token'])
    autominer = Autominer(client, config['channel_id'])

    # Auto-sell
    # You must enable auto-sell in order for auto-upgrade and auto-rebirth to work
    threading.Thread(target=autominer.auto_sell, kwargs={
        'randomization': config['auto_sell']['randomization'],
        'base': config['auto_sell']['base'],
        'auto_upgrade': config['auto_upgrade']['enabled'],
        'auto_rebirth': config['auto_rebirth']['enabled'],
        'upgrade_after': config['auto_upgrade']['upgrade_after'],
        'rebirth_after': config['auto_rebirth']['rebirth_after']
    }).start()

    # Auto-fish
    threading.Thread(target=autominer.auto_fish, kwargs={
        'randomization': config['auto_fish']['randomization'],
        'base': config['auto_fish']['base'],
    }).start()

    # Auto-hunt
    threading.Thread(target=autominer.auto_hunt, kwargs={
        'randomization': config['auto_hunt']['randomization'],
        'base': config['auto_hunt']['base'],
    }).start()

    # Auto-quiz
    threading.Thread(target=autominer.auto_quiz, kwargs={
        'randomization': config['auto_quiz']['randomization'],
        'base': config['auto_quiz']['base'],
    }).start()

    # Auto-hourly
    threading.Thread(target=autominer.auto_hourly, kwargs={
        'randomization': config['auto_hourly']['randomization'],
        'base': config['auto_hourly']['base'],
    }).start()
