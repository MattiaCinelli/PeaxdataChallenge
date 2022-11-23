# PEAX AgriFood Data Science Challenge

Welcome to the one and only PEAX AgriFood data science challenge! We are happy that you have made it this far already, since it means that we believe you could be a great fit. But of course, as data-centric professionals we cannot just trust our gut. Therefore, we have created this challenge to test if you have a matching skillset. 
 
 What do you need to prove to us? A lot - but certainly the following:
 
- You are self reliant
- You know how to use data tools
- You have a healthy dose of common sense
- You can present results with your audience in mind
- You have some creativity / originality in your style of problem solving

## The challenge

With PEAX we are assisting organizations in the entire AgriFood value chain. This means that we get in contact with all sorts of companies that contribute to bringing fresh fruit and flowers to people around the world. Our goal is to assist these organizations in implementing data & AI solutions into their business. 

As a new member of our team you have been presented with a dataset from a new customer. We have sold this customer a data exploration and data roadmap project. During such a project we go through a customer's data and determine if certain projects have a high chance of success, and if it is worth investing in them or not.

This client is a large greenhouse grower and is interested in the following two projects:

1. **Artificial lightning control**: For crops to grow, they require substantial levels of radiation. A great source of radiation is, of course, the sun. However, as you might have experienced yourself, the sun does not always show up for providing its beloved rays. To overcome this issue, growers have installed assimilation lighting to provide the crops with additional "artificial" radiation. But, as we say in Dutch: "Voor niets gaat de zon op" and assimilation lighting requires a substantial amount of electricity, which makes it a quite expensive option that should be avoided whenever possible. Over the years the greenhouse grower has gained plenty of experience to know when to turn on the assimilation lightning and when not to. However, he is tired of switching the light on and off himself and thinks this process is ready to be automated. Do you agree with him that this process can be automated? If yes, can you show us how this could be achieved?

2. **Day-ahead energy prediction**: Energy for heating the greenhouse is one of the main cost drivers and natural gas prices can flucatuate substantially, posesing the risk for energy costs getting out of control. In order to mitigate this risk, a greenhouse grower can purchase energy hedge contracts through its energy supplyer. To do so, he needs to have an idea of the amount of energy that he is going to consume on a certain day, so he can purchase the right number of contracts. The grower asked us to help him in making the best decision on a daily basis, when purchasing energy contracts for the next day (starting at 00:00h). Can the dataset be used to predict the energy consumption for the day ahead? If this is possible, what is the margin of error and how should this be taken into account? 

As of now you are responsible for exploring these two areas and seeing what might work. If you have other ideas for interesting cases don't hesitate to show initiative. Also note that the cases described here can be interpreted in the broadest possible sense

## The data

You have received four files which you can use to base your analysis on:

- Weather.parquet (outdoor climate)
- GreenhouseClimate.parquet (indoor greenhouse climate, irrigation, status of actuators, requested and realized climate setpoints)
- Resources.parquet (resources)
- Production.parquet (harvest)

Besides these files there is a README included that is created by the customer and tells you more about the content of the data files. The person who created this README has left on holidays after sendig us the README, but she said they should be easy to figure out. Let's hope they are because you won't have the luxury of asking someone questions.

If you are unsure about something - feel free to make assumptions, but as always mention this in your presentation.

> Note: This dataset is based on real data that is collected during the Autonomous Greenhouse Challenge 2nd Edition, organized by Wageningen University & Research (WUR). You have been handed the data of the reference team, experienced growers which were used as a benchmark. 

## Deliverables

As the newest team member you are expected to take the first steps towards solving this case for this client. We want you to show us:

1. A walkthrough of your code/notebooks/... Focus on the important aspects - no need to explain to us how you load the data. What solution techniques would you plan on using? Why? Imagine this to be presented to the tech lead of your project, someone who has substantial experience and will challenge you on the technical aspects of what you propose. This can be done in your solution notebook, ensuring that it is readable to somebody else: Make sure you have enough comments/markdown to support your code. Also ensure that the answers to the business questions are (briefly) given in this notebook, without any external materials needed. This includes a proper evaluation of your model(s).

2. A brief presentation where you present your findings to a management audience. Defend your business case. If doing all the calculations right now is too much work show us how you would do these calculations and where you expect to find the required data. Imagine this to be a dry-run with the product owner from our side (= the person responsible for taking the client's perspective) or a C-level manager from the customer, who has some basic data science understanding.

The materials you send should be comprehensive (= they include everything a reader might need to evaluate what you have done). Keep in mind that these materials will be read without your voice over before you are given the opportunity to present your work. While it is certainly not expected that you provide a full written article do provide some notes on what you are doing and why in the files you send to us.

If you are short on time, we recommend you focus on the notebook (with comments), as there is some time between our evaluation of your notebook and your presentation. This means you have some more time to finish your presentation after sending us your notebook.

Important note: While we want you to show us what you've got, there is no need to fully "solve" the case; no need to create every single possible model and deploy things on a server. Focus on the important part: Show how you would solve things, convince us that you understand what you are doing.

**As a closing argument please include how you would approach this if you had had more time, and how much more time you would expect to need to perform the additional things you have in mind.**

**Impress us!**