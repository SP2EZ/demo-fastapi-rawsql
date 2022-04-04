# This Script creates a session with the Database so that SQL commands can be executed
# Library Used : psycopg3
# pip install psycopg[binary]
# Psycopg3 (successor of psycopg2) is a newly designed PostgreSQL database adapter for the Python programming language

import psycopg
from psycopg import rows
import time
from . import config
#print(f"LOOKATME: {config.settings.DATABASE_HOSTNAME}")
try:
    # Connect to an existing database
    # conn = psycopg.connect(host='localhost', dbname='fastapi', user='postgres', password='p@s!gre&', port='5432', row_factory=rows.dict_row)
    conn = psycopg.connect(host=config.settings.DATABASE_HOSTNAME, dbname=config.settings.DB_NAME, user=config.settings.DB_USERNAME, password=config.settings.DB_PASSWORD, port=config.settings.DB_PORT, row_factory=rows.dict_row)
    cursor = conn.cursor()
    print("Database Connected !!!")
except Exception as error:
    print("Database Connection Failed, Error Encountered :")
    print(error)
    time.sleep(15) # This will attempt to reconnect to database every 15 sec if any Connection Issue arises
    #conn.rollback()
#else:
#    conn.commit()
#finally:
#    conn.close()