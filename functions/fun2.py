from unittest import result


def vowel_counter(sentence):
    result={}
    for vowel in 'aeiou':
        result[vowel]=sentence.lower().count(vowel)
    return result
    #special condition for calling function
if __name__=="__main__":
    msg='This is a test'
    print(vowel_counter(msg))