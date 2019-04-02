# a3checks.py
# Beverly Balasu bb532
# 3/28/17
# Skeleton by Lillian Lee (LJL2), March 2017

import a3
import a3given

print "Trying out creating a short sample"

s0 = a3given.sample_from_source_file('short.txt', "short")
a3given.print_summmary_stats(s0)
print

print "Combining Obama SOTU and then Bush SOTU"

olist=[]
for year in range(2013, 2016+1):
    olist.append(a3given.sample_from_source_file(str(year)+"_obama.txt", str(year)))

obama = a3.merge(olist, "Obama SOTU 2013-2016")
a3given.print_summmary_stats(obama)
print

print "\n......\n"

blist=[]
for year in range(2005, 2008+1):
    blist.append(a3given.sample_from_source_file(str(year)+"_bush.txt", str(year)))

bush = a3.merge(blist, "Bush SOTU 2005-2008")
a3given.print_summmary_stats(bush)
print

threshold = 10
title = "****"
title += "Analyzing differences between " + obama.label + " and "
title += bush.label + "****"
print title
differences = a3.diffs(obama, bush, threshold)
threshold_string = " (and at least " + str(threshold) + " times)"
print "Only said by Obama " + threshold_string + ": " + str(differences[0])
print "Only said by Bush: " + threshold_string + ": " + str(differences[1])
print "Ten most Obama-leaning joint words: " + str(differences[2][:10])
print "Ten most Bush-leaning joint words: " + str(sorted(differences[2][-10:],reverse=True))


# Generation checks

print "Trying out trigram generation for short sample"
print a3.trigram_generation(s0,100)
print


cs1110 = a3given.sample_from_source_file('2014sp_exam.txt', "CS1110 2014sp P1")

for sample in [obama, bush, cs1110]:
    print "Bigram and trigram generation according to " + sample.label
    print a3.bigram_generation(sample, 300)
    print
    print a3.trigram_generation(sample, 300)
    print
    print
