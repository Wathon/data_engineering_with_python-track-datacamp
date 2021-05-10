# Data Engineering for Everyone

## What is data engineering?
### Go with the flow
To understand what data engineers do, why they are necessary and the impact they have, you need to know how data flows through an organization.

Can you order the four steps of the data science workflow chronologically?
##### Ans:
1. Data collection and storage
2. Data preparation
3. Exploration and visualization
4. Experimentation and prediction

### Not responsible
You recently joined the data science team as a manager for a music streaming company named Spotflix. It's a music platform that lets users stream songs, create playlists, follow artists, watch music videos and even look up lyrics!

One of your colleagues just walked to your desk. They just got hired, but they already know you're on the data team - after training with DataCamp, you've made a name for yourself pretty quick! They have a bunch of data tasks they need completed, and they want to make sure they ask the right person. You tell them you can help them identify what they should request from data engineers, and what they should not.

Can you deliver on this promise?
##### Ans:
###### Data engineering tasks
* Ensuring corrupted, unreadable music tracks are removed and don't end up facing customers.
* Optimizing the customers databases for analysis.
* Gathering music consumption data from desktop and mobile sources.

###### Not data engineering tasks
* Building a visualization to understand listening patterns by city.
* Running an experiment to identify the optimal search bar positioning in the app.
* Based on their listening behavior, predict which songs customers are likely to enjoy.

### Big time
You saw how the advent of big data increased the demand for data engineers. As more data gets generated, at a higher rate, with a growing variety of formats, the need for people able to manage this data is soaring.

Which of the statements on the right are true, and which are false?
##### Ans:
###### True
* Value refers to how actionable the data is.
* Data types refer to the variety of the data.

###### False
* Veracity refers to how frequently the data is generated.
* Volume has to do with how trustworthy the data is.
* Velocity refers to how big the data is.

### Tell me the truth
In 2012, IBM declared that 90% of the data in the world had been created in the past 2 years. That same year, the amount of digital data in the world first exceeded 1 zetabyte (1 billion terabytes). In 2020, we're expected to reach 44 zetabytes. This big data era led to the advent of two new roles: data engineers and data scientists. You just studied the differences between these two roles.

Let's have a quick sanity check: which of the following options is true?

##### Possible Answers:
- [ ] Data engineers intervene at the very end of the data workflow.
- [ ] Data scientists build pipelines.
- [ ] Data engineers need strong statistical expertise.
- [x] Data engineers enable data scientists.

### Who is it
In the first lesson, you classified some data related tasks between data engineer tasks and not data engineer tasks. Let's raise the bar and see if you can assign more specific tasks to data engineers or data scientists.

##### Ans:
###### Data engineer
* Use Java to build a pipeline collecting album covers and storing them.
* Ensure that people who use the databases can't erase music videos by mistake.
* Provide listening sessions data so it can be analyzed with minimal preparation work.

###### Data scientist
* Find out in which countries certain artists are popular to give them insights on where to tour.
* Identify which customers are likely to end their Spotiflix subscriptions, so marketing can target them and encourage them to renew.
* Use Python to run an analysis and understand whether users prefer having the search bar on the top left or the top right of the Spotiflix desktop app.

### It's not true
The main objective, when setting up data pipelines, is to improve the efficiency with which data flows, from its ingestion to the final users.

Most of the options below are true, but one is false. Which one is it?

##### Possible Ansers:
- [ ] Data pipelines ensure an efficient flow of the data through the organization.
- [ ] Data pipelines automate data extraction.
- [x] Data pipelines necessarily include a transformation step.
- [ ] ETL stands for Extract, Transform, Load.

### Pipeline
**Once you've successfully completed this exercise, make sure to read the success message! 🎶😉**

You've just seen some examples of pipelines used at Spotflix. Let's have you build one!

Our data engineer, Vivian, is working on building new pipelines to generate a new product: the *Weekly Playlist*. It's a playlist that is created by our system every day to recommend new songs that users might like based on their tastes.

On the right, you will find some steps. Can you order the steps correctly to help her build the pipeline generating a *Weekly Playlist* for each user? Let's start with one user, and build a pipeline to generate a *Weekly Playlist* for Julian, our data scientist.

##### Ans:
1. Load the recommended songs into a new table. That's Julian's **Weekly Playlist!**
2. Load only the 10 top songs these users listened to the most over the past week into a table called "Similar profiles"
3. Extract only songs these other users listen to that are of the same genre as the ones in Julian's listening sessions. These are our recommendations.
4. Extract the songs Julian listened to the most over the past month
5. Find other users who listened to these same songs a lot as well