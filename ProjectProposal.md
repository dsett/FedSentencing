# Python Final Project

1.	The problem: What is the problem you wish to solve? 

While the US Commission of Federal Sentencing posts periodic reports on federal sentences, testifies before Congress, and makes datasets available on their website, the data is not easily manipulatable or searchable by the general public in a way that makes significant trends visible.

Federal courts hear fewer cases than state courts but they tend to be of great importance and of public interest. The types of cases they hear are ones where the United States is a party; violations of the Constitution or federal law; crimes on federal land; and bankruptcy cases. Federal courts also hear cases based on state law that involve parties from different states. The types of high profile cases that qualify as federal include the Madoff Ponzi scheme, and cases against the bosses of organized crime bosses such as Gotti and Gambino.

While the public can be privy to the stories behind these high profile crimes in press coverage, there is no tool that allows analysis of the larger trends in federal crime and sentencing, either nationally or by state or other variables. Every year there are between 75,000 and 105,000 reported federal crimes, so the scale of data makes data visualization tools and statistical analysis especially relevant. 

2.	The data: What is the data you will analyze and where is it from? 

My data comes from the U.S. Federal Sentencing Commission, and consists of individal data sets for each fiscal year from 2002 to 2016. These data files are only SAS and SPSS compatible. The individual offender is the unit of analysis, and the variables include spatially related info, such as state, district, federal court circuit, and region of the country; demographic data such as race, age, marital status, and gender; types of crimes, such as organized crime, check kiting and child pornography; offender background, including if they do not have a criminal history; judge, prosecutor and mandatory minimum impact on sentences, such as how much circuits are deviating from standard sentencing guidelines, which mandatory minimums do or do not apply and instances where prosecutors lowered sentences due to cooperation with the government.  

Sentences are also classified as pre or post Booker, which refers to the 2005 Supreme Court ruling US vs Booker that made federal sentencing guidelines advisory rather than mandatory. 
  
3. The tools: What computational tools will you use to solve the task? 

First I need to convert the data into a format that is readable with one of the many tools available online. Then I will use Pandas to organize the data, and perhaps to filter it in certain ways, and Folium to make choropleth maps. DASH might also come in handy. The code will be organized in a python library. 
 
4.	The novelty: Why is this novel? 

As mentioned above, this project would make federal sentencing information much more accessible and interactive in a searchable, customizable way. The project could also be used to translate other similarly formatted data sets into much more accessible data in an automated way. Some design elements might also be novel, potentially through the use of p5.js animations (to be determined). 

5.	The goal: What is your envisioned product at the due date and after?

A helpful interface/tool organized in a python library that can automatically take data in an SPSS format and make it accessible, searchable and interactive, including producing custom maps, charts and tables to answer particular queries. 
