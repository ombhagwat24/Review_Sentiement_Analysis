# `Fire TV Stick Reviews Sentiement Analysis`
<img src="https://www.kdnuggets.com/wp-content/uploads/mayo_sent_analysis_fastapi_transformers-0.jpg" width="400px" align="right" alt="emo">

Sentiment Analysis, as the name suggests, it means to identify the view or emotion behind a situation. It basically means to analyze and find the emotion or intent behind a piece of text or speech or any mode of communication.
We, humans communicate with each other in a variety of languages and any language is just a mediator or a way in which we try to express ourselves. And whatever we say has a sentiment associated with it. It might be positive or negative or it might be neutral as well.

### Example: 
There is a fast-food chain company and they sell a variety of different food items like burgers, pizza, sandwiches, milkshakes, etc. They have created a website to sell their food and now the customers can order any food item from their website and they can provide reviews as well, like whether they liked the food or hated it.

- User Review 1: I love this cheese sandwich, it’s so delicious.
- User Review 2: This chicken burger has a very bad taste.
- User Review 3: I ordered this pizza today.

So, as we can see that above 3 reviews, 
> #### The first review is definitely a positive one and it signifies that the customer was really happy with the sandwich.

> #### The second review is negative, and hence the company needs to look into their burger department.
> #### And, the third one doesn’t signify whether that customer is happy or not, and hence we can consider this as a neutral statement. 

<img src="https://miro.medium.com/max/1400/1*8yXXpa8fOBibcOo12gMC_Q.png" min-width="100px" max-width="100px" width="400px" align="left" alt="graph">

## We Have selected amazon FireTV Stick as our product because it has more reviews and also good customer ratings so we decided to extract the data from Amazon website using BeautifulSoup.
## Amazon fire Tv stick is a media streaming device which lets to stream video, install apps, play music etc on your tv. It's built on the Android platform and it converts normal tv to a smart tv. 

## `Dataset after Adding polarity & Subjectivity`
![0025A4E7-2F29-4B94-B6B1-89FC0B41C590](https://user-images.githubusercontent.com/94888819/178972748-68e75d58-733b-4eea-a744-612c9f7bda79.jpeg)

# `Insights`

<img src="https://user-images.githubusercontent.com/94888819/178961424-2c09572e-4c84-41f0-ba44-d687a37541a8.png" min-width="100px" max-width="100px" width="500px" align="left" alt="count"/>

<img src="https://user-images.githubusercontent.com/94888819/178956189-df549926-62cd-4261-adb0-de8e6832506d.png" width="500px" align="right" alt="pie" />

<img src="https://user-images.githubusercontent.com/94888819/178960397-d066533e-1ed1-45c7-a25b-b40f66e9e840.png" width="500px" align="left" alt="polarity" />
 
<img src="https://user-images.githubusercontent.com/94888819/178962297-566ba8ca-8c77-4a0c-8ad9-5c3a0a839e15.png" width="500px" align="right" alt="pair" hspace="20"/>
<br><br><br><br><br><br><br><br><br><br><br><br>

<p align="center">
  <img width=100% src="https://user-images.githubusercontent.com/94888819/179353317-284f8499-3045-4dd0-8050-2d6c0754881e.png">
</p>


# `Model Accuracy Comparison`

| Algorithms  | Accuracy  |
| --- | --- | 
| **Logistic Regression** | **89%** | 
| **Random Forest** | **88%** | 
| **Naive Bayes** | **84%** | 
 

# `Model Deployment`
<img src="https://user-images.githubusercontent.com/94888819/178969316-0f2b851a-57e7-406b-88bf-2ea0fd3f63ac.png" width="900px" align="left" alt="deploy" />
<br><br><br> <br> <br><br><br><br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> 


# `Group Members`
This project is part of Data Science internship in [Excelr](https://learn.excelr.com/login)
Member | Email | LinkedIn |
| --- | --- | --- |
| **Mentor: Varun Vennelaganti** | [💌](vv@gmail.com) | [☺️](https://www.linkedin.com/in/ram-varun-vennelaganti-52119331/) |
| **Omkar Bhagwat** | [💌](https://mail.google.com/mail/u/0/#inbox?compose=GTvVlcSGMSqpLlKHdJncbTZTdtLhpXqgQSwHCFpfrjfZtHKSSfSsbndnmvKSTbBncQRzXzfTqwgKn) | [🤗](https://www.linkedin.com/in/omkar-bhagwat-64b103230) |
| **Yogita Mishra** | [💌](https://mail.google.com/mail/u/0/#inbox?compose=CllgCJTNqLRFszLcsmmlCThKhwwtPfgTksfpBHzXLnnwjJkSbwStDZHKDMrTdHZPZHrppSzWCZL) |[😄](https://in.linkedin.com/in/yogita-mishra-8487b5161?trk=people-guest_people_search-card&original_referer=https%3A%2F%2Fwww.linkedin.com%2F) |
| **Chitravi Angane** | [💌](https://mail.google.com/mail/u/0/#inbox?compose=DmwnWrRlQHVftJQMlZKhBJjnFWzKGhwxgckCSxwhZWwqZGXCtLNtbnNsZTMjnpmQgcWgVGldKfZQ) | [😎](https://in.linkedin.com/in/chaitravi-angane-a83a9323b) |
| **Amrut Vishwaroop** | [💌](https://mail.google.com/mail/u/0/#inbox?compose=DmwnWrRlQHVftJQMlZKhBJjnFWzKGhwxgckCSxwhZWwqZGXCtLNtbnNsZTMjnpmQgcWgVGldKfZQ) | [🥰](https://www.linkedin.com/in/amrut-vishwaroop-0ab946232/) |
| **Akarsh Bhasi** | [💌](https://mail.google.com/mail/u/0/#inbox?compose=DmwnWrRlQHVftJQMlZKhBJjnFWzKGhwxgckCSxwhZWwqZGXCtLNtbnNsZTMjnpmQgcWgVGldKfZQ) | [😀](https://www.linkedin.com/in/akarshbhasi/) |
| **Nitin Sharma** | [💌](https://mail.google.com/mail/u/0/#inbox?compose=DmwnWrRlQHVftJQMlZKhBJjnFWzKGhwxgckCSxwhZWwqZGXCtLNtbnNsZTMjnpmQgcWgVGldKfZQ) | [😇](https://www.linkedin.com/in/nitin-sharma-5972091b0/) |
