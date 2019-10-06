# n * (n + 1) / 2 -- total number of possible substrings

# palindrome probllem. all sub-strings that equal in cluding x,xx,xxxx and all substrings where left and right are of equal number of chracters and are the same characters
def substrCount(n, s):
    tot = 0
    count_sequence = 0
    prev = ''
    for i,v in enumerate(s):
        # first increase counter for all seperate characters
        count_sequence += 1
        if i and (prev != v):
            # if this is not the first char in the string 
            # and it is not same as previous char, 
            # we should check for sequence x.x, xx.xx, xxx.xxx etc
            # and we know it cant be longer on the right side than
            # the sequence we already found on the left side.
            j = 1
            while ((i-j) >= 0) and ((i+j) < len(s)) and j <= count_sequence:
                # make sure the chars to the right and left are equal
                # to the char in the previous found squence
                if s[i-j] == prev == s[i+j]:
                    # if so increase total score and step one step further out
                    tot += 1
                    j += 1
                else:
                    # no need to loop any further if this loop did 
                    # not find an x.x  pattern
                    break
            #if the current char is different from previous, reset counter to 1
            count_sequence = 1  
        tot += count_sequence            
        prev = v
    return tot    
s = 'acddfdfd'
c = [1,2,3,6,7,8]
#print(enumerate(s))

for i,char in enumerate(c):
    print(char)