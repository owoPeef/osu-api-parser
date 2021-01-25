# osu-api-parser
This custom parser by FazziCLAY (https://fazziclay.ru/)

This tool allows you to easily access the API of a game called "osu!", tool was written for your discord bots, VK, telegrams, and so on. Written in the Python programming language.

To get started, you need to get the api key (http://osu.ppy.sh/p/api), then you must download the file (osuapi.py) and place it in the same folder as your main file, import it in the file (import osuapi), also, you must create a variable with the api itself, for example:
api = osuapi.OsuApi ("api key")
In your methods, you write variables like
user = api.get_user (nick) | get a user (from there you can take data in JSON format (get_user and other methods look there https://github.com/ppy/osu-api/wiki), an example of them:
user_id; level; join_date; accuracy and the like.
