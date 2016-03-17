
self.redis.zadd('flaw_scope', '{ "name":"minor"    , "score":30  }', '30')
self.redis.zadd('flaw_scope', '{ "name":"moderate" , "score":70  }', '70')
self.redis.zadd('flaw_scope', '{ "name":"major"    , "score":100  }', '100')

self.redis.zadd('flaw_quality', '{ "name":"horrible"    , "score":30  }', '30')
self.redis.zadd('flaw_quality', '{ "name":"bad" , "score":70  }', '70')
self.redis.zadd('flaw_quality', '{ "name":"poor"    , "score":100  }', '100')

# and is made out of
self.redis.lpush('flaw_enemytrait', 'devious')
self.redis.lpush('flaw_enemytrait', 'unforgiving')
self.redis.lpush('flaw_enemytrait', 'vicious')

self.redis.lpush('flaw_fleeing', 'the law')
self.redis.lpush('flaw_fleeing', 'a jilted lover')
self.redis.lpush('flaw_fleeing', 'a gang')

# and is made out of
self.redis.lpush('flaw_extremity', 'finger')
self.redis.lpush('flaw_extremity', 'toe')
self.redis.lpush('flaw_extremity', 'hand')
self.redis.lpush('flaw_extremity', 'foot')
self.redis.lpush('flaw_extremity', 'leg')
self.redis.lpush('flaw_extremity', 'arm')
self.redis.lpush('flaw_extremity', 'ear')

self.redis.lpush('flaw_allergy', 'certain foods')
self.redis.lpush('flaw_allergy', 'peanuts')
self.redis.lpush('flaw_allergy', 'dogs')
self.redis.lpush('flaw_allergy', 'cats')
self.redis.lpush('flaw_allergy', 'horses')
self.redis.lpush('flaw_allergy', 'grass')
self.redis.lpush('flaw_allergy', 'pollen')

self.redis.lpush('flaw_addiction', 'food')
self.redis.lpush('flaw_addiction', 'drug')
self.redis.lpush('flaw_addiction', 'magic')
self.redis.lpush('flaw_addiction', 'gambling')

self.redis.lpush('flaw_abuse', 'physically')
self.redis.lpush('flaw_abuse', 'mentally')
self.redis.lpush('flaw_abuse', 'psychologically')
self.redis.lpush('flaw_abuse', 'magically')

self.redis.lpush('flaw_anxiety', 'nervous')
self.redis.lpush('flaw_anxiety', 'anxious')
self.redis.lpush('flaw_anxiety', 'neurotic')
self.redis.lpush('flaw_anxiety', 'fidgety')

self.redis.lpush('flaw_defiant', 'defiant')
self.redis.lpush('flaw_defiant', 'disobedient ')
self.redis.lpush('flaw_defiant', 'insolent')
self.redis.lpush('flaw_defiant', 'brazen')
self.redis.lpush('flaw_defiant', 'bold')

self.redis.lpush('flaw_bigot', 'certain races')
self.redis.lpush('flaw_bigot', 'the opposite sex')
self.redis.lpush('flaw_bigot', 'anyone odd-looking')
self.redis.lpush('flaw_bigot', 'anyone progressive')
self.redis.lpush('flaw_bigot', 'anyone conservative')
self.redis.lpush('flaw_bigot', 'certain religions')

# your flaw: 
self.redis.lpush('flaw_template', 'You are hard of hearing')
self.redis.lpush('flaw_template', 'You are illiterate')
self.redis.lpush('flaw_template', 'You have {{params.quality[\'name\']}} breath')
self.redis.lpush('flaw_template', 'You have {{params.quality[\'name\']}} eyesight')
self.redis.lpush('flaw_template', 'You have {{params.quality[\'name\']|article}} attitude')
self.redis.lpush('flaw_template', 'You have {{params.scope[\'name\']|article}} limp')
self.redis.lpush('flaw_template', 'You are missing {{params.extremity|article}}')
self.redis.lpush('flaw_template', 'You have a visible, {{params.scope[\'name\']}} scar')
self.redis.lpush('flaw_template', 'You have {{params.enemytrait|article}} foe')
self.redis.lpush('flaw_template', 'You are on the run from {{params.fleeing}} ')
self.redis.lpush('flaw_template', 'You have {{params.scope[\'name\']|article}} addiction')
self.redis.lpush('flaw_template', 'You have {{params.scope[\'name\']|article}} an allergy to {{params.allergy}}')
self.redis.lpush('flaw_template', 'You are absentminded')
self.redis.lpush('flaw_template', 'You are {{params.abuse}} abusive')
self.redis.lpush('flaw_template', 'You are aimless')
self.redis.lpush('flaw_template', 'You are {{params.anxiety}}')
self.redis.lpush('flaw_template', 'You are arrogant')
self.redis.lpush('flaw_template', 'You are {{params.defiant}} ')

