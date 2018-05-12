# Crimes & Punishments: The Federal Crime App 

## An Interactive Visualization Tool for Federal Offender & Sentencing Data 


The Fed Criminals App offers insight into larger trends and patterns in the people and kinds of crimes tried in the Southern District of New York. One of the most influential and active federal district courts in the country, the SDNY has jurisdiction over New York's major financial centers, not to mention multiple big mobster cases. SDNY prosecutors often maintain a high profile, and have gone on to become governors, Supreme Court justices and even Nobel laureates; famous alums include Rudolph Guliani and Mary Jo White.   

The Fed Criminals App allows users to choose two crime types from 32 options in drop menus, and then compare the age and number of dependents of offenders on the selected crimes. Use the arrows on your keyboard to scroll through the offense options in the drop down menus. Say you pick Firearms and Racketeering/Exortion. If you hover over any dot on the chart, you will see two numbers in parentheses followed by another number, such as this: ```(30, 4) 3.``` In this case that would mean that there are 3 offenders who are 30 year old and have 4 dependents. 

![Add image](https://raw.githubusercontent.com/drs22Col/FedSentencing/master/Images/Chart3.png)

Some results: gamblers don't tend to have kids, whereas racketeers do. The number and spread of the dots also quickly gives you a visual picture of how prevalent a certain offense is in the Southern District. The darker the dot, the greater the number of a particular confluence of age and dependents. 

In order to use this app yourself, please clone this repository and then run the app in the terminal with the command "python Chart3.py". Then visit http:127.0.0.1:8050/ in your web browser. You will see something that looks like the image above.  

A second app uses the dimension of color to convey information as well as data along the x and y axis, and a hover data function. The 0 on the horizontal axis indicates that a sentence is within the recommended sentencing guidelines set up by Congress in 1994. 

0= Within Range (the judge imposed a sentence within the range recommended by the guidelines)
1= Above Departure (the judge imposed a sentence higher than the top of the range recommended by the guidelines)
2= Government Sponsored (The prosecutor recommended a sentence outside the guidelines)
3= Below Range (the judge imposed a sentence lower than the minimum recommended by the guidelines)

![Add image](https://raw.githubusercontent.com/drs22Col/FedSentencing/master/Images/Chart2.png)

As you can see from the chart, most judges in the Southern District set sentences within the guideline range.
And the higher the sentence the more likely it is to be outside that range. 

To see this second visualization, type "python Chart2.py" in your terminal and then refresh your local host at the same address listed above, http:127.0.0.1:8050/  Then you should see something like this: 


Hover over the dots for more case-specific information. 

A future stage of this project will allow comparison of Southern District data with other districts such as the Eastern District of NY through a slider function; and yet another version will compare stats in the Southern District over time, specifically for the past 16 years (for the current app, the dataset is 2015 sentences). In the future I also plan to embed this tool, and others, in a website.  


### BACKGROUND 

The Federal Courts handle between 75,000 and 105,000 cases a year. That's a relatively small number: there are more than 8 million state property crimes alone every year. Federal cases tend to be of larger significance. The Constitution or federal law has been violated, the US is a party, federal land is involved or state lines have been crossed. Federal proescutors select the cases. The most common offenses: drug trafficking, immigration, firearms and fraud. 

SDNY prosecutors often maintain a high profile, and have gone on to become governors, Supreme Court justices and even Nobel laureates. Notable alums include Rudolph Guliani and Mary Jo White. 

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

Although federal crimes are of great public interest and are often covered in the press, it is hard to access and manipulate all the data on them that the United States Federal Sentencing Commission (USSC) collects. Larger trends are therefore harder to see. While the data files are available on the USSC website, they are very hard to access unless you have spss, and even then these are enormous files that require a lot of computing firepower to examine. Yet the vast range and scope of the data would make data visualization tools and statistical analysis especially useful. 

This project began with the goal of creating a library that could be run in Jupyter Notebooks to expose larger trends on a host of variables, everything from demographics to national distribution of offense type to differences between districts and the sentences they tend to impose. One particular question of interest was how judicial and prosecutorial practices changed after the profoundly important 2005 Supreme Court ruling "United States vs Booker." This ruling, authored by Justice Stephen Breyer, granted judges far more discretion in sentencing federal criminals, making sentencing guidelines merely advisory (recommended) rather than mandatory. Judicial discretion is at the heart of the justice system, since justice depends on consistency in sentence for the same crime (with the same criminal history) from court to court.  

As a prototype for this larger project, I have started out by focusing on one of the 94 federal court districts, the Southern District of NY.


### PROCESS 

I began by downloading 16 pairs of dat and spss files (32 total files) that covered 16 years of federal sentencing data from the USSC website, separated into the variable headings and the actual data. I opened the files in spss, a statistical software program, which I used to combine the pairs into a total of 16 complete sav files for each year. In order to manipulate this data in python, I had to convert the sav files into csv format. While there does not appear to be a straightforward way to do this in Python, a library in R came to the rescue. Here's the R code I used:  

```install.packages('foreign') library(foreign)```

```dataset1 = read.spss('/path/to/file.sav', to.data.frame=TRUE)```

```write.csv(dataset1, file='/home/dsetton/dataset1.csv')```

However, these datasets were so enormous -- 2017 alone is 3.8GB -- that opening just one crashed my Excel and was taking forever to load in Jupyter Notebooks. I was able to download another year in csv format from a University of Michigan website. This file was 1.8 gigabytes. However as I examined the data in Pandas, I discovered that many variables listed in the Codebook were mysteriously missing. Eventually I realized that the University of Michigan had split these behemoths into two mini-behemoths. 


### Data Prep

I worked in a Jupyter Notebook to subset the data, rename columns and clean the data: 

![Add image](https://raw.githubusercontent.com/drs22Col/FedSentencing/master/Images/Col1Code.png)
![Add image](https://raw.githubusercontent.com/drs22Col/FedSentencing/master/Images/Col2Code.png)

![Add image](https://raw.githubusercontent.com/drs22Col/FedSentencing/master/Images/RenameCode.png)


When I checked the datatypes, I found that python had read in a few as int64 and the rest as objects, even though the Codebook said the data was numeric. I realized I had to get rid of the blanks in the data, which I did using vim on the terminal, with the following command that replaced all spaces with a -999 (the g stands for global): 


```:%s/ /-999/g```

### Data Exploration

I first made a table of data using DASH, but I decided I preferred to look over my data in Excel, referencing the Codebook when needed. 

Then I did some data exploration in Jupyter, using toyplots and pandas. For example, these histograms: 

![Add image](https://raw.githubusercontent.com/drs22Col/FedSentencing/master/Images/Age.png)

![Add image](https://raw.githubusercontent.com/drs22Col/FedSentencing/master/Images/Dependents.png)


### REFLECTIONS 

Through this project, I became more familiar with Numpy and Pandas, different data formats (sav, spss, txt, ASCII, etc), and how to prepare and clean data. That was the first half of the project. The second half involved teaching myself how to use DASH, which I found to be an espcially exciting and interactive way of presenting data that also has the advantage of incorporating stylistic features from html and css. Because DASH isn't integrated with Jupyter Notebooks, I wrote the code in Sublime and tested in a local host, which was not as smooth a workflow. Right now that is the downside of DASH. 

Although I have not yet gotten to that stage, from the preliminary research and working sketches I developed in Photoshop, I gained a bigger picture sense of how to fit different components together in a website. And I gained a greater appreciation of the flexibility of python, and the vast array of tools that are built with it as a base (in comparison to say R, which is more exclusively stats focused). 





