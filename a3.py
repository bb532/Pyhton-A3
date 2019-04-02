# a3.py
# Beverly Balasu bb532
# 3/28/17
# skeleton by Lillian Lee (LJL2)

"""CS1110 assignment on processing and comparing text samples"""


import random
import a3given 
import math # for the log function


# This function is the core of a3given.sample_from_source_file
def make_sample(textstring, label):
    """Returns: a new Sample where all its attributes are filled in correctly
    with respect to the string textstring.

    Preconditions: textstring is a nonempty string of English text.  Words are
    delimited by whitespace, are all lowercase, and all punctuation has been
    removed."""
    # STUDENTS: because we haven't talked about writing your own methods yet,
    # your function will be directly modifying the attributes of a Sample that
    # you create. This is UNORTHODOX python; later, you'll learn the "right"
    # way to do this, which involves writing the __init__ method for Sample.

    # REPLACE WITH YOUR IMPLEMENTATION

    # HINT: First, create a new Sample and set up the "easy" attributes.
    sample = a3given.Sample()
    sample.label = label
    sample.text = textstring.split()
    sample.length = len(sample.text)

    ## Using three separate passes through sample.text, for code simplicity
    ## Could have done one pass, with the unigram, bigram and trigram data
    ## updated simulataneously, but the code would probably be hard to read.

    # REQUIREMENT: fill in sample.unigram_counts by a for-loop through sample.text
    # HINT: Whether or not a key is already in sample.unigram_counts is important
    #       to check.
    for x in sample.text:
        if x not in sample.unigram_counts:
            sample.unigram_counts[x] = 1
        else:
            sample.unigram_counts[x] = sample.unigram_counts[x] + 1
        

    # REQUIREMENT: Compile the bigram dictionary by going through all
    # possible bigram beginnings.
    # Note that a bigram cannot start at index sample.length-1 in sample.text
    for w in range(len(sample.text)-1):
        if sample.text[w] not in sample.bigram_dict:
            sample.bigram_dict[sample.text[w]] = [sample.text[w+1]]
        else:
            sample.bigram_dict[sample.text[w]].append(sample.text[w+1])

    # Compile the trigram dictionary by going through all possible trigram starts.
    # Note that a trigram can't start at index sample.length-2 in sample.text
    for y in range(len(sample.text)-2):
        if (sample.text[y] + ' ' + sample.text[y+1]) not in sample.trigram_dict:
            sample.trigram_dict[sample.text[y] + ' ' + sample.text[y+1]] = [sample.text[y+2]]
        else:
            sample.trigram_dict[sample.text[y] + ' ' + sample.text[y+1]].append(sample.text[y+2])
    return sample

def merge(samplelist, label):
    """Returns a new Sample whose text is the concatenation of the text for
    all the Samples in samplelist and whose label is <label>.

    Precondition: samplelist is a list of Samples of length >= 2.
    """
    # REPLACE WITH YOUR IMPLEMENTATION

    # Implementation hint: all you need to do is create the right text to feed
    # into make_sample.
    samplestring = ''
    for x in samplelist:
        for y in range(len(x.text)):
            samplestring = samplestring + ' ' + x.text[y]
    return make_sample(samplestring, label)



def diffs(s1, s2, k):
    """Returns: [justs1, justs2, ranked], where
    justs1 is a list of words occurring at least k times in s1.text but never in s2.text
        (order doesn't matter);
    justs2 is a list of words occurring at least k times in s2.text but never in s1.text
        (order doesn't matter)
    ranked is a list of items [word, logprobratio] where word occurs in both s1.text
        and s2.text, and logratio is the score mentioned in the assignment
        handout, rounded to 3 decimal digits using round(f, 3) where f is a float
        The items in ranked are sorted by logprobratio, highest first.

    Precondition: s1 and s2 are Samples."""
    pass # REPLACE WITH YOUR IMPLEMENTATION

    # HINT: first create justs1, justs2, and ranked as empty lists []
    justs1 = []
    justs2 = []
    ranked = []
    
    for x in s1.unigram_counts:
        if x not in s2.unigram_counts and s1.unigram_counts[x]>=k:
            justs1.append(x)
        elif x in s2.unigram_counts:
            numerator = float(s1.unigram_counts[x])/s1.length
            denominator = float(s2.unigram_counts[x])/s2.length
            logprobratio = math.log(numerator/denominator)
            ranked.append([x, round(logprobratio, 3)])
            
    for y in s2.unigram_counts:
        if y not in s1.unigram_counts and s2.unigram_counts[y]>=k:
            justs2.append(y)
    # HINT: first, loop through the keys of s1.unigram_counts
    # For each such word w, check whether it's in s2.unigram_counts.
    # If w isn't, if  and w occurs at least k times in s1.text, append it to justs1.
    # If it is, append [w, logratio] to ranked
    #
    # You can use "x in alist" and "y in adictionary" as boolean expressions
    #
    # To get the log function, use math.log (using the default base)
    #
    
    # HINT: then, check in s2.unigram_counts for words not in s1.unigram_counts

    # HINT: there's a function you can use to sort ranked in module a3given.
    a3given.sort_weighted_list(ranked)
    # HINT: this should be your final line
    return [justs1, justs2, ranked]



def bigram_generation(s, k):
    """Returns <= k-token string according to the bigram dictionary of Sample s.
    Fewer than k tokens are generated if the generator chooses a token that
    is not followed by any token in s.text (in particular, the last token might
    have that property.)

    Preconditions: k>1 is an int."""

    ## STUDENTS: we start by picking the first token.
    # This line picks a random item from the list s.text and stores it in output
    output = random.choice(s.text)
    prev_word = output  # prev_word is always the most recently generated word

    ## STUDENTS: now finish the body of this function, using any hints or
    # requirements mentioned below.

    ## REQUIREMENT: use a for-loop to perform k-1 times the following:
    # if prev_word is in the bigram dictionary,
    # (1) choose the next word randomly from the dictionary entry for the
    #     previous word (since that's where the possible words to follow
    #     prev_word are stored)
    # (2) add the new next word to output
    # (3) since you're moving on to the next-next word, set prev_word to
    #     be the word you just selected.
    # But if prev_word is not in the bigram dictionary, do nothing in the loop.
    for x in range(k-1):
        if prev_word in s.bigram_dict:
            rand = random.choice(s.bigram_dict[prev_word])
            output = output + ' ' + rand
            prev_word = rand
    
    return output

def trigram_generation(s, k):
    """Generate <= k-token string according to the trigram dictionary of Sample
    s.

    Fewer than k tokens are generated if the generator chooses a token that
    is not followed by any token in s.text (in particular, the last token might
    have that property.)

    Preconditions: k>2 is an int, s is a Sample."""
    # REPLACE WITH YOUR IMPLEMENTATION.

    # REQUIREMNET: first, randomly pick a starting bigram "w1 w2".
    start = bigram_generation(s, 2)
    output = ""
    # Then, use a  for-loop to create the next k-2 words.
    # In the loop body,
    # (1) choose the next word w3 randomly from the list stored in the trigram
    #   dictionary for "w1 w2".
    # (2) do something to get w2 added to your output
    # (3) update the information you're storing so that you know that now "w2 w3"
    #   are the last two words generated.
    for x in range(k-2):
        if start in s.trigram_dict:
            next_word = random.choice(s.trigram_dict[start])
            second_word = start[start.index(" ")+1:]
            output = output + " " + second_word
            start = second_word + " " + next_word
    
    return output


