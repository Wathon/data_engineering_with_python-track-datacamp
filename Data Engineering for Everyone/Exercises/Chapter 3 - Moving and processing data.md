# Data Engineering for Everyone
---

## Moving and processing 
Data engineers make life easy for data scientists by preparing raw data for analysis using different processing techniques at different steps. These steps need to be combined to create pipelines, which is when automation comes into play. Finally, data engineers use parallel and cloud computing to keep pipelines flowing smoothly.

### Processing data - Connect the dots
Data pipelines are used to process data. At the end of Chapter 1, you learned about ETL (Extract, Transform, Load), one of the frameworks used to build data pipelines. The data processing tasks you just studied actually match that framework, corresponding to either extraction, transformation or loading operations.

Note that although saving and loading are usually considered to be opposites, in the context of data engineering, they are the same thing, as you may have noticed. The reason for this is that when you're saving something, you're just storing it in the next step in the pipeline.

Can you correctly classify data processing tasks as extraction, transformation, or loading operations?

##### Answer:
###### Extract
* Collecting data from Google Analytics about our web-marketing promotion offering 3 months of access to the premium tier.
* Pulling the top 20 songs users have been listening to on a loop.

###### Transform
* Sorting a playlist's songs based on the date they were added.
* Summarizing the yearly listening activity to tell users how many hours they've listened to music on Spotflix this year.

###### Load
* Saving the new order of a playlist that was sorted based on the date songs were added, so that it remains that way the next time the user connects.
* Writing all the followers of a user in a table.
---

### Scheduling data - Schedules
You just saw three ways of scheduling data: manually, at a specific time, or if a specific condition is met.

Can you correctly classify the actions on the right?

##### Answer:
###### Manual
* Running the song encoding pipeline, because engineering changed the encoder and wants to make sure they still pass the validation check.
* Running the pipeline processing sign ups because in the past 10 minutes, 100 new users complained to support that they can't connect.

###### Time
* Collecting data from Google Analytics every morning to check how the promotion campaign is going.
* Generating the Spotflix Weekly Playlist from Chapter 1 every Monday at 00:00 AM.
* Processing music videos uploaded by artists every hour.

###### Condition
* Running validation checks if new videos are being collected.
* Updating the number of followers in a playlist table after a user subscribed to it.
---

### Scheduling data - One or the other
You've seen that data can be processed in batches (records are grouped and processed at intervals) or streams (records are sent individually right away).

Can you correctly classify the actions on the right as being batched or streamed?

Some of these are tricky, you may have to think twice! Don't worry if you don't get it right the first time. All that matters is that you get the difference between batches and streams, so if you make a mistake, make sure to read the orange feedback messages at the bottom left to understand why!

##### Answer:
###### Batch
* Loading new employees to Spotflix's employee table.
* Reducing access to premium features when someone unsubscribes.
    > This one was tricky. Think about what happens when you unsubcribe from a service. Do they remove your accesses right away? No! They tell you you will still have access until the subscription period expires. So everyday at 11:59 PM, Spotflix runs the pipeline managing accesses, and all users whose subscription period ends at that date and that did not renew lose access. Because we group all unsubscribed users, this is a batching situation.

###### Stream
* Updating the count of followers in a playlist when a user subscribes to it.
* When a user listens to songs that are being recommended in real time, loading his upvotes and downvotes on each song.
---

### Parallel computing - Whenever, whenever
While you're having lunch with the rest of the data science team, Sasha, the new data engineer intern, is telling you this: "Parallel computing is a jack of all trades and can be used whenever we want, for any task we want. It just optimizes running any data processing tasks. We should start implementing it across the whole pipeline. I'm ready to help doing it!"

Is her statement actually true or false?

##### Answer:
- [ ] True
    > Nope! Parallel computing, although incredibly efficient and powerful, is not a magic tool solving all the data engineering processing challenges, and can actually be overkill. It incurs a cost in that data has to be moved to the processor. Also, the time taken to move data can sometimes outweigh the time saved by doing computations in parallel. The two scenarios where this tends to occur are when transporting data is slow (imagine if the sales assitants folding t shirts worked in different buildings), or when the computation is trivial.
- [x] False
---

### Parallel computing - Parallel universe
You just told Sasha, the data engineer intern, that although incredibly efficient and powerful, parallel computing is not suited to every situation. It has its limitations, and sometimes it's just unnecessary.

