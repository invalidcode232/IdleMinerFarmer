import time
from random import randrange

ANSWERS = ["A", "B", "C", "D"]


class Autominer:
    def __init__(self, client, channel, dm_id):
        self.client = client
        self.channel = channel
        self.dm_id = dm_id

    def captcha_check(self):
        messages = self.client.get_messages(self.dm_id, limit=1)

        for message in messages:
            if "Please enter the following code to prove that you're human" in message['content']:
                self.client.send_message(self.channel, "Captcha request detected")
                raise Exception("Captcha request detected")

    def auto_sell(self, **kwargs):
        # Bool flip to choose between pickaxe/backpack upgrade
        # False = Pickaxe
        # True = Backpack
        purchases = 0

        # Keep track of amount of sells
        sell = 0

        while True:
            self.captcha_check()

            self.client.send_message(self.channel, ";s")
            sell += 1

            if kwargs["auto_upgrade"] is True and sell % kwargs["upgrade_after"] == 0 and sell != 0:
                if purchases < 2:
                    self.upgrade_pick()
                    purchases += 1
                else:
                    self.upgrade_bp()
                    purchases = 0

            if kwargs["auto_rebirth"] is True and sell % kwargs["rebirth_after"] == 0:
                self.rebirth()

            delay = kwargs["base"] + randrange(kwargs["randomization"])
            time.sleep(delay)

    def auto_fish(self, **kwargs):
        self.captcha_check()

        while True:
            self.captcha_check()

            self.client.send_message(self.channel, ";f")
            time.sleep(kwargs['base'] + randrange(kwargs['randomization']))

    def auto_hunt(self, **kwargs):
        if self.captcha_check() is True:
            raise Exception("Captcha Request Detected..")

        while True:
            self.captcha_check()

            self.client.send_message(self.channel, ";h")
            time.sleep(kwargs['base'] + randrange(kwargs['randomization']))

    def auto_hourly(self, **kwargs):
        self.captcha_check()

        while True:
            self.captcha_check()

            self.client.send_message(self.channel, ";hourly")
            time.sleep(kwargs['base'] + randrange(kwargs['randomization']))

    def auto_quiz(self, **kwargs):
        self.captcha_check()

        while True:
            self.captcha_check()

            self.client.send_message(self.channel, ";quiz")
            time.sleep(2)
            self.client.send_message(self.channel, ANSWERS[randrange(4)])
            time.sleep(kwargs['base'] + randrange(kwargs['randomization']))

    def upgrade_pick(self):
        self.client.send_message(self.channel, ";up p a")

    def rebirth(self):
        self.client.send_message(self.channel, ";rb")

    def upgrade_bp(self):
        self.client.send_message(self.channel, ";up b a")
