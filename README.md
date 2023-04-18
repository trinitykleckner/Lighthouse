# LightHouse

### Won best Diversity, Equity, and Inclusion hack at Philly Codefest 2023!

### Check out this article written about it: [Haverford Team Triumph at Philly Codefest Competition](https://www.haverford.edu/college-communications/news/haverford-team-triumphs-philly-codefest-competition) 

## Elevator Pitch
Our web app aims to help refugees and immigrants find resources to meet immediate needs and work towards long term goals which will help them thrive in the U.S.

## Inspiration
For refugees, settling in a new country can be a challenging and overwhelming experience, especially if they are unfamiliar with the language, culture, and resources available to them. LightHouse is created to help address these challenges by providing refugees with information and resources that can help them navigate their new surroundings more easily. The inspiration behind Lighthouse have come from a refugee team members and the desire to help refugees integrate into their new communities, connect with resources that can support them, and ultimately build new lives for themselves and their families in the United States.


## What it does
LightHouse, our web app will helping refugees integrate into their new communities and build new lives for themselves and their families. Specifically, it aims to help refugees in the United States find resources to meet immediate needs and work towards long-term goals. 

The app provides a user-friendly interface, with no complicated features someone with little experience on the internet would struggle with, to connect refugees with resources that offer services such as housing, employment, healthcare, education, legal aid, and more using OpenAI's GPT3. 


## How we built it
We used python-based web app using a Django framework. The front end was build with bootstrap, html, css, and js, and the backend was all python. Because the chatGPT API is paid, we built a webhook in js that was called from the app, that used GPT for Sheets to return chatGPT answers for free. 


## Challenges we ran into
As with any hackathon, the main challenge we faced was time. Our vision was large, and cutting down what was accomplishable for this 24 hour MVP was difficult. Besides time, our toughest, ongoing challenge was balancing personalization and privacy. We wanted the GPT responses to be specific enough to really provide value to the user, however we did not want to ask the user much about themselves, as for people entering the U.S. that is very sensitive information. Accordingly, we decided not to have any accounts created, which meant we needed to figure out how to store the minimal information throughout one persons session, which was another challenge in itself. 


## Accomplishments that we're proud of
We are proud of what we built, and how well we worked together over the 24 hours. We are most proud that what we built can have a positive impact and utilizes what has become trivial technology to help a very vulnerable populations in the U.S. that may not know how to use it otherwise. 


## What we learned
The importance of user research, design, data security and privacy, and user feedback. 

## What's next for LightHouse
Research! 
