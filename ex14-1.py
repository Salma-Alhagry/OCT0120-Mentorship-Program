# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 00:38:16 2020

@author: Ouso
"""

'''
Exercise 14-1.
Write a function called sed that takes as arguments a pattern string, 
a replacement string, and two filenames; it should read the first file 
and write the contents into the second file (creating it if necessary). 
If the pattern string appears anywhere in the file,
it should be replaced with the replacement string.
If an error occurs while opening, reading, writing or closing files,
your program should catch the exception, print an error message, and exit.
'''
def sed(pat_str, rep_str, f1, f2):
    ''' A function that replaces string from input file with another in output
    file.
    pat_str: the string to be replaced
    rep_str: the replacing string
    f1: the file to be read and parsed for pat_str
    f2: the new output file created to save the replacement pattern
    '''    
    try:
    f_read= open(f1,'r')
    f_write = open(f2,'w')
    for line in f_read:
        if pat_str.lower() in line.lower():
            idx= line.lower().find(pat_str.lower())
            b = line[:idx]+\
            line[idx: idx+len(pat_str)].lower().replace(pat_str.lower(),\
                rep_str)+line[idx+len(pat_str):]
            f_write.write(b)
        else:
            f_write.write(line)
    f_read.close()
    f_write.close()    
        
    except:
        print('something went wrong')
        