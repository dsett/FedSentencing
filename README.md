# Crimes & Punishments: The Federal Criminal App 

## An Interactive Visualization Tool for Federal Offender & Sentencing Data 


This python app gives people insight into the nature of the people and kinds of crimes tried in the Southern District of New York, the high profile federal court whose prosecutors have gone on to become mayors, governors, Supreme Court justices and even Nobel laureates. One of the most influential and active federal district courts in the country, the SDNY has jurisdiction over New York's major financial centers, not to mention trying mobster bosses like Gambino and Gotti.  The Fed Criminals App allows users to choose two crime types from 32 options in drop menues, and then compare the age and number of dependents of offenders on the selected crimes. If you hover over any dot on the chart, you see three pieces of data: tk tk and tk. Some results: gamblers don't tend to have kids, whereas tk do; drug traffickers tk and tk. 

![Add image](https://raw.githubusercontent.com/drs22/FedSentencing/master/Images/Chart2.png)


A second chart uses the dimension of color as well as an x and y axis and a hover function . This time, the colors show aht. 


TK LOOKS LIKE THIS


In order to use these apps yourself, please clone this repository and then run Chart3.py and Chart2.py from terminal by using the commands "python Chart3.py" and "python Chart3.py". Then open your browser and go to the local host address ttkktktk addresss. 


 Another stage of this project will allow comparison of Southern District data with other districts like the Eastern District of NY through a slider function; and yet another version will compare stats in the Southern District over time, specificallt for the past 16 years (for the current app, the dataset is 2015 sentences). In the future I also plan to embed this tool, and others, in a website.  


### BACKGROUND 

The Federal Courts handle between 75,000 and 105,000 cases a year. That's a relatively small number: there are more than 8 million state property crimes alone every year. Federal cases tend to be of larger significance. The Constitution or federal law has been violated, the US is a party, federal land is involved or state lines have been crossed. Federal proescutors select the cases. The most common offenses: drug trafficking, immigration, firearms and fraud. 

### Some famous Southern District of NY Cases:

- Injury and loss of life claims from sinking of the Titanic
- Espionage trial of Julius and Ethel Rosenberg  
- Perjury trial of Alger Hiss  
- Obscenity case against James Joyce’s Ulysses
- Right to publish the Pentagon Papers
- Trying Watergate's John Mitchell  
- Big fraud cases: Bernard Madoff, Ivan Boesky and Michael Milken
- International terrorism: 1998 US embassy bombings in East Africa, 1993 World Trade Center bombing, Omar Abdel Rahman (“The Blind Sheikh")
- White collar crime: Bess Myerson, Leona Helmsley Martha Stewart


And more recently, Trump's lawyer Michael Cohen, and the Deflategate controversy concerning NFL's Tom Brady  


IMAGE01-Cohen&CO 

### Problem to Solve

Although federal crimes are of great public interest and are often covered in the press, it is hard to access and manipulate all the data on them that the United States Federal Sentencing Commission (USSC) collects. Thus the larger trends are harder to see. While the data files are available on the USSC website, they are very hard to access unless you have spss, and even then these are enormous files that require a lot of computing firepower to examine. Yet the vast range and scope of the data would make data visualization tools and statistical analysis especially useful. 

This project began with the goal of creating a library that could be run in Jupyter Notebooks in which people could gain insight into the data to expose larger trends on a host of variables, everything from demographics to national distribution of offense type to differences between districts and the sentences they tend to impose. One particular question of interest was to examine how judicial and prosecutorial practices chnaged after the profoundly important 2005 Supreme Court ruling "United States vs Booker." This ruling, authored by Stephen Breyer, granted judges far more discretion in sentencing federal criminals, making sentencing guidelines merely advisory (recommended) rather than mandatory. Judicial discretion is at the heart of the justice system, since justice depends on consistency in sentence for the same crime from court to court. (Almost all federal cases are settled through a plea agreement that recommends a specific sentence that the judge may or may not sign off on.)

As a prototype for this larger project, I have started out by focusing on one of the 94 districts,  the 
The Southern District of NY wprobably the best known one. Top lawyers have used it as a stepping stone to become mayor, governor and Supreme Court Justices. Famous alums include tktktkt t t t tkttktkktktkt .   famous cases are tried here .... Michael Cohen, tktktktktktktk. 


### PROCESS 

I began by downloading 16 pairs of dat and spss files (32 total files) that covered 16 years of federal sentencing data from the USSC website, separated into the variable headings and the actual data. I opened the files in spss, a statistical software program, which I used to combine the pairs into a total of 16 complete sav files for each year. In order to manipulate this data in python, I had to convert the sav files into csv format. While there does not appear to be a straightforward way to do this in Python, a library in R came to the rescue. Here's the R code I used:  

```install.packages('foreign') library(foreign)```

```dataset1 = read.spss('/path/to/file.sav', to.data.frame=TRUE)```

```write.csv(dataset1, file='/home/dsetton/dataset1.csv')```

However, these datasets were so enormous -- 2017 alone is 3.8GB -- that opening just one crashed my Excel and was taking forever to load in Jupyter Notebooks. I was able to download another year in csv format from a University of Michigan website. This file was 1.8 gigabytes. However as I examined the data in Pandas, I discovered that many variables listed in the Codebook were mysteriously missing. Eventually I realized that the University of Michigan had split these behemoths into two mini-behemoths. 


### DATA PREP 

I worked in a Jupyter Notebook to subset the data, rename columns and clean the data: 

![Add image](https://raw.githubusercontent.com/drs22/FedSentencing/master/Images/Col1Code.png)
![Add image](https://raw.githubusercontent.com/drs22/FedSentencing/master/Images/Col2Code.png)

![Add image](https://raw.githubusercontent.com/drs22/FedSentencing/master/Images/RenameCode.png)


When I checked the datatypes, I found that python had read in a few as int64 and the rest as objects, even though the Codebook said the data was numeric. I realized I had to get rid of the blanks in the data, which I did using vim on the terminal, with the following command that replaced all spaces with a -999 (the g stands for global): 


```:%s/ /-999/g```

### DATA EXPLORATION

I ran a dash Table, but I decided I preferred to look over my data in Excel. 

Imagetk : Dash Table 

Then I did some data exploration in Jupyter, using toyplots and pandas. For example: 

![Add image](https://raw.githubusercontent.com/drs22/FedSentencing/master/Images/Age.png)

![Add image](https://raw.githubusercontent.com/drs22/FedSentencing/master/Images/Dependents.png)

Histograms of age, race, etc. 


### REFLECTIONS 

Through this project, I became more familiar with Numpy and Pandas, different data formats (sav, spss, txt, ASCII, etc), and how to prepare and clean data. That was the first half of the project. The second half involved teaching myself how to use DASH, which I found to be an espcially exciting and interactive way of presenting data that also has the advantage of incorporating stylistic features from html and css. Because DASH isn't integrated with Jupyter Notebooks, I wrote the code in Sublime and tested in a local host, which was not as smooth a workflow. Right now that is the downside of DASH. 

Although I have not yet gotten to that stage, from the preliminary research and working sketches I developed in Photoshop, I gained a bigger picture sense of how to fit different components together in a website. And I gained a greater appreciation of the flexibility of python, and the vast array of tools that are built with it as a base (in comparison to say R, which is more exclusively stats focused). 