self.redis.lpush('flaw_template', 'You are a bigmouth')
self.redis.lpush('flaw_template', 'You are a bigot towards {{params.bigot}}')
self.redis.lpush('flaw_template', 'You intolerant towards {{params.bigot}}')
self.redis.lpush('flaw_template', 'You judgmental towards {{params.bigot}}')

self.redis.lpush('flaw_blunt', 'blunt')
self.redis.lpush('flaw_blunt', 'frank')
self.redis.lpush('flaw_blunt', 'callous')
self.redis.lpush('flaw_blunt', 'insensitive')
self.redis.lpush('flaw_template', 'You are too {{params.blunt}}')

self.redis.lpush('flaw_template', 'You suffer from a curse')


self.redis.lpush('flaw_template', 'You suffer from mental illness')

self.redis.lpush('flaw_reputation', 'childishness')
self.redis.lpush('flaw_reputation', 'immature')
self.redis.lpush('flaw_reputation', 'hostility')
self.redis.lpush('flaw_reputation', 'treachery')
self.redis.lpush('flaw_reputation', 'treason')
self.redis.lpush('flaw_reputation', 'disloyalty')
self.redis.lpush('flaw_reputation', 'deranged')
self.redis.lpush('flaw_reputation', 'mad')
self.redis.lpush('flaw_reputation', 'psychotic')
self.redis.lpush('flaw_reputation', 'verbally abusive')
self.redis.lpush('flaw_reputation', 'prudish')
self.redis.lpush('flaw_reputation', 'annoying')
self.redis.lpush('flaw_reputation', 'obnoxious')
self.redis.lpush('flaw_reputation', 'picking fights')
self.redis.lpush('flaw_reputation', 'being a jerk')
self.redis.lpush('flaw_reputation', 'neurotic')
self.redis.lpush('flaw_reputation', 'loud')

self.redis.lpush('flaw_deserved', 'unwarranted')
self.redis.lpush('flaw_deserved', 'overblown')
self.redis.lpush('flaw_deserved', 'well deserved')
self.redis.lpush('flaw_deserved', 'warranted')

self.redis.lpush('flaw_template', 'Your reputation for {{params.reputation}} is {{params.deserved}}')

self.redis.lpush('flaw_template', 'Your are gullible')
self.redis.lpush('flaw_template', 'Your are easily manipulated')
self.redis.lpush('flaw_template', 'Your are too trusting')
self.redis.lpush('flaw_template', 'Your are overly dependent on others')
self.redis.lpush('flaw_template', 'Your are color blind')
self.redis.lpush('flaw_template', 'Your have no sense of smell')

self.redis.lpush('flaw_template', 'Your are non-committal')
self.redis.lpush('flaw_template', 'Your are fickle')
self.redis.lpush('flaw_template', 'Your are finicky')
self.redis.lpush('flaw_template', 'You commit without thinking it through')
self.redis.lpush('flaw_template', 'Your are dyslexic')


self.redis.lpush('flaw_template', 'Your are egotistical')
self.redis.lpush('flaw_template', 'Your are boastful')
self.redis.lpush('flaw_template', 'Your are pompous')

self.redis.lpush('flaw_template', 'Your are envious of those around you')
self.redis.lpush('flaw_template', 'Your are covetous of other\'s possessions')
self.redis.lpush('flaw_template', 'Your are jealous of others')
self.redis.lpush('flaw_template', 'Your behavior is erratic')
self.redis.lpush('flaw_template', 'Your behavior is eccentric')
self.redis.lpush('flaw_template', 'Your behavior is bizarre')
self.redis.lpush('flaw_template', 'Your behavior is outlandish')
self.redis.lpush('flaw_template', 'Your behavior is strange')


