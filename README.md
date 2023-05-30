# Part 2 of assignment

This is the repository for my data pipeline. My focus on this assigment has been to build a production database in MySQL, being able to fetch from tables and putting the data into new tables.

## How to run and set up
The scripts that I have written are in Python, using pip you can install the required packages.
`$ pip install -r requirements.txt`

On the lines 43, 44 and 68 in the **mysqlFunc.py** you will need to put in your username and password for your local instance of MySQL. If this would have been a real production environment I would of course implement a safer way of handling authentication but because of the time constraint I chose not to do so. A safer way of handling authentication can be a github secret, cloud secret or a kubernetes secret, of course all of those depending on how the service is run and orchestrated. 

There is a **main.py** file which is how the script is triggered and calls the functions in the **mysqlFunc.py** file. The functions in the **mysqlFunc.py** file are the ones that create the connection, databases and tables needed for the assignment. There is also a function that fetches and inserts data into the tables.

## What has been implemented and why
As mentioned in the beginning of the README, this solution to the assignment focuses on building the databases and tables needed for a data pipeline.

As stated in the assignment the **production** database is located in a MySQL database which will be recreated together with the user and account tables in the script.

I have chosen to create a seperate database called **analytics** for the pipeline to put the data in, normally I wouldn't put a data platform in a MySQL database since it is not suitable for that, the sheer size and wide variety of rawness of the data makes the use of a relational database management system very cumbersome and difficult. 
My reason for this decision is the time constraint on the assignment and I didn't feel like I had the time to implement a proper data platform on a more suitable data storage system such as Amazon Redshift, Snowflake, BigQuery and others. 
