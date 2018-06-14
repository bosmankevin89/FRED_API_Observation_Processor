
#Imports
import configparser
import psycopg2

class DB_FRED_Observations:
    

    def __init__(self, tableName):

        try:

            config = configparser.ConfigParser()
            config.read('config/config.ini')

            host = config['DEFAULT']['TARGET_DB_HOST']
            dbName = config['DEFAULT']['TARGET_DB_NAME']
            user = config['DEFAULT']['TARGET_DB_USER']
            password = config['DEFAULT']['TARGET_DB_PASSWORD']

            # Raise error on missing values
            if not host:
                raise ValueError('Configuration value host not defined')
            if not dbName:
                raise ValueError('Configuration value dbName not defined')
            if not user:
                raise ValueError('Configuration value user not defined')
            if not password:
                raise ValueError('Configuration value password not defined')
            if not tableName:
                raise ValueError('Variable tableName not defined')

            self.cs = "host='%s' dbname='%s' user='%s' password='%s'" % (host,dbName,user,password)

            #Setup delete and insert statements
            self.tableName = tableName
            self.strDelete = 'delete from "FRED_OBSERVATIONS".' + tableName + ' where realtime_end = %(realtime_end)s'
            self.strInsert = 'INSERT INTO "FRED_OBSERVATIONS".' + tableName + ' (series_id, realtime_start, realtime_end, observation_date, observation_value) VALUES (%(series_id)s, %(realtime_start)s, %(realtime_end)s, %(observation_date)s, %(observation_value)s);'

        except ValueError as err:
            raise ValueError('Error initializing DB_FRED_Observations: ' + str(err))


   
    def insert(self, data):
        
        conn = psycopg2.connect(self.cs)
        cursor = conn.cursor()

        #Inject table name
        data["table_name"] = self.tableName
        
        cursor.execute(self.strInsert, data)
        conn.commit()

    def delete(self, date):
        
        conn = psycopg2.connect(self.cs)
        cursor = conn.cursor()
        
        data = {
            "table_name" : self.tableName,
            "realtime_end": date
        }

        cursor.execute(self.strDelete, data)
        conn.commit()