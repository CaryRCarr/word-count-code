# word-count-code
Simple Python code for counting the number of times certain words appear in a text file.

This code uses system arguments, as listed below.

Steps for use:
When testing the functionality for finding the top three most common words, run the code using the following set-up:
wordcount.py [Convert to Lower Case: True/False] [Path to Text File]

The first system argument will convert all words to lower-case if true, allowing for identical words in different cases to be counted as a single word. The second argument will be taken as the path to the text file in question. So long as no key word is provided as a third argument, then the code will automatically return the top three most common words.

When testing the functionality for finding the number of times a given word shows up in the file, run the code using the following set-up:
wordcount.py [Convert to Lower Case: True/False] [Path to Text File] [Word To Be Found]

As with the top three most common words, the first system argument will convert all words, including the word being searched for, to lower-case if true, allowing for identical words in different cases to be counted as a single word. The second argument will be taken as the path to the text file in question, and the third argument will be the word to be counted in the file.

As an example, running the command "wordcount.py True frankenstein.txt" would run the file, finding the three most common words in the frankenstein.txt file, without regard for the case of the different words.

Example:
```
>>>>> python wordcount.py True frankenstein.txt
The top three words in this file are 'the', 'and', and 'i'.
```

As a second example, running the command "wordcount.py False frankenstein.txt Frankenstein" would run the file to find the number of times that 'Frankenstein' appeared in the frankenstein.txt file, and it would only consider the word 'Frankenstein' with that exact casing.

Example 2:
```
>>>>> python wordcount.py False frankenstein.txt Frankenstein
The word 'Frankenstein' appears a total of 28 time(s) in the file.
```