self.redis.lpush('flaw_zeal', 'your religion')
self.redis.lpush('flaw_zeal', 'your race')
self.redis.lpush('flaw_zeal', 'your hobby')
self.redis.lpush('flaw_zeal', 'your weaponry')
self.redis.lpush('flaw_zeal', 'your class')
self.redis.lpush('flaw_zeal', 'your favorite food')
self.redis.lpush('flaw_zeal', 'your guild')

self.redis.lpush('flaw_template', 'Your are a fanatic about {{params.zeal}}')
self.redis.lpush('flaw_template', 'Your are a zealot regarding {{params.zeal}}')
self.redis.lpush('flaw_template', 'Your are fixated on {{params.zeal}} in most conversations')


self.redis.lpush('flaw_template', 'Your are meticulous')
self.redis.lpush('flaw_template', 'Your are obsessive compulsive')
self.redis.lpush('flaw_template', 'Your are choosy')
self.redis.lpush('flaw_template', 'Your are critical')
self.redis.lpush('flaw_template', 'Your are picky')
self.redis.lpush('flaw_template', 'Your are prissy')
self.redis.lpush('flaw_template', 'Your have an obvious but unacknowledged fetish')


self.redis.lpush('flaw_template', 'You flirt regardless of the consequences')
self.redis.lpush('flaw_template', 'You are in love with someone taking advantage of you')


self.redis.lpush('flaw_template', 'You are a fraud ')
self.redis.lpush('flaw_template', 'You are a glutton')
self.redis.lpush('flaw_template', 'You are a habitual liar')
self.redis.lpush('flaw_template', 'You are easily duped')
self.redis.lpush('flaw_template', 'You are gruff to a fault')
self.redis.lpush('flaw_template', 'You are surly to a fault')


self.redis.lpush('flaw_badhabit', 'pick your nose')
self.redis.lpush('flaw_badhabit', 'spit tobacco everywhere')
self.redis.lpush('flaw_badhabit', 'drool profusely')
self.redis.lpush('flaw_badhabit', 'have severe body odor')
self.redis.lpush('flaw_badhabit', 'are too serious')
self.redis.lpush('flaw_badhabit', 'belch loudly')
self.redis.lpush('flaw_badhabit', 'continuously bite your fingernails')
self.redis.lpush('flaw_badhabit', 'chew on things')
self.redis.lpush('flaw_badhabit', 'click or tap your teeth')
self.redis.lpush('flaw_badhabit', 'crack your knuckles')
self.redis.lpush('flaw_badhabit', 'excessively blink your eyes')
self.redis.lpush('flaw_badhabit', 'roll your eyes when others are speaking')
self.redis.lpush('flaw_badhabit', 'gesture wildly')
self.redis.lpush('flaw_badhabit', 'unconsciously hum at inappropriate times')
self.redis.lpush('flaw_badhabit', 'unconsciously whistle at inappropriate times')
self.redis.lpush('flaw_badhabit', 'lick your lips inappropriately')
self.redis.lpush('flaw_badhabit', 'pick at your teeth')
self.redis.lpush('flaw_badhabit', 'pinch others')
self.redis.lpush('flaw_badhabit', 'are vulgar')
self.redis.lpush('flaw_badhabit', 'slap people on the back way too much')
self.redis.lpush('flaw_badhabit', 'slurp everything')
self.redis.lpush('flaw_badhabit', 'talk with a full mouth')
self.redis.lpush('flaw_badhabit', 'tap your foot')
self.redis.lpush('flaw_badhabit', 'wink inappropriately')

self.redis.lpush('flaw_template', 'You {{params.badhabit}}, which other people find off-putting')
self.redis.lpush('flaw_template', 'You constantly misuse words')
self.redis.lpush('flaw_template', 'You use too much profanity')
self.redis.lpush('flaw_template', 'You squint when people speak to you')
self.redis.lpush('flaw_template', 'You have a {{params.scope[\'name\']}} stutter')

