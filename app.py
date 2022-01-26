# import pyodbc

# server = 'siametrices-db.database.windows.net'
# database = 'siametricesdb' 
# username = 'siametricesdbadmin'
# password = 'Twpc@2022pM!!dB'

# # Specifying the ODBC driver, server name, database, etc. directly
# cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=siametrices-db.database.windows.net;DATABASE=siametrices-db;UID=siametricesdbadmin;PWD=Twpc@2022pM!!dB')

# # Create a cursor from the connection
# cursor = cnxn.cursor()

# with open('test-smc-app.py','w',encoding = 'utf-8') as f:
#    f.write("test-smc-app, done.")

def hello():
    print("Handling request to home page.")
    return "Hello, Azure!"
