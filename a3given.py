# a3given.py
# Beverly Balasu bb532
# March 28, 2017


"""Prewritten code for students' text-sample assignment."""

import a3  # This file uses students' make_sample
import random

class Sample(object):
    """A Sample of text has the following attributes:

        label: a string.  A name the user gives to the Sample.

        text: a list of the words from some original document, in the order they
            appeared in that document, all converted into lowercase. We assume
            that punctuation has been removed and no words contain whitespace.

        length: a non-negative int.  The length of text.

        unigram_counts: a dictionary.  Keys are words that appear in text (no
            repeats).  The value for a given word w is the number of times
            w occurs in text.

        bigram_dict: a dictionary whose keys are words that appear in text (no
            repeats).  The value for a given key w is a list of each of the words
            that immediately follow w in text, repeats included.

        trigram_dict: a dictionary whose keys are two-word sequences that occur
            in text, separated by a space when stored as a key.
            The value for a given key (word pair) "w x" is a list of each word
            that immediately follows "w x" in text.


        Example: if text were ["a", "man", "a", "plan", "a", "canal"],
        then
            unigram_counts should contain key-value pairs "a":3, "man":1, etc.
            bigram_dict should contain key-value pairs "a":["man", "plan", "canal"],
                "man":["a"], etc.
            trigram_dict should contain key-value pairs "a man":["a"],
                "man a":["plan"], etc.
            """

    def __init__(self):
        """Creates Sample with label, text, unigram_counts, bigram_dict, trigram_dict
        all set to the empty string/list/dictionary, and length set to 0.

        (Because we haven't covered writing methods yet, students will
        be doing initialization via non-method functions.)"""
        self.label = ""
        self.text = []
        self.length = 0
        self.unigram_counts = {}
        self.bigram_dict = {}
        self.trigram_dict = {}


def sample_from_source_file(f, label):
    """Returns: a new Sample where all its attributes are filled in with respect
        to the contents of file f.

        Preconditions: f is a string that is the name of a plaintext file that
        is in a subdirectory of the current directory called sources."""

    import string # Access some utilities and handy constants

    inputfile = open("sources/"+f, 'r') # Create a file object in read-only mode.
    content = inputfile.read()
    inputfile.close() # Close the file.

    # Use string.translate to downcase all words and delete all punctuation.
    # Method "translate" requires a translation table.
    downcaser = string.maketrans(string.ascii_uppercase, string.ascii_lowercase)
    d_error_msg = "sample_from_source_file error: "
    d_error_msg += "length mismatch in ascii_upper/lowercase"
    assert len(string.ascii_uppercase) == len(string.ascii_lowercase), d_error_msg
    content = content.translate(downcaser, string.punctuation)

    return a3.make_sample(content, label)


def _second_item(sublist):
    """Helper for sort_weighted_list.
    Returns: sublist[1].
    Precondition: sublist is a list of length 2"""
    return sublist[1]


def sort_weighted_list(wl):
    """Sorts weighted list wl, largest-weight items first. Does not return
    anything.

    Precondition: all items in wl have the form [key, weight], where weight is
    a number (int or float)."""

    wl.sort(key=_second_item, reverse=True)

# TO BE USED TO HELP YOU DEBUG!
def print_summmary_stats(s):
    """Prints out some statistics about sample s.

    To be used by students to help debug!"""
    print "Label: " + str(s.label)
    print "Length: " + str(s.length)
    print "First 10 (or at most 10) tokens:" + str(s.text[:10])

    # Create a list of the top 10 (or at most 10) frequent words in the text,
    # most frequent first, and describe both their count and percentage
    freq_sorted_words = []
    for w in s.unigram_counts:
        freq_sorted_words.append([w,s.unigram_counts[w]])
    sort_weighted_list(freq_sorted_words)
    print "First 10 (or at most 10) most frequent word-types: count and percentage: "
    for weighted_word in freq_sorted_words[:10]:
        count = weighted_word[1]

        # To avoid overly-long code lines, build up printout bit by bit
        printout = '\t' + weighted_word[0] + str(": ")
        printout += str(count)  + " ("
        printout += str(round(100.0*count/s.length, 2))
        printout += "%)"
        print printout

    most_freq_word = freq_sorted_words[0][0]
    print "First <=10 items in entry in bigram dictionary for most frequent word-type, " + \
        most_freq_word + \
        ": " + str(s.bigram_dict[freq_sorted_words[0][0]][:10])

    print "<=10 random entries in trigram dictionary: "
    for c in range(9):
        key = random.choice(s.trigram_dict.keys())
        print "\tkey: " + str(key)
        print "\tvalue: " + str(s.trigram_dict[key])

