from string import punctuation

def remove_punc(text):
    '''Remove punctuations from a text and return cleaned text
    -> clean_Text=remove_punc(text)
    '''


    for punc in punctuation:
        # print(punc)
        text=text.replace(punc,'')
    return text

if __name__=='__main__':
     msg='_@#this is a (*!)(@#) is) a) string)'
     cln_text=remove_punc(msg)
     print('orignal: ',msg)
     print('cleaned: ',cln_text)


    #wap to replace all the multiple spaces in a single space