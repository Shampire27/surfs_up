# surfs_up

Module 9 - SQL - Advanced Data Storage and Retrieval

In this Module, SQLite is used for a smaller, faster and no users database which could lives on a computer or phone.  SQLAlchemy, as the query tool for SQLite, is used for statistical analysis with data frame analysis.  Flask, as the web framework, is used to write in Python to build web pages.

## **Overview of the statistical analysis**

There is a business plan for a Surf n' Shake Shop which aimes for serving surf sports and ice creams to the locals and tourists.  For funding purpose, a weather analysis on the weather for the business plan was required by the investor, W. Avy.

By using SQLite and SQLAlchemy, percipitation analysis and weather station analysis was created. Moreover, a climate appp was built with Flask.

Additionally, two technical analysis about temperature trends was required before opening the surf shop, in order to determine if the surf and ice cream shop business is sustainable year-round:
- Deliverable 1: Determine the Summary Statistics for June
- Deliverable 2: Determine the Summary Statistics for December

In the analysis, the main tools uesd for coding was Jupyter Nootbook and Visual Studio Code.


## **Results**

In the two deliverables, the weather statistics summary shows as below:

***Summary Statistics for June***

[Summary Statistics for June](Analysis/Summary_Statistics_for_June.png)


***Summary Statistics for December***

[Summary Statistics for December](Analysis/Summary_Statistics_for_December.png)

According the the results, there are three key diferences in weather between June and December:

1. In Decmber, the temperature difference is 27 (=83-56) which was significant larger than June 21 (=85-64).  Meanwile the difference on standard diviation results also shows the same result. The larger standard diviation means the larger temperature diferences. The larger temperature diferrence may caused unstable profitability for the ice cream selling.

2. The lowest temperature in June was 64F but for December is 56F, the 8F diferences means in December the weather could be much colder than in June. The lower min temp will cause a decrease on the needs of surfing and ice cream service because of the feeling on the waether by consumers.

3. Based on the quartiles results, the overall temperature in December decrease more significantly.  If most people feels cold under 70F, there is about 25% more opportunities that people feeling cold in December, bacause there are about 50% weather counts in December are under 70F and less than 25% counts in June.

## **Summary**

Based on the results the overall temperature in December is lower than in June.  If set 70F as the comfort temperature for people to get surf and ice cream service, there is about 25% opportunities on the total temperatures that in December would be more unsuitable to maintain serving than in June.  As a result, the weather in December may not suitable for profitable purpose if opening a Surf n' Shake Shop.  Further analysis on the seasonally revenue and expenses on similar industrial reports could be analyzed to determine the profitability of this business plan.
