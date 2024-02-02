# Module 10 - sqlalchemy-challenge

### In this challenge, we were tasked to create a climate analysis for a long holiday vacation to Honolulu, Hawaii. This challenge was split into two parts: Analyze and Explore the Climate Data and Designing a Climate App.

## Part 1: Amalyze and Explore the CLimate Data
### In this section, we used Python and SQLAlchemy to do basic climate analusis and data exploration of the climate database. 

#### Precipitation Analysis
##### 
1. Find the most recent date in the dataset: 8/23/2017
2. Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
3. Select only the "date" and "prcp" values.
4. Load the query results into a Pandas DataFrame. Explicitly set the column names.
5. Sort the DataFrame values by "date".
6. Plot the results by using the DataFrame plot method.

#### Station Analysis
##### 
1. Design a query to calculate the total number of stations in the dataset: 9
2. Design a query to find the most-active stations (that is, the stations that have the most rows). List the stations and observation counts in descending order. Answer the following question: which station id has the greatest number of observations? USC00519281
3. Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
4. Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps: Filter by the station that has the greatest number of observations, query the previous 12 months of TOBS data for that station, plot the results as a histogram with bins=12.

## Part 2: Design Climate App
### In this section, we designed a Flask API on the queries that we developed. 

#### 1. /
Start at the homepage and list all available routes: 
/api/v1.0/precipitation
/api/v1.0/stations
/api/v1.0/tobs
/api/v1.0/start
/api/v1.0/start/end

#### 2. /api/v1.0/precipitation
Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the value. Return the JSON representation of your dictionary. The first date in the dictonary is "2016-08-23": 0.7, and the last is "2017-08-23": 0.45

#### 3. /api/v1.0/stations
Return a JSON list of stations from the dataset. 
 "USC00519397",
  "USC00513117",
  "USC00514830",
  "USC00517948",
  "USC00518838",
  "USC00519523",
  "USC00519281",
  "USC00511918",
  "USC00516128"

#### 4. /api/v1.0/api/v1.0/tobs
Query the dates and temperature observations of the most-active station for the previous year of data. Return a JSON list of temperature observations for the previous year. The first observed temp is 77.0 and the last is 79.0.

#### 5. /api/v1.0/<start> --- To test if this route worked I used /api/v1.0/'2016-08-23'
Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start date. For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
##### http://127.0.0.1:5000/api/v1.0/'2016-08-23'
Returns: Min temp: 53.0, Avg temp: 73.09795396419437, Max temp: 87.0


#### 6. /api/v1.0/<start>/<end> --- To test if this route worked I used /api/v1.0/2016-10-11/2017-08-11
Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start date. For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
###### http://127.0.0.1:5000/api/v1.0/2016-10-11/2017-08-11
Returns: Min temp: 58.0, Avg temp: 73.9524064171123, Max temp: 87.0

### Outside Help
#### For this assignment, I used outside sources such as Stack Overflow, ChatGPT, Classmates.
##### One of the reoccuring errors I came across when creating the Flask API was a "server already in use" error. I found that this could be resolved by running "lsof -i :5000" in the terminal, this returns which programs are running on the 5000 server. To termiate the server I ran "kill -9 <pid_id>" an used the pid id that was listed in the previous command. 
##### When creatnig the start and start/end routes I found that for the start url the date had to be in quotes due to the forloop whereas the start/end route dates did not need to be in quotes. 
###### "summary[i][0:]" accesse the i-th element from the list of temperatures and copies the entire string of data(min temp, avg temp, max temp)
