import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('registros.db')
cursor = conn.cursor()

# Define a mapping of weekday numbers to weekday names
weekday_mapping = {
    '0': 'Sunday',
    '1': 'Monday',
    '2': 'Tuesday',
    '3': 'Wednesday',
    '4': 'Thursday',
    '5': 'Friday',
    '6': 'Saturday'
}

# Iterate over each weekday
for weekday_number in range(7):
    # Execute the query to calculate hits for the current weekday
    query = '''
        SELECT strftime('%w', datetime(utc, 'unixepoch')) AS weekday, 
       AVG(Identificador) AS average_hits
        FROM registros
      
        GROUP BY weekday;
        
        
    '''
    cursor.execute(query, (str(weekday_number),))
    result = cursor.fetchone()
    hits = result[0]

    # Calculate the average hits for the current weekday
    average_hits = hits / len(weekday_mapping)

    # Get the weekday name from the mapping
    weekday_name = weekday_mapping[str(weekday_number)]

    # Print the average hits for the current weekday
    print(f"Average hits for {weekday_name}: {average_hits}")

# Close the database connection
conn.close()
