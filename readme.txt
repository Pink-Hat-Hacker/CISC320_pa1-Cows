Explaination:
    Getting and putting records in is O(n) (aka O(r)). I looped through each line
    of the records and made Cow objects for them -- adding them to a dictionary (COWS). 
    r is the number of record line rows and loop goes through each and adds it to the dictionary.
    
    To satisfy the case of 0 milks or 0 weights, I created a for loop that 
    appends all of the cow objects (> 0 MW) to a list.

    Sorting:
    Python's built in sorting function [Timsort] is O(n log(n)) https://www.educative.io/edpresso/what-is-the-python-list-sort
    which in this case is O(c log(c)), where it sorts based on the cow object attributes
    lowW (lowest weight), lateW (latestW), and average milking (avgM).

    This is all stored in a list and printed out using a for loop. This is not
    necessary, however, it does look better than a list of lists.

    So breakdown:
    - Adding to dictionary
        - O(r)
    - For loop to deal with 0 Milkings or weights
        - O(r) [aka(O(n))]
    - Sorting
        - O(c log (c)) [(aka) O(n log (n))]
    - Printing
        - O(r)
    - TOTAL = O(c log(c)) + 3 * O(r) -> [ignore constants] O(c log(c)) + O(r) -> 
        O(c log(c) + r)
    

please ignore "test.json"


Collaborators:
    Worked with and advised:
    - akumar@udel.edu / Iclyn
    - aeshak@udel.edu / Aesha
    Much of their code may look like mine due to working together
    and me helping them get started. Dictionaries was how I planned to solve
    this and that is how I was able to help them.

    Please check my github for timestamps/commits if necessary