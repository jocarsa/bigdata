import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('registros.db')
cursor = conn.cursor()

# Execute the query to group epoch values by month
cursor.execute("""
    SELECT strftime('%Y-%m', datetime(utc, 'unixepoch')) AS mes,
           COUNT(*) AS count
    FROM registros
    GROUP BY mes
    ORDER BY mes
""")

# Fetch all the results
results = cursor.fetchall()

# Print the results
for row in results:
    month = row[0]
    count = row[1]
    print(f"Month: {month}, Count: {count}")

# Close the database connection
conn.close()
