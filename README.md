# Crimes & Punishments: The Federal Crime App 

## An Interactive Visualization Tool for Federal Offender & Sentencing Data 

The Fed Criminals App offers insight into larger trends and patterns in the people and kinds of federal crimes tried in the Southern District of New York. One of the most influential and active federal district courts in the country, the SDNY has jurisdiction over New York's major financial centers and has also tried major mafia and terrorism cases. Cases brought by SDNY prosecutors include those against Bernie Madoff, John Gotti and Michael Cohen. Apart from press coverage of such high profile cases, the general public has had little access to comprehensive data about federal offenders and the crimes they commit. The Fed Criminals App seeks to address that lack of information through several easy to use chart apps that present data in an accessible and interactive way.

In order to use this app, please clone this repository and then run the app in the terminal with the command "python OffenseChart.py". Then visit http:127.0.0.1:8050/ in your web browser. If this command does not work from your location, you can try "python Project/both.py".

Once you run the app, the first interactive chart at the top of the screen allows users to choose two crime types from 32 options in two drop down menus, and then compare the age and number of dependents of offenders on the selected crimes. Arrows on the keyboard enable users to scroll through the offense options in the drop down menus. 

![Add image](https://raw.githubusercontent.com/drs22Col/FedSentencing/master/Images/Dropdown.png)

Say you pick Firearms and Racketeering/Exortion, for example. If you hover over any dot on the chart, you will see two numbers in parentheses followed by another number, such as: ```(30, 4) 3.``` In this case, that would mean that there are 3 offenders who are 30 years old and have 4 dependents. 

![Add image](https://raw.githubusercontent.com/drs22Col/FedSentencing/master/Images/OffenseChart.png)

Such visualizations make results easy to grasp: gamblers don't tend to have kids, whereas racketeers do, for example. The number and spread of the dots also quickly provide a visual picture of how prevalent a certain offense is in the Southern District. The darker the dot, the greater the number of a particular confluence of age and dependents. Here is another view, this time for embezzlers and drug traffickers (compared to the earlier pair, there are more, and they tend to have fewer kids). 

![Add image](https://raw.githubusercontent.com/drs22Col/FedSentencing/master/Images/Embezz.png)

One might also pair up white collar crime vs blue collar crime, etc. 

A second chart below the first one uses the dimension of color to convey information along the x and y axis in a way that is intergrated with a hover function. If you click on the colored dot in the legend, dots of that color will disappear from the chart; click again and that color will appear. You can thus isolate particular elements. 

The minimum number of months served spans the x axis, while along the y axis is the number of dependents of the offender. The age of the offender is revealed through the color of the dots. 

![Add image](https://raw.githubusercontent.com/drs22Col/FedSentencing/master/Images/DependMin.png)
Type "python DependentsMinSentence.py" in terminal, then refresh your browser. 

Another version switches dependent number and age. 

![Add image](https://raw.githubusercontent.com/drs22Col/FedSentencing/master/Images/AgeMin.png)
To see this chart app (which has a hover function), type "python AgeMinSentence.py" in terminal and go to http:127.0.0.1:8050/ in your web browser.

I also created an app that focused on whether or not a sentence was within the recommended sentencing guidelines set up by Congress in 1994; it shows whether the offender has a criminal history, and what the length of their sentence was in months. To run this app, type "python GuidelinesChart.py" in your terminal.

The relation to the Guidelines is color-coded, and here are the relevant keys:  

Relation to Guidelines:
- 0= Within Range (the judge imposed a sentence within the range recommended by the Guidelines)
- 1= Above Departure (the judge imposed a sentence higher than the top of the range recommended by the Guidelines)
- 2= Government Sponsored (the prosecutor recommended a sentence outside the Guidelines)
- 3= Below Range (the judge imposed a sentence lower than the minimum recommended by the Guidelines)

Criminal History: 
- 0 = No Criminal History
- 1 = Yes, there is Criminal History

![Add image](https://raw.githubusercontent.com/drs22Col/FedSentencing/master/Images/GuidelinesTotal.png)

As you can see from the chart, most judges in the Southern District set sentences within the recommended guideline range (green). Hovering over the dots, the first number gives you the number of months of the sentence.

If we isolate the red dots, we see that judges only gave offenders with criminal historys sentences that were above the suggested guideline range.

![Add image](https://raw.githubusercontent.com/drs22Col/FedSentencing/master/Images/PartialRed.png)

And government-sponsored departures from the recommended guidelines for sentences greater than 92 months (almost 8 years) applied only to offenders with a criminal history.

![Add image](https://raw.githubusercontent.com/drs22Col/FedSentencing/master/Images/PartialBlue.png)


### BACKGROUND 

The Federal Courts handle between 75,000 and 105,000 cases a year. That's a relatively small number: there are more than 8 million state property crimes alone every year. Federal cases tend to be of larger significance. The Constitution or federal law has been violated, the US is a party, federal land is involved or state lines have been crossed. Federal proescutors select the cases. The most common offenses: drug trafficking, immigration, firearms and fraud. 

SDNY prosecutors often maintain a high profile, and have gone on to become governors, Supreme Court justices and even Nobel laureates; famous alums include Rudolph Guliani and Mary Jo White.  

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

![Add image](https://raw.githubusercontent.com/drs22Col/FedSentencing/master/Images/Cohen.png)

### PROBLEM ADDRESSED

Although federal crimes are of great public interest and are often covered in the press, it is hard to access and manipulate all the data on them that the United States Federal Sentencing Commission (USSC) collects. Larger trends are therefore harder to see. While the data files are available on the USSC website, they are very hard to access unless you have SPSS, and even then these are enormous files that require a lot of computing firepower to examine. Yet the vast range and scope of the data would make data visualization tools and statistical analysis especially useful. 

This project began with the goal of creating a library that could be run in Jupyter Notebooks to expose larger trends on a host of variables, everything from offender demographics to national distribution of offense type to differences between districts and the sentences they tend to impose. One particular question of interest was how judicial and prosecutorial practices changed after the seminal 2005 Supreme Court ruling "United States vs Booker." This ruling, authored by Justice Stephen Breyer, granted judges far more discretion in sentencing federal criminals, making sentencing guidelines merely advisory (recommended) rather than mandatory. The ruling is of particular importance because judicial discretion is at the heart of the justice system: justice depends on consistency in sentence for the same crime for an offender with the same criminal history, no matter in what state the offender is sentenced. 

As a prototype for this larger project, I have started out by focusing on one of the 94 federal court districts, the Southern District of NY (the focus of this app). 

### PROCESS 

I began by downloading 16 pairs of dat and spss files (32 total files) that covered 16 years of federal sentencing data from the USSC website, separated into the variable headings and the actual data. I opened the files in SPSS, a statistical software program, which I used to combine the pairs into a total of 16 complete sav files for each year. In order to manipulate this data in Python, I had to convert the sav files into csv format. While there does not appear to be a straightforward way to do this in Python, a library in R came to the rescue. Here's the straightforward R code I used:  

```install.packages('foreign') library(foreign)```

```dataset1 = read.spss('/path/to/file.sav', to.data.frame=TRUE)```

```write.csv(dataset1, file='/home/dsetton/dataset1.csv')```

However, these datasets were so enormous -- 2017 alone is 3.8GB -- that opening just one crashed my Excel and was taking forever to load in Jupyter Notebooks. I was able to download another year in csv format from a University of Michigan website. This file was 1.8 gigabytes. However as I examined the data in Pandas, I discovered that many variables listed in the Codebook were mysteriously missing. Eventually I realized that the University of Michigan had split these behemoths into two mini-behemoths. 

### Data Prep

I worked in a Jupyter Notebook to combine the two datafiles:   

![Add image](https://raw.githubusercontent.com/drs22Col/FedSentencing/master/Images/Col1Code.png)
![Add image](https://raw.githubusercontent.com/drs22Col/FedSentencing/master/Images/Col2Code.png)

Then I renamed some of the variables to make them more user-friendly:
![Add image](https://raw.githubusercontent.com/drs22Col/FedSentencing/master/Images/RenameCode.png)

When I checked the datatypes, I found that Python had read in a few as int64 and the rest as objects, even though the Codebook said the data was numeric. And I had to get rid of the blanks in the data, which I did using vim on the terminal, with the following command that replaced all spaces with a -999 (the g stands for global): 

```:%s/ /-999/g```

I subsetted the data to just focus on the Southern District of NY:
 ```(df.loc[df['CIRCDIST'] == 8]).to_csv("/Users/DSetton/Desktop/NYSouthernDistrictData.csv",index=False)```

I also used the key from the codebook to type in the labels for all the offenses. 

I did some data exploration in Jupyter, using toyplots and pandas to make histograms, for example. The next step was to learn DASH, testing back and forth to see what different lines in their model examples accomplished in order to learn how the program worked. Underneath certain functions, one had to infer that loops were being run in Python under the hood. 

### REFLECTIONS & FUTURE DIRECTIONS

I found DASH to be an especially exciting and interactive way of presenting data that also offers the advantage of incorporating stylistic features from html and css. Because DASH isn't integrated with Jupyter Notebooks, I wrote the code in Sublime and tested on a local host, which was not as smooth a workflow as just working in Jupyter Notebooks. Right now that is the downside of DASH. 

There is certainly more to explore. A future stage of this project would allow comparison of Southern District data with other districts such as the Eastern District of NY through a slider function; and yet another version could compare stats in the Southern District over time, specifically for the past 16 years (for the current app, the dataset is 2015 sentences). I could  add statistical functionality, for example adding probabilities for the criminal history chart app, and for other binarie categories such as US Citizen and gender for different offenses. Many other variables could be explored as well. And beyond these DASH apps, it would be useful to create a heat map integrated with a US map.










