# How to run
To run the script, navigate to the directory the averageSpeedReport.py file is located in and then send it the file path of the input file as the first argument.

Ex: python3 ./averageSpeedReport.py input.txt


## Running the unit tests
To run the unit tests, navigate to the main directory and run the following command. 

python3 -m unittest tests/averageSpeedReportTests.py

That should show that 7 test were run with an OK result


## Thought process
When planning how to process the input file, I decided to make a DriverData class that would store a driver's total distance, duration & be able to calculate the average speed.

From there it made since to add the function to add a trip right into the class. This way it could update the object if the trip met the criteria

I decided to store the driverData in a dictionary with driver name as the key. It made since because the trips could come in any order and a dictionary would provide easy access to the driver data of any driver by their name (which is provided in the trip command)

Printing the report was broken out into a separate function to make unit testing easier

A lot of unit testing was done for the DriverData class because the entire process is really built around it