You would like to help Sasha improve her understanding. You ask her to tell you their assumptions about parallel computing: you will tell her if she's right or wrong, and try to explain why. Are you up to the challenge?

##### Answer:
###### Right
* Parallel computing relies on processing units.
    > Processing units would correspond to the employees in the video's t-shirts folding example. They work in parallel and merge their results after completing their part of the job.
* It's a good idea to use parallel computing to encode songs uploaded by artists to the `.ogg` format that Spotflix prefers.
    > Encoding many songs is a resource intensive. It's a good idea to leverage parallel processing to get extra processing and finish faster.
* Parallel computing is used to provide extra processing power.
    > Providing extra processing power is one of the two main reasons you would want to use parallel computing.

###### Wrong
* It's a good idea to use parallel computing to update the employees table every morning.
    > It's not necessary to use parallel computing to update the employees table. It's a casual, low resource task that can easily be completed on one processing unit only. Using parallel processing for that would be like investing in a top-of-the-art soud system to play midi ringtones on it. In terms of communication time, going back to the t-shirt analogy: if there are only 10 t-shirts to fold, and it takes 10 minutes to share out the t-shirts and 5 minutes to collect them, it definitely outweighs the couple of minutes required for a single person to fold the t-shirts.
* Parallel computing can't be used to optimize for memory usage.
    > Parallel computing can be used to optimize for memory usage.
* Parallel computing will always make things faster.
    > There are some instances when parallel computing can actualy make things longer, because of the time required to communicate between the processing units.
---

### Cloud computing - Obscured by clouds
Sasha, the new data engineer intern, is now trying to convince you that cloud computing and multicloud computing have absolutely no downsides. You disagree: you know for a fact that this is not true. It makes you question whether or not she is actually comfortable with the topic.

Once again, you take your manager role to heart and try to help her improve her understanding. You ask her to tell you their assumptions about cloud computing: you will tell her if she's right or wrong, and try to explain why. Are you up to the challenge?

##### Answer:
###### Right
* Cloud computing encompasses storage, database and computing solutions.
    > Storage, database and computing are the three faces of cloud computing.
* Leveraging the cloud instead of having our own on-premises data center allows us to use just the resources we need, when we need them.
    > If you own an on-premises data center, you need it to be powerful enough for your peak activity, and the rest of the time these resources stay idle. Using the cloud allows you to use just the resources you need, when you need them.
* A multicloud solution reduces reliance on a single vendor.
    > Multicloud consists in using several cloud providers, so you reduce your reliance on a single vendor.

###### Wrong
* EC2, S3 and RDS are solutions offered by Microsoft Azure.
    > EC2, S3 and RDS are solutions offered by AWS.
* Cloud computing reduces all kinds of risk.
    > Cloud computing is basically just using another computer, far away. If you manage sensitive data, like medical records, you'd probably prefer to keep them close. Also, following the global surveillance revelations made by Snowden in 2013, a lot of companies became wary of using the cloud, and tend to request that the servers at least be outside the US.
* Multicloud solutions reduce security and governance concerns.
    > Multicloud increases security and governance concerns. You need to pay attention to the vulnerabilities of three providers instead of one. You also need to manage the availability, usability, integrity and security of the data not only over different services, but also over different platforms.
---

### Cloud computing - Somewhere I belong
81% of companies have implemented a multicloud approach, according to Gartner. Spotflix's data engineers are worried about the company's reliance on a single vendor, and are considering a multicloud approach. They also think it might be allow Spotflix to reduce costs, and to be more resilient in the face of a disaster.

As you've just seen, the main cloud providers are AWS, Microsoft Azure and Google Cloud. Together, they own about half of the cloud computing market share. They have different services, some you saw in the video, some you're about to discover. They also have competitors, some of which you're about to discover as well.

Can you help the data engineers classify the different services before they start evaluating alternatives?

##### Answer:
###### File storage
* AWS S3
* IBM Cloud File Storage

###### Computing
* Azure Virtual Machines
* AWS EC2

###### Databases
* AWS Redshift (datawarehouse)
* Snowflake Data Warehouse
    > Snowflake, founded in 2012, is disrupting the data warehouse industry and enjoyed a 174% revenue growth in 2019. That might be a name to remember!
* Google Cloud Datastore (NoSQL)