self.redis.lpush('flaw_template', 'You are hedonistic')
self.redis.lpush('flaw_template', 'You are interested in frivolous details')
self.redis.lpush('flaw_template', 'You have no sense of humor')
self.redis.lpush('flaw_template', 'You have a {{params.scope[\'name\']}} hypocritical belief')
self.redis.lpush('flaw_template', 'You are too idealistic and impractical')


self.redis.lpush('flaw_template', 'You act foolishly')
self.redis.lpush('flaw_template', 'You act carelessly')
self.redis.lpush('flaw_template', 'You are ignorant on an important topic')
self.redis.lpush('flaw_template', 'You are excitable')
self.redis.lpush('flaw_template', 'You mumble')
self.redis.lpush('flaw_template', 'You speak with a thick accent')
self.redis.lpush('flaw_template', 'You think you are funny... but you\'re not')
self.redis.lpush('flaw_template', 'You are insecure')
self.redis.lpush('flaw_template', 'You obsess over topics that no one cares about')
self.redis.lpush('flaw_template', 'You focus on unimportant details')
self.redis.lpush('flaw_template', 'You constantly distract people')
self.redis.lpush('flaw_template', 'You are barely literate')
self.redis.lpush('flaw_template', 'You are impatient')
self.redis.lpush('flaw_template', 'You are indifferent')
self.redis.lpush('flaw_template', 'You were framed for a crime you didn\'t commit')
self.redis.lpush('flaw_template', 'You are wanted for a crime you didn\'t commit')
self.redis.lpush('flaw_template', 'You are wanted for a crime you did commit')


self.redis.lpush('flaw_template', 'You are a klutz')
self.redis.lpush('flaw_template', 'You are clumsy')
self.redis.lpush('flaw_template', 'You are lazy')
self.redis.lpush('flaw_template', 'You are lewd ')
self.redis.lpush('flaw_template', 'You are lustful')
self.redis.lpush('flaw_template', 'You are obscene')
self.redis.lpush('flaw_template', 'You are indecent')
self.redis.lpush('flaw_template', 'You are lecherous ')
self.redis.lpush('flaw_template', 'You are salacious')

self.redis.lpush('flaw_template', 'You are a masochist')
self.redis.lpush('flaw_template', 'You are meddlesome')
self.redis.lpush('flaw_template', 'You interfere in the affairs of others')
self.redis.lpush('flaw_template', 'You offer your unsolicited opinion to everyone')
self.redis.lpush('flaw_template', 'You are meek')
self.redis.lpush('flaw_template', 'You are cowardly')
self.redis.lpush('flaw_template', 'You are compliant ')
self.redis.lpush('flaw_template', 'You are submissive')


self.redis.lpush('flaw_delusion', 'wealth')
self.redis.lpush('flaw_delusion', 'power')
self.redis.lpush('flaw_delusion', 'knowledge')
self.redis.lpush('flaw_delusion', 'attractiveness')
self.redis.lpush('flaw_delusion', 'skills')

self.redis.lpush('flaw_template', 'You are delusional regarding your {{params.delusion}}')
self.redis.lpush('flaw_template', 'You are naive')
self.redis.lpush('flaw_template', 'You avoid violence')
self.redis.lpush('flaw_template', 'You are nosey')
self.redis.lpush('flaw_template', 'You are oppressive')
self.redis.lpush('flaw_template', 'You are overbearing')
self.redis.lpush('flaw_template', 'You are overambitious')
self.redis.lpush('flaw_template', 'You are overemotional')
self.redis.lpush('flaw_template', 'You are overprotective of certain things, person or people')
self.redis.lpush('flaw_template', 'You overvalue your skills ')
self.redis.lpush('flaw_template', 'You are a pacifist')
self.redis.lpush('flaw_template', 'You are paranoid ')
self.redis.lpush('flaw_template', 'You are ill-tempered ')
self.redis.lpush('flaw_template', 'You are crotchety')
self.redis.lpush('flaw_template', 'You are cranky')
self.redis.lpush('flaw_template', 'You are a pest ')
self.redis.lpush('flaw_template', 'You are a nuisance')
self.redis.lpush('flaw_template', 'You are a nag')
self.redis.lpush('flaw_template', 'You are a pessimist')
self.redis.lpush('flaw_template', 'You are a perfectionist')
self.redis.lpush('flaw_template', 'You are prideful')
self.redis.lpush('flaw_template', 'You are rebellious')
self.redis.lpush('flaw_template', 'You are reckless')
self.redis.lpush('flaw_template', 'You are remorseless')
self.redis.lpush('flaw_template', 'You are overly rigorous')
self.redis.lpush('flaw_template', 'You are a sadist')
self.redis.lpush('flaw_template', 'You are cruel')
self.redis.lpush('flaw_template', 'You are obnoxiously sarcastic')
self.redis.lpush('flaw_template', 'You are skeptical of everything')
self.redis.lpush('flaw_template', 'You are skeptical things that don\'t warrant it')

