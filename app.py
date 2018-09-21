#! /usr/bin/python3

import praw
import dateparser
import time
import datetime
import config
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
log = logging.getLogger(__name__)
logging.Formatter('%(levelname)s T: %(thread)d - P: %(process)d - %(asctime)s - %(name)s - %(message)s')



def mooch_convert(start, end):

    # start and end are both tuples

    s = time.mktime(start.timetuple())
    e = time.mktime(end.timetuple())
    return str((e - s)/864000)


def parse_arbitrary(phrase):
    log.debug(phrase)

    """
    input formats:
    !moochbot

    """
    if 'sessions' in phrase.lower():
        start_date = dateparser.parse('February 8, 2017')
        end_date = datetime.datetime.now()
        mooch_count = mooch_convert(start_date, end_date)
        return "Jeff Sessions has been in office for {} mooches".format(mooch_count)

    elif 'pence' in phrase.lower():
        start_date = dateparser.parse('January 20, 2017')
        end_date = datetime.datetime.now()
        mooch_count = mooch_convert(start_date, end_date)
        return "Mike Pence has been in office for {} mooches".format(mooch_count)

    elif 'pompeo' in phrase.lower():
        start_date = dateparser.parse('March 13, 2017')
        end_date = datetime.datetime.now()
        mooch_count = mooch_convert(start_date, end_date)
        return "Mike Pompeo has been in office for {} mooches".format(mooch_count)

    elif 'mnuchin' in phrase.lower():
        start_date = dateparser.parse('February 13, 2017')
        end_date = datetime.datetime.now()
        mooch_count = mooch_convert(start_date, end_date)
        return "Steve Mnuchin has been in office for {} mooches".format(mooch_count)

    elif 'mattis' in phrase.lower():
        start_date = dateparser.parse('January 20, 2017')
        end_date = datetime.datetime.now()
        mooch_count = mooch_convert(start_date, end_date)
        return "Jim Mattis has been in office for {} mooches".format(mooch_count)

    elif 'ross' in phrase.lower():
        start_date = dateparser.parse('February 27, 2017')
        end_date = datetime.datetime.now()
        mooch_count = mooch_convert(start_date, end_date)
        return "Wilbur Ross has been in office for {} mooches".format(mooch_count)

    elif 'perdue' in phrase.lower():
        start_date = dateparser.parse('April 24, 2017')
        end_date = datetime.datetime.now()
        mooch_count = mooch_convert(start_date, end_date)
        return "Sonny Perdue has been in office for {} mooches".format(mooch_count)

    elif 'tillerson' in phrase.lower():
        start_date = dateparser.parse('February 1, 2017')
        end_date = dateparser.parse('March 13, 2018')
        mooch_count = mooch_convert(start_date, end_date)
        return "Rex Tillerson was in office for {} mooches".format(mooch_count)

    elif 'kelly' in phrase.lower():
        start_date = dateparser.parse('July 31, 2017')
        end_date = datetime.datetime.now()
        mooch_count = mooch_convert(start_date, end_date)
        return "John Kelly has been in office for {} mooches".format(mooch_count)

    elif 'zinke' in phrase.lower():
        start_date = dateparser.parse('March 1, 2017')
        end_date = datetime.datetime.now()
        mooch_count = mooch_convert(start_date, end_date)
        return "Ryan Zinke has been in office for {} mooches".format(mooch_count)

    elif 'acosta' in phrase.lower():
        start_date = dateparser.parse('April 28, 2017')
        end_date = datetime.datetime.now()
        mooch_count = mooch_convert(start_date, end_date)
        return "Alex Acosta has been in office for {} mooches".format(mooch_count)

    elif 'carson' in phrase.lower():
        start_date = dateparser.parse('March 2, 2017')
        end_date = datetime.datetime.now()
        mooch_count = mooch_convert(start_date, end_date)
        return "Ben Carson has been in office for {} mooches".format(mooch_count)

    elif 'priebus' in phrase.lower():
        start_date = dateparser.parse('January 20, 2017')
        end_date = dateparser.parse('July 28, 2017')
        mooch_count = mooch_convert(start_date, end_date)
        return "Reince Priebus has been in office for {} mooches".format(mooch_count)

    elif 'pruitt' in phrase.lower():
        start_date = dateparser.parse('February 17, 2017')
        end_date = dateparser.parse('July 6, 2018')
        mooch_count = mooch_convert(start_date, end_date)
        return "Scott Pruitt was in office for {} mooches".format(mooch_count)

    elif 'scaramucci' in phrase.lower():
        return "The Mooch was in office for 1 mooch"

    else:

        from dateparser.search import search_dates
        res = search_dates(phrase)
        log.debug(res)
        if len(res) == 2:
            start_date = res[0][1]
            end_date = res[1][1]
            mooch_count = mooch_convert(start_date, end_date)
            return "{} mooches between {} and {}".format(mooch_count, start_date.strftime("%B %d, %Y"),
                                                     end_date.strftime("%B %d, %Y"))
        elif len(res) == 1:
            start_date = res[0][1]
            end_date = datetime.datetime.now()
            mooch_count = mooch_convert(start_date, end_date)
            return "{} mooches between {} and {}".format(mooch_count, start_date.strftime("%B %d, %Y"),
                                                     end_date.strftime("%B %d, %Y"))
        else:
            return None



def moochbot():
    client_id = config.CLIENT_ID
    client_secret = config.CLIENT_SECRET
    username = config.USERNAME
    password = config.PASSWORD
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, password=password, username=username,
                         user_agent='Moochbot 0.1')
    # debug
    try:
        for comment in reddit.subreddit('all').stream.comments(skip_existing=True):
            if '!moochbot' in comment.body or 'how many mooches' in comment.body.lower():
                ret = parse_arbitrary(comment.body)
                log.debug(ret)
                if ret is not None:
                    comment.reply(ret)
            else:
                pass
    except Exception as e:
        log.debug(e)


if __name__ == '__main__':
    try:
        moochbot()
    except:
        pass















