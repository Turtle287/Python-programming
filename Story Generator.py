import random
when=['A few years ago', 'once upon a time', 'a long time ago', 'last year']
who=[' a frog ', ' a wizard ', ' a rabbit ', ' a terrapin ', ' a monkey ']
where=[ 'candy land', 'farm', 'bamboo forest', 'mountain', 'pond']
why=['because he wanted treasure', 'because he wanted friends', 'because he was looking for a home']
print(random.choice(when)+','+random.choice(who)+'lived in a '+random.choice(where)+' '+random.choice(why))
