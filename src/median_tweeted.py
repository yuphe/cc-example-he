def cal_median_num_unique(fin,fout):
    
    """ function that calculates the median number of 
        unique words of updated tweets.  
  
        Keyword arguments:
 
        fin -- input file
        fout-- output file

        return: fout
    """
    try:
        import numpy as np
    except ImportError:
        np=None

    num_words, num_median = [],[]
 
    # open input file
    # read each tweet from file
    # count the number of unique words per tweet
    # append it to the list of num_words
    # calculate the median number of list num_words
    # append it to the list of num_median
 
    with open(fin, 'r') as f1:

        # check numpy package
        if np:

            for line in f1.readlines():                 
                num_words.append(len(set(line.split()))) 
                num_median.append(np.median(num_words))  

        else:        
            print "function 'cal_median_num_unique' needs numpy package"


    # open output file
    # write the calculated median numbers to output file

    with open(fout, 'w') as f2:
    
        f2.writelines('%.2f\n' % x for x in num_median)



#check if this module is executed directly
if __name__ == '__main__':

    import sys

    f1,f2 = sys.argv[1], sys.argv[2]

    # call function
    cal_median_num_unique(f1,f2)
