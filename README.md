# PythonJishoBot
A modification and improvement of https://github.com/trohrt/python_jisho for Twitch Bot usage.

Running the Python3 script will make it connect to a Twitch account that will join a channel of preference.
The Jisho API gives a lot of tags and up to 10 results so we make use of trohrt's existing code to put them into lists.
This code, however, does not contain failsafes for searching blank terms or terms that give no results on Jisho. This has been fixed in this version.

When a user types !jisho <word> or !j <word> into the Twitch channel, this code will parse the first result from the sorted lists with a clean format.
It's not totally perfect but it does the job for a quick Jisho lookup.

Many thanks to https://github.com/darkedge for sharing his programming skills for this script, I would not have been able to do this on my own!
