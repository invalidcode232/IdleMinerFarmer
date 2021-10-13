import requests
import time


class Discord:
    def __init__(self, token):
        self.token = token
        self.header = {
            "Authorization": self.token,
            "User-Agent": "Chrome/86.0.4240.75",
            "Accept-Language": "en-GB",
            "Content-Type": "application/json"
        }

        # Check if token is valid
        try:
            user_data = requests.get(f"https://discord.com/api/users/@me", headers=self.header)
        except requests.exceptions.ConnectionError:
            print("Connection error, this could be an issue with the server or your connection..")
        else:
            if user_data.status_code != 200:
                raise Exception(f"Error while logging in with token | Status code: {user_data.status_code}")
            else:
                user_json = user_data.json()
                print(f"Logged in successfully as {user_json['username']}#{user_json['discriminator']} ({user_json['id']})")

    def typing(self, channel):
        try:
            response = requests.post(f"https://discord.com/api/v9/channels/{channel}/typing", headers=self.header)
        except requests.exceptions.ConnectionError:
            print("Connection error, this could be an issue with the server or your connection..")
        else:
            if response.status_code >= 300:
                raise Exception(f"An unknown error occurred while typing | Status code: {response.status_code}")

    def send_message(self, channel, content):
        self.typing(channel)

        time.sleep(1)

        payload = {
            "content": content,
            "tts": "false"
        }

        try:
            response = requests.post(f"https://discord.com/api/v9/channels/{channel}/messages", json=payload, headers=self.header)
        except requests.exceptions.ConnectionError:
            print("Connection error, this could be an issue with the server or your connection..")
        else:
            if response.status_code != 200:
                raise Exception(f"An unknown error occurred while sending message | Status code: {response.status_code}")
