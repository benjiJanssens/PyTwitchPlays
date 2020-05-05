# PyTwitchPlays

PyTwitchPlays is a Python package to create your own Twitch Plays channel

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install PyTwitchPlays.

```bash
pip install pytwitchplays
```

## Usage

```python
from pytwitchplays import TwitchPlays, Action

ACTIONS = {
    "command": Action(BUTTON, DURATION),
    "command with voting": Action(BUTTON, DURATION, COMMAND_NAME, SUCCESS_MESSAGE, PERCENTAGE_REQUIRED),
}
TWITCH_PLAYS = TwitchPlays(password, username, channel, ACTIONS)
TWITCH_PLAYS.run()
```

* **\<password>** needs to be an OAuth token. You can use [Twitch Chat OAuth Password Generator](https://twitchapps.com/tmi) to generate an OAauth token.
* **\<username>** and **\<channel>** need to be in lowercase.
* **PERCENTAGE_REQUIRED** needs to be a decimal.

[direct_input_keyboard_scan_codes.py](https://github.com/benjiJanssens/PyTwitchPlays/blob/master/pytwitchplays/direct_input_keyboard_scan_codes.py) contains a list of buttons you can use.

Take a look at [TwitchPlaysTrackmania](https://github.com/benjiJanssens/TwitchPlaysTrackmania) for a sample implementation of PyTwitchPlays using Trackmania.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)