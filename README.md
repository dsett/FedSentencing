# FedSentencing -- Judging the Federal Courts // Who are Federal Defendants? 


The Federal Courts handle between 75,000 and 100,000 cases a year, far fewer than the millions of annual state crimes. But federal cases are special ones that the prosecutors have selected, ones where the Constituion has been violated, the US is a party, state lines are crossed, tktktk The most common types are drugs, immigration tk and tk. These are often high profile cases of great public interest, everything from the Gambino crime boss family trial to Michael Cohen's particular contributions'. 

Although the USSC collects a lot of data about these cases, it is not easily accessible to the general public, nor can it be manipulated easily. 

This project began with the goal of creating a library where people could gain insight into federal sentencing practices, the distribtion of cases throhgout the country. And also, they could learn about how praactices chnaged aafter the 2005 Supreme Court ruling United States vs Booker which granted judges almost unfettered discretion in sentencing federal criminals. This is an issue fundamental to the justice system, since cwithout consistncy from court to court, there can be no justice and confidence in the judicial system would suffer. 

As a prototype for this larger project, I have started out by focusing on one of the 94 districts,  the 
The Southern District of NY wprobably the best known one. Top lawyers have used it as a stepping stone to become mayor, governor and Supreme Court Justices. Famous alums include tktktkt t t t tkttktkktktkt .   famous cases are tried here .... Michael Cohen, tktktktktktktk. 

This project gives people insight into the people and kinds of crimes tried in the Sourthern District, offering intereactive charts that along people to dig deep into the data. Because the SOuther District includes the financial centers in NY, in some ways its cases are going to be different than other districts. Another stage of this project will allow comparison with other districts 

###H3 PROCESS 

Initially I had to get the dat and spss files for 16 years of federal sentencing data changed into sav files. I found a libarary in R to do the trick. Here's the code:  

```install.packages('foreign') library(foreign)

dataset1 = read.spss('/path/to/file.sav', to.data.frame=TRUE)

write.csv(dataset1, file='/home/dsetton/dataset1.csv')```

However, the datasets were so enormous -- 2017 alone is 3.8GB -- that I decided to start off looking at one year.  many variables listed in the Codebook were missing. I eventually realized the data for each year had been divided into two . 

DATA PREP 

image: how the dataset was created through pulling columns from both

Image: renaming columns

getting rid of blanks to turn everythng into ints64 and floats

###H3RESEARCH 
The Southern District: "The Southern District is one of the most influential and active federal district courts in the United States, largely because of its jurisdiction over New York's major financial centers.""

"go to the best law schools and clerked for federal judges, Lemann writes. And, since the office is in the heart of New York City, they get to go after high rollers on Wall Street and mobsters. "This gives them macho points in addition to their academic credentials," Lemann writes.



###H3DATA EXPLORATION

Image: Dash Table 

Images: Histograms of age, race, etc. 

###H3DASH CHART NUMBER 1

IMAGE TK

###H3 Some famous Southern District Cases:

- The injury and loss of life claims from the sinking of the Titanic
- The espionage trial of Julius and Ethel Rosenberg a
- perjury trial of Alger Hiss  
- Obscenity case against James Joyce’s Ulysses
- the Pentagon Papers. 
- John Mitchell of the Watergate era tried there (he was acquitted.

- Financial frauds: Bernard Madoff, Ivan Boesky and Michael Milken.

-  1998 US embassy bombings in East Africa-  those alleged to have been responsible for the 1993 World Trade Center bombing
 - Omar Abdel Rahman (“The Blind Sheikh")"
  -- Abduwali Muse, the so-called Somali Pirate, 
- criminal cases against Bess Myerson, Leona Helmsley and Martha Stewart, Imelda Marcos.

-  Deflategate controversy concerning NFL's Tom Brady  


What it does 

Conclusions from this data 

###H3 DASH CHART NUMBER 2

IMAGE TK 

What it does 

Conclusions from this data 

###H3 DASH HISTOGRAMS 





###H3REFLECTIONS 

Became more familiar with Numpy and Pandas, and some of the steps one needs to take in preparing data. I  learned how to use DASH, 


Although I didn't get to the animated part because data took so much longer than I expected, I did read up on on ways t.. 

Because DASH isn't integrated with Jupyter Notebooks, I wrote the code in Sublime and tested in a local host, which was not as smooth a workflow.  

On the other hand, one strength of DASH --  besides its interactive features defined as core components -- is that it is integrated with html and Markdown, so I realized I could build a website around it relatively simply. 

