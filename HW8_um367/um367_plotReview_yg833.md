## Assignment 1: Review of Urwa's Plot Assignment from HW8
yg833

This is a peer review of my colleague Urwa's plot assignment from [homework 8](https://github.com/meiguan/PUI2018_um367/tree/master/HW8_um367)

Urwa provided a very detailed and thorough description of his idea and the process for the data wrangling and production of the resultant plots. I really appreciated how detailed Urwa was and how his readme file and jupyter notebook clearly walked me through his thinking. Urwa used the analysed the text from the slides from our [2018 Principals of Urban Informatics course.](https://github.com/fedhere/UInotebooks) and created 3 plots as rendered below:

### Plot 1: Lexical Dispersion of 25 Most common Words in PUI Slides

![um367_LexicalDispersionplot](../HW8_um367/LexicalDispersion.png)

### Plot 2: Frequency Distribution 25 common Words in PUI Slides

![um367_LexicalDispersionplot](../HW8_um367/freq.png)

### Plot 3: Sentiment Analysis PUI Slides

![um367_sentimentplot](../HW8_um367/sentiment.png)

For each of the plots, I appreciated how it was trying to communicate 1 idea and the presentation was clean (no clutter). I also liked the detailed descriptions of the plots in the narrative. Below are my notes for each of the plots from my colleague:

- For the 1<sup>st</sup> plot, the plot description/ caption helped me understand what exactly it was that I was looking at. Since the Y Axis was not labeled, the caption help me understand that the plot was showing the 25 most common words and it was ordered from most common to least from top to bottom on the y-axis. 

- For the 2<sup>nd</sup> plot, it is a clear line graph that depicts the frequency of the 25 commonly appeared words. And it immediately highlighted how much more the word "data" appeared in the slides than anything other word.

- For the 3<sup>rd</sup> plot, this is a bar graph of lectures vs the average sentence sentiment score which was calculated using vader_lexicon package in NLTK with scores ranging from -1 (very negative) to 1 (very postive). I like how this plot adds a different flavor to the overall analysis to assess the "sentiments" of the course content. 

Urwa's idea to assess PUI lecture slides is fun and I enjoyed reading this analysis. For plot 1, I think the graphic is definitely intriguing and I was motivated to really understand it. I wished there was an overlay of a legend to tell me what the colors mean or correspond to. And I would like to have seen a y-axis label. I think for the future it maybe worthwhile to pick clearer axis labels. For example in plot 2, the x-axis was labeled as "Samples". It could be helpful to have something more descriptive. For 3rd plot showing sentiment, while the numeric values are close to "0" and the take-away is that course content is fairly neutral, the way that the y-axis scale is way zoomed-in could mis-lead this take-away. 

