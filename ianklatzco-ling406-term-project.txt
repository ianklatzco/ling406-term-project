##############################################################################
#   PROJECT                                                                  #
##############################################################################

    Chat message generator, using a markov chain,
    	Investigated bigram probabilities, and adversarial neural networks.

##############################################################################
#   MOTIVATION (why did i do this instead of the default project)            #
##############################################################################

	Broadly speaking, realistic text generation is useful in the realm of
		say, chatbots. If we want to interact with computers in text-only
		fashions, it'd be useful to be able to interact with them like
		how we can interact with other humans now, and then still have
		access to all their resources in a way that doesn't require teaching
		everyone the arcane art of "how to program".

    i like working with python and the telegram API.
        i've used markov chain bots before, but i didn't really write any of
        the code and i wanted to figure out how they actually work.

    i also love meta-analysis of how much i communicate with my friends
    verbally, and this provides a great opportunity to get stats on that.

##############################################################################
#   PROBLEM                                                                  #
##############################################################################

	Programmatically generating realistic-looking text is hard.
	
	Given an input corpus, how do we make text that looks like it came from
		the input corpus?

	Cleverbot was an early example, which was fairly random, but managed to
		sometimes spit out believeable sentences.

	There was a brief period on twitter where "_ebooks" bots were popular -
		after someone made twitter.com/horse_ebooks. You could run a script
		against your corpus of tweets, and it'd try generating tweets that
		looked like yours.

##############################################################################
#   PREVIOUS WORK                                                            #
##############################################################################

	Cleverbot.com was an early example, which was fairly random, but managed to
		sometimes spit out believeable sentences/queries.

	I set up an ebooks acconut for my best friend a while back. Our friends
		got a kick of it, while the server I ran it up was still alive.
			twitter.com/stinakat_ebooks

    "generated adversarial networks" work to synthesize real-valued data from
        input data, but it doesn't work on text.
        Some researchers from Duke applied this, and this looks like a cool
        "next steps" if I wanted to continue this past just markov chains.

        https://zhegan27.github.io/Papers/textGAN_nips2016_workshop.pdf
        https://web.stanford.edu/class/cs224n/reports/2761133.pdf

##############################################################################
#   TOOLS                                                                    #
##############################################################################

    Telegram messenger, my primary mode of communication, to dump all
        messages that I've sent over the past two years.

    tg - telegram cli - https://github.com/vysheng/tg
        bad C client to access the telegram api directly
            (telegram's api is documented horrendously)

    telegram-history-dump https://github.com/tvdstaaij/telegram-history-dump
        ruby script to yank messages out of tg-cli

    python 3.6, my baby

##############################################################################
#   COMMENT                                                                  #
##############################################################################

    I did use other code in this project: a "how to make your own markov chain"
        blog post as a starting point and, and a python library, markovify,
        as a gold standard.

    I have sourced this code, and commented it line-by line, in order to
        learn how it works.

##############################################################################
#   FILES                                                                    #
##############################################################################

    corpus-processing/
        fullDataset-to-myMessagesOnly.py
            converts JSON-formatted datasets with a mix of messages from lots
            of people to newline-separated messages typed by me alone.

    scripts that, when run, return generated strings.
    message-generating/

        markov-naive.py
            simply markov example from http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/
        markov-mine.py
            my modifications to the above script
        markov-ify.py
            a nice library for text generation, our "golden standard"
            https://github.com/jsvine/markovify
        markov-nltk.py
            an attempt to use nltk that didn't pan out. i spent a couple
            hours on it, so i'm submitting it even thought it doesn't work.

    ling-telegram-bot/bot.py
        bot to run testing interactions.

    data/
        name.txtfmtd - text files containing the results of texting from
            various friends of mine.

##############################################################################
#   APPROACH                                                                 #
##############################################################################

    Preprocessing: fullDataset-to-myMessagesOnly.py
        I scraped all my messages off of telegram.
        I parsed them to be just message with "Ian Klatzco" in the from field.
        I removed any links or media (images, music)

        I decided to use just my primary groupchat as the corpus, in the
            interest of preserving the privacy of the others who I communicate
            with in text-based form. This is "output/xFF5353.txt".

    Learning how to markov:
        I found a simple existing text generator, and used it to understand
            how to implement a markov chain for text generation.
        http://agiliq.com/blog/2009/06/generating-pseudo-random-text-with-markov-chains-u/

        I commented the code and made some changes to clarify.

    Making my own:
        Once I understood it, I modified the above code to include start
        and end symbols on each sentence, in the hope that this would
        generate more realistic messages.

    Using a library for the gold standard:
        I found a nice markov chain library that generates very convincing
        messages. This is my "gold standard" to test against.

    TESTING:
        I created a telegram bot that randomly selects a message I have sent
        to a particular groupchat, and generates messages using each of the
        three message generation scripts. That is to say:

            - the naive approach, which treats the corpus as one very long string
            - my extension to that approach, which has start/end terminators
            - a gold standard, a python "markovify" library.
            and a real message pulled from the dataset.

        I ask my friends to select which of the four is the real message.
        this is stored in data/

    PARSING:
        I recorded their responses in an ugly format, and had to write a 
            lot of formatting scripts.
        data/remove-double-taps.py handles most of this.


##############################################################################
#   RESULTS                                                                  #
##############################################################################

    data/count-probabilities.py

    returns:
         52  naive
        366  mine
        126  markovify
        737  real
       ----
       1371

    Each number is one test by a user. Every time a user selects an option,
        I increment the one they chose.

    That is to say, my markov chain generator, with added start/end
        terminators, performed better than the other two!!! which is
        suprising and exciting~!!!!

    If you wanna see the bot in action, t.me/ling_406_bot


##############################################################################
#   PROBLEMS                                                                 #
##############################################################################

    Sometimes, I newline-separate longer messages. These are sorted into
    different messages when I do parsing.

    Sometimes, I send friends things like. Hashes.
        That'll be fun.
        I don't think I have a super good way of identifying... non-messages?
        So I'm just gonna leave em in there!

    Many of the friends who did this are in the groupchat that I sent the
        original messages to, so they had a leg up on others because they may
        have seen the messages before. (they could also ctrl+f) the groupchat,
        but that's not something i'm too concerned about.

    As usual, my python code is disgustingly ugly. I'm sorry.

    If you mashed buttons, things would go wrong. I had to filter
        the dataset a little bit in order to catch double-generated messages
        that didn't actually produce useful data.

##############################################################################
#   DISCUSSION AND CONCLUSIONS                                               #
##############################################################################

    Things I learned:
        Python generators.
        Python objects and the self keyword.
        What markov chains actually do:
            Decide next state purely based on current state. Say current state
                is the two previous words: we pick the next word based
                exclusively on these two.
        Generated adversarial neural networks exist: you use two neural
            networks to generate final output. They're a form of unsupervised
            machine learning.

    Making a basic markov chain is extraordinarily straightforward. Adding a
        bit of bonus to it (start/end string terminators) increasing its
        efficacy by quite a bit.

    If I were to do it again, I would not let people from the chat participate.

    I would also increase the size of the corpus to my entire dataset, ie,
        all messages I sent to everyone over the past two years or so.

    This test isn't perfect - it's subject to a lot of things that potentially
        detract from clean data (such as members of the chat being able to
        search messages) - but i'm effectively recreating the turing test.

        I think it's alright, altogether, for evaluating what I'm trying to
            evaluate.

