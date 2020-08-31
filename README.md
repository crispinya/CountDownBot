# @CountdownTheBot - twitter bot

A simple twitter bot (@CountdownTheBot) created in Python using the Tweepy library.

## Table of contents
* [General info](#general-info)
	* [Personal note](#personal-note)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Contact](#inspiration)

## General info

This project aims to create a simple Twitter bot using Python and the Tweepy Library. 

This bot (@CountdownTheBot) makes a countdown in its timeline (it updates the time left every eight or more hours. The python script runs, thanks to the task manager, when the computer is powered on). It also replies with a fixed sentence to tweets mentioning it.

As explained later on this readme, some improvements could be implemented to make the project more interesting.

### Personal note

For me (the creator) doing this project has been a way of learning Python (a programming language I had barely used before) while having fun and allowing myself to be creative. It has been a delight working on this bot.

I hope it also brings you (the reader) some kind of joy or, at least, I hope it gives you a will to keep learning and programming while also having fun.
	
## Technologies
Project created using:
 * Python 2.7
	* Tweepy library 3.9.0
	
## Setup
In order to use this project you should follow the next steps:

 1. Install the [tweepy library](http://docs.tweepy.org/en/latest/install.html)

In the cmd:
```
pip install tweepy
```

2. Import this project

3. Set up the credentials

Substitute the credentials in the credentials python file with the ones from your twitter developer account/project.

4. Schedule the run of the script

As an optional step, the bot script can be configured with the Task Manager (Windows) so it runs at a specified time or after a specified action (for example, when the computer is turned on).


## Features
**Current features:**
*  [x] Update the countdown ,    `updateCountdown()`

This function includes a checking that the last time the countdown was published was eight or more hours ago.
This validation is need because, locally, the script is configured (by the Task Manager) to run itself each time the computer is power on. To avoid having too many updates following each other (if, for example, the computer restarts itself) the validation is implemented.

In case the update is possible:


![enter image description here](https://i.ibb.co/M9QP77H/Countdown.png)

* [x]  Answer when mentioned, `answerWhenMentioned()`

The bot replies (when the script is run by the task manager) with a fixed sentence to tweets mentioning it:

![enter image description here](https://i.ibb.co/r4F3WH9/mention.png)


**Future possible upgrades:**

 * [ ] Implement replies to direct messages (DMs).
`answerDMs()`
 * [ ] Implement more complex replies to mentions and DMs
	 * Implement IA powered replies.

## Status
This project is **in progress**, as it is still being used as a learning tool by its creator.

## Contact
Created by [Cristina Piña Miguelsanz](https://www.linkedin.com/in/cristina-pina/) - feel free to contact me!