self.redis.lpush('flaw_seduce', 'married men')
self.redis.lpush('flaw_seduce', 'married women')
self.redis.lpush('flaw_seduce', 'strangers')
self.redis.lpush('flaw_seduce', 'the elderly')
self.redis.lpush('flaw_seduce', 'the rich')
self.redis.lpush('flaw_seduce', 'the poor')
self.redis.lpush('flaw_seduce', 'the wrong people')
self.redis.lpush('flaw_seduce', 'the clergy')

self.redis.lpush('flaw_template', 'You seduce {{params.seduce}} for kicks')

self.redis.lpush('flaw_template', 'You are showing signs of senility')

self.redis.lpush('flaw_template', 'You are a scoundrel')
self.redis.lpush('flaw_template', 'You are selfish')
self.redis.lpush('flaw_template', 'You are a self-martyr')
self.redis.lpush('flaw_template', 'You are self-righteous')
self.redis.lpush('flaw_template', 'You are shallow')
self.redis.lpush('flaw_template', 'You are a smart ass')
self.redis.lpush('flaw_template', 'You are weak-willed')
self.redis.lpush('flaw_template', 'You are soft-hearted')
self.redis.lpush('flaw_template', 'You are nihilistic')
self.redis.lpush('flaw_template', 'You are spineless')
self.redis.lpush('flaw_template', 'You are cowardly ')
self.redis.lpush('flaw_template', 'You are wimpy')
self.redis.lpush('flaw_template', 'You are gutless')
self.redis.lpush('flaw_template', 'You are spiteful')
self.redis.lpush('flaw_template', 'You are malicious')
self.redis.lpush('flaw_template', 'You are vindictive')
self.redis.lpush('flaw_template', 'You are vengeful')
self.redis.lpush('flaw_template', 'You are spoiled')
self.redis.lpush('flaw_template', 'You are pampered')
self.redis.lpush('flaw_template', 'You are coddled')
self.redis.lpush('flaw_template', 'You have no notion of hard work')
self.redis.lpush('flaw_template', 'You are stubborn')
self.redis.lpush('flaw_template', 'You are squeamish')
self.redis.lpush('flaw_template', 'You are superstitious')
self.redis.lpush('flaw_template', 'You are tactless')
self.redis.lpush('flaw_template', 'You are temperamental')
self.redis.lpush('flaw_template', 'You are moody ')
self.redis.lpush('flaw_template', 'You are irritable')
self.redis.lpush('flaw_template', 'You are sensitive')
self.redis.lpush('flaw_template', 'You are volatile')
self.redis.lpush('flaw_template', 'You tempt others into misbehaving')
self.redis.lpush('flaw_template', 'You are shy')
self.redis.lpush('flaw_template', 'You are a troublemaker')
self.redis.lpush('flaw_template', 'You are ugly')
self.redis.lpush('flaw_template', 'You are unattractive')
self.redis.lpush('flaw_template', 'You are unlucky')
self.redis.lpush('flaw_template', 'You are a backstabber')
self.redis.lpush('flaw_template', 'You are unpredictable')
self.redis.lpush('flaw_template', 'You are vain')
self.redis.lpush('flaw_template', 'You are conceited')
self.redis.lpush('flaw_template', 'You are narcissistic')

