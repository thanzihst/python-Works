text="abbbbc"
# i,left,right,longest_palindrome,current_palindrome
longest_palindrome=""

for i in range(0,len(text)):

    left=i

    right=i

    while(left>=0 and right<len(text) and text[left] == text[right]):

        current_palindrome_text=text[left:right+1]

        if len(current_palindrome_text) > len(longest_palindrome):

            longest_palindrome=current_palindrome_text
        
        left=left-1

        right=right+1
    
    left=i

    right=i+1

    while(left>=0 and right<len(text) and text[left] == text[right]):

        current_palindrome_text=text[left:right+1]

        if len(current_palindrome_text) > len(longest_palindrome):

            longest_palindrome=current_palindrome_text
        
        left=left-1

        right=right+1
    

print(longest_palindrome)



# collection type
# list
# tuple
# set
# dictionary




