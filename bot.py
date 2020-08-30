from credentials import createInterface
import timeManager

COUNTDOWN_SENTENCE = "%d days, %d hours, %d minutes and %d seconds left until it happens"
REPLY_MENTIONS_SENTENCE = "Sorry @%s, I can't hear you through the sound of Time unavoidably passing by"
FINAL_SENTENCE = "The time has come. Goodbye everyone. Thank you for walking this path with me"

api = createInterface()


def updateCountdown():
    # check if it is time to update the countdown
    countdown_must_be_updated = timeManager.checkLastUpdateTime()
    if countdown_must_be_updated == -1:
        print ("not enough time between the updates of countdowns.")
        return

    difference, days = timeManager.calculateDifferenceCurrentDate_FinalDate()

    # check if the finish date has been reached
    if days < 1 and difference.hours < 8:
        doFinishDate()
        return

    # Update the countdown
    api.update_status(COUNTDOWN_SENTENCE % (days, difference.hours, difference.minutes, difference.seconds))
    print("countdown updated")


def answerWhenMentioned():
    mentions = api.mentions_timeline(count=50)
    i = 0

    last_replied_mention_time = timeManager.get_last_replied_mention_time()

    for mention in mentions:

        # whe only reply to those mentions which we have not replied yet
        if mention.created_at > last_replied_mention_time:
            if i == 0:
                # whe only save the time of the first retrieved tweet (the newer)
                timeManager.set_reply_mention_time(str(mention.created_at))
                i = 1

            user_name = mention.user.screen_name
            api.update_status(REPLY_MENTIONS_SENTENCE % user_name, mention.id)

            print("mention replied")


# TODO when someone DMs the bot it should reply automatically
def answerDMs():
    return


def doFinishDate():
    api.update_status(FINAL_SENTENCE)
    timeManager.setUnachievableDates()


# answerDMs()
updateCountdown()
answerWhenMentioned()
