# Crowdfunding for charity: data analysis using computational linguistics (NLP) methods.

The study on the material of charitable campaigns on the www.planeta.ru website, completed in years 2012-2020. 

Training research project by Elizaveta Kadetova
Moscow Higher School of Economics, 2019-2020


**Purpose of the Study**

The purpose of the study is to find out whether there is any correlation between particular characteristics of a text aimed to raise money for some charity cause and the success of the collection. For the purpose of the study materials of charitable campaigns from a popular Russian crowdfunding platform were used. 

**Background**

Crowdfunding is a way to attract money for financing a project. It is called that way because the idea is to gather relatively small amounts of money from many people, so that the total amount makes a project possible. Although it has become well known and popular recently due to the Internet and electronic payments services, it is not an invention of the 21st century. For example, in 1850-80s the National Theatre in Prague was built and later restored after a fire due to common people’s donations. And this is not the only, and not the earliest, case. Interestingly, there is an inscription inside saying “Národ sobě”, which means “people for themselves”, as a reminder that this is a result of the collective impact of those who wanted to have a theater in the city. It is somewhat close to what modern fundraisers frequently offer to their backers: a mentioning of their names in the titles of the movie or on the cover of the album, released due to their funding. 

Modern crowdfunding on the Internet began to develop around 2000s. Today there are several clearly distinguished models of raising funds online, such as reward-based, debt-based, donations-based, equity-based, and others. The causes are various: from creating and launching a new product into market to paying off one’s penalty. Naturally, charity is among the most popular causes for crowdfunding.

Crowdfunding seems to be constructed rather simply, but it is not. Every campaign profile consists of many details. Some campaigns are successful, others are not, and those successful ones show different rate of luck. But there is no answer why it is so. Definitely it is a combination of factors: the idea behind or the purpose of the collection, target amount of money, reputation of the founder, visual design of the campaign, for example, presence of high-quality photographs or a promo video, rewards and gifts, advertising, and so on. This is all applicable to charity (donations-based crowdfunding) as well. However, there are some points that make charitable crowdfunding specific. 

**Relevance**

Donations-based charitable campaigns, to my opinion, are more, let’s say, vulnerable. Unlike reward or equity-based campaigns they don’t offer any gain to donors, except for small thank-you souvenirs like a magnet, a bracelet, or a ticket to a partnership cinema. And they don’t have any product idea behind. So charitable campaigns suggest that users just give their money away. What helps them achieve their goal?

**Studies of the Topic**

In recent years, crowdfunding success factors have been the subject of interest for many researchers from different countries. There are many popular articles and research papers devoted to this issue. Several large datasets are available on Kaggle, where users suggest models predicting if a project is going to be successful. Success factors of Russian crowdfunding projects, based on data from Boomstarter platform, were explored as a subject of master’s thesis by a student of St. Petersburg University Graduate School of Management Anna Petrova, which is claimed to be a pioneered paper in studying success factors of Russian crowdfunding projects. However, I am not aware of any studies 1. devoted specifically to charitable campaigns 2. focused on texts or NLP methods.

**Data Sample**

The vast majority of large and medium Russian nonprofits are engaged in public fundraising on the Internet using their websites, mass media, social media, and crowdfunding platforms. For research purposes, campaign profiles from crowdfunding platforms are the best match since multiple data are publically available and well organised there. Russian nonprofit organisations most often use the following platforms designed for public fundraising: Boomstarter.ru, Planeta.ru, Dobro.mail.ru, and an information portal Takie Dela. The latter is very popular and effective, but is not of much help for data study since the main tools there are not projects’ profiles per se, but professional reports and picture stories, provided by the edition, with no public evidence of the impact of each particular piece to the progress of a campaign.

It is also worth mentioning that all platforms have their own policies and technologies regarding campaign promotion, termination or abortion, which frame its progress and result, so it seems appropriate to analyse the platforms separately first. 

The data available on the three above mentioned platforms are not fully the same. 

Planeta.ru: title, short description, full description, target goal, goal achieved, number of transactions, date of closure, date of start.
Boomstarter.ru: title, short description, full description, target goal, goal achieved, number of transactions, date of closure. 
Dobro.mail.ru: title, short description, full description, target goal, goal achieved, number of transactions. 

So only Planeta.ru allows to see how long it took to achieve the goal, which is important as it can be considered as one of the indicators for measuring success. Taking this into account, I have chosen this platform as the source of data for this project.  

**Success Evaluation**

Classic crowdfunding model suggests that a goal or at least a particular benchmark must be reached within originally specified period of time, otherwise all the pledges are canceled. Charitable campaigns on the platforms mentioned above are based on co-called flexible funding principle. A campaign is considered successful and the founder can get the money no matter what part of the target sum is gathered. And if the target sum is gathered, а project is not closed automatically, but goes on until its founder closes it. Often these campaigns terminate with a result of 150-200% of the original goal. Thus, a simple classification of such campaigns into successful and unsuccessful is impossible, so in this research the rate score was taken into account, which equals to the sum of money collected devided by the duration of the collection.

**Research Design**

In order to achieve the goal of the study the following objectives were set and reached:
- to collect and systematise the data needed. The final dataset consists of 2000+ texts (or text id-s) of campaigns with their indicators: target goal, goal achieved, number of transactions, date of closure, date of start, and other variables,
- to analyse texts for a number of characteristics,
- to match significantly different characteristics with the success indicators,
- to find patterns and make assumptions.

The project was carried out in Python3 and R.

**Further Development**

In future the study can be expanded to cover:

1. Other Russian-language platforms, listed above, to verify the patterns found within current research of the Planeta.ru campaigns 
2. Crowdfunding texts in Czech, Polish, and English, as it has been already revealed that the same features of campaigns may be involved in completely different patterns depending on a country and audience.

