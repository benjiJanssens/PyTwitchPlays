from math import ceil
from threading import Timer
from datetime import datetime, timedelta
from pytwitchchat import TwitchChatClient
from direct_input import press_key, release_key


class TwitchPlays:
    def __init__(self, password, username, channel, actions):
        self.TWITCH_CHAT_CLIENT = TwitchChatClient(password, username, channel, self.handle)
        self.ACTIONS = actions
        self.active_chatters = {}

    def run(self):
        self.TWITCH_CHAT_CLIENT.connect()
        self.TWITCH_CHAT_CLIENT.run()

    def handle(self, message, user, is_mod):
        self.active_chatters = {
            k: v for k, v in self.active_chatters.items() if v > (datetime.now() - timedelta(minutes=1))
        }
        self.active_chatters[user] = datetime.now()
        if message.lower() in self.ACTIONS:
            self.ACTIONS[message.lower()].run(
                user, self
            )


class Action:
    def __init__(self, key, time, string_voting=None, string_vote_passed=None, voting_ratio=None):
        self.__KEY = key
        self.__TIME = time
        self.__TIMER = Timer(
            self.__TIME, release_key, [self.__KEY]
        )
        self.__STRING_VOTING = string_voting
        self.__STRING_VOTE_PASSED = string_vote_passed
        self.__VOTING_RATIO = voting_ratio
        self.__voters = {}

    def __execute(self):
        if self.__TIMER.is_alive():
            self.__TIMER.cancel()
        else:
            press_key(self.__KEY)
        self.__TIMER = Timer(
            self.__TIME, release_key, [self.__KEY]
        )
        self.__TIMER.start()

    def __vote(self, user, twitch_plays_instance):
        self.__voters = {
            k: v for k, v in self.__voters.items() if v > (datetime.now() - timedelta(minutes=1))
        }
        self.__voters[user] = datetime.now()
        if len(self.__voters) / len(twitch_plays_instance.active_chatters) >= self.__VOTING_RATIO:
            self.__voters.clear()
            twitch_plays_instance.TWITCH_CHAT_CLIENT.send_message(
                "/me " + self.__STRING_VOTE_PASSED
            )
            self.__execute()
        else:
            twitch_plays_instance.TWITCH_CHAT_CLIENT.send_message(
                "/me " +
                str(len(self.__voters)) +
                "/" +
                str(ceil(len(twitch_plays_instance.active_chatters) * self.__VOTING_RATIO)) +
                " votes to " + self.__STRING_VOTING
            )

    def run(self, user, twitch_plays_instance):
        if self.__VOTING_RATIO is None:
            self.__execute()
        else:
            self.__vote(user, twitch_plays_instance)
