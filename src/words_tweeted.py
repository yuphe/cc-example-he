def num_times_word_tweeted(fin,fout):

    """function that calculates the total number of 
       times each word has been tweeted.

       Keyword arguments:
 
       fin -- input file
       fout-- output file

       return: fout
    """ 
    try:
        import numpy as np
    except ImportError:
        np=None

    from collections import Counter

    words_tweeted = []

    # open input file
    # read each tweet from file
    # append splitted words to the list of words_tweeted

    with open(fin, 'r') as f1:

        for line in f1.readlines():
            words_tweeted.append(line.split()) 


    # open output file
    # count the number of times word appears
    # sort it according to ASCII Code
    # write it to output file

    with open(fout,'w') as f2: 

        # check numpy package
        if np:

            num_times=Counter(np.hstack(words_tweeted)) 
            num_times=sorted(num_times.iteritems())    
            f2.writelines('%-30s %s\n' % x for x in num_times)

        else:

            print "function 'num_times_word_tweeted' needs numpy package"


#check if this module is executed directly
if __name__ == '__main__':
    
    import sys
  
    f1,f2 = sys.argv[1], sys.argv[2]

    # call function
    num_times_word_tweeted(f1,f2)

