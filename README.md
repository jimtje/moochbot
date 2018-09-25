# **Moochbot**

### What is it?

This bot turns time periods to "Mooches", which is signified by the 10 day "reign" of Anthony Scaramucci as White House Communications Director in July, 2017

### How to run it

Change config.example.py to config.py and then fill in information.


Packages used:
```
praw
dateparser
```

### How to use it
This bot reads all comments on /r/politics (can be customized, of course), and then looks for "!moochbot" or "how many mooches" and then parse the comment afterwards to read date pairs, and if there is only one date, assume that the date pair is the parsed date and today. Also, there are some pre-set pairs for some administration officials.
