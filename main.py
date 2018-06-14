#
#   "This product uses the FRED® API but is not endorsed or certified by the Federal Reserve Bank of St. Louis."
#


import datetime
from FRED_API_Observations import FRED_API_Observations
from DB_FRED_Observations import DB_FRED_Observations

# Series to process and the related tables.
# (Series ID, Target Table name)
seriesToProcess = [
    #("GDPC1", "real_gross_domestic_product"),
    ("UMCSENT", "University_of_Michigan_Consumer_Sentiment_Index")
    #("UNRATE", "US_Civilian_Unemployment_Rate")
]



def transferData(seriesID, targetTable):

    #Get today's date in YYYY-MM-DD format for deletion
    today = datetime.datetime.today().strftime('%Y-%m-%d')

    print('-------------------------------------------------')
    print('Loading Series "' + seriesID + "' into table '" + targetTable + "'")

    db_RGDP = DB_FRED_Observations(targetTable)
    api = FRED_API_Observations()

    db_RGDP.delete(today)

    rowsProcessed = 0
    rowsInserted = 0
    rowsError = 0

    jsonResponse = api.query(seriesID, rowsProcessed)

    totalRowCount = jsonResponse["count"]

    print('Observation Count: ' + str(totalRowCount))

    while rowsProcessed < totalRowCount:

        # Print status update
        print('~~~~~~~~')
        print('Rows Processed: ' + str(rowsProcessed))
        print('Rows Inserted: ' + str(rowsInserted))
        print('Rows Error: ' + str(rowsError))
        print('~~~~~~~~')

        #Insert each observation into the database.
        for val in jsonResponse["observations"]:
            
            observationValue = val["value"]

            # In some cases, only "." is being reported.  Default to null and potentially log in the future.
            if observationValue == ".":
                observationValue = None

            data = {
                "series_id" : seriesID, 
                "realtime_start" : val["realtime_start"], 
                "realtime_end": val["realtime_end"],
                "observation_date" : val["date"], 
                "observation_value" : observationValue
            }

            try:
                db_RGDP.insert(data)

                rowsInserted += 1
                
            except Exception as err:
                rowsError += 1
                print('Error inserting record: ' + str(err))
            
            #Always increase rows processed
            rowsProcessed += 1
            

        # Reset JSON response based on the rowsProcessed as the current offest
        jsonResponse = api.query(seriesID, rowsProcessed)

    print('Rows Processed: ' + str(rowsProcessed))
    print('Rows Inserted: ' + str(rowsInserted))
    print('Rows Error: ' + str(rowsError))

    if rowsError == 0:
        print('SUCCESS: Successfully loaded Series "' + seriesID + '"')
    else:
        print('WARNING: Errors Encountered loading Series "' + seriesID + '"')

    print('-------------------------------------------------')


##################################
## Main Processing Logic
##################################
try:

    for seriesTuple in seriesToProcess:
        try:
            transferData(seriesTuple[0], seriesTuple[1])
        except Exception as err:
            print('Error loading series "' + seriesTuple[0] + '" ' +  str(err))    

except Exception as err:
    print('Main Processing Error: ' + str(err))