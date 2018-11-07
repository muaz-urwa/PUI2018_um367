# HW8_um367


## Assigment 1

#### Data Source: 
I used the the text data from Principles of Urban Informatics 2018 lecture slides. This course has and its materials definitely have undeniable urban relevance. 

print("Principles of Urban Informatics".contains('Urban'))
###True

I retrieved the pdfs in a reproducible way from the web and parsed them to extract text using PyPDF2. Text was preprocessed and tokenized and then top 25 most frequent words were selected. I decided to visualize the distribution and occurence of these terms through out the course so far. For that I created a lexical dispersion plot of these terms, which shows there distribution in the corpus by plotting there occurence offsetted from the start of corpus. Corpus here is the raw text from all lectures concatenated in order of the lectures. NLTK library had a lexical dispersion plot but it was monochromatic and dull so I downloaded the source code function and modified it to color the bars by the lecture they correspond to (with an assumption that all the lectures roughly have same length.)

### Image 1
![screen shot 1](LexicalDispersion.png)


This repository contains home work 3 deliverables for my class of PUI 2018.

The screen shots of the homework assignment are embedded below:




### Image 2
![screen shot 1](https://raw.githubusercontent.com/muaz-urwa/PUI2018_um367/master//HW3_um367/Screenshot%20from%202018-09-26%2021-50-06.png)

### Image 3
![screen shot 1](https://raw.githubusercontent.com/muaz-urwa/PUI2018_um367/master//HW3_um367/Screenshot%20from%202018-09-26%2021-50-58.png)
