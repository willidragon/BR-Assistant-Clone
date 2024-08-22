import psycopg2

# Connection details
conn = psycopg2.connect(
    dbname="mpcs_db",
    user="mpcs_user",
    password="mpcs_password",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Query to retrieve data from the recipes table
cursor.execute("SELECT * FROM recipes LIMIT 10;")
rows = cursor.fetchall()

# Print the column names
colnames = [desc[0] for desc in cursor.description]
print(" | ".join(colnames))

# Print the retrieved rows
for row in rows:
    print(" | ".join(str(col) for col in row))

# Close the connection
cursor.close()
conn.close()
