import pymysql
import logging
import config

# Logging config
logging.basicConfig(filename="RDS.log", format='%(asctime)s %(message)s', filemode='w') 
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)


# Establish connection to the RDS instance
connectn = pymysql.connect(host=config.host1, user=config.user1, password=config.pwd, db=config.db_name, port=config.port1)


# Cursor allows Python executable code in DB session 
cursr = connectn.cursor()


# Error handling for every operation
try:
    # Query String
    qry_create = "CREATE TABLE Movies(mid int, mname varchar(30))"

    # Query Execution
    cursr.execute(qry_create)

    # Listing Tables for viewing
    qry_show = "show tables"
    cursr.execute(qry_show)
    rows = cursr.fetchall()
    for row in rows:
        print(row)

    # Logging info as table is created successfully
    logging.info('Table Created')

except Exception as e:
    # Displays and Logs Errors
    logger.error(e)
    print('Error! Please Check Your Code.')


try:
    # Query String
    qry_insert = "INSERT INTO Movies(mid, mname) VALUES (1, 'movie1'),(2, 'movie2'),(3, 'movie3'),(4, 'movie4')"

    # Query Execution
    cursr.execute(qry_insert)
    rows = cursr.fetchall()
    for row in rows:
        print(row)

    # Logging info as data is inserted successfully
    logging.info('Inserted Entries')

except Exception as e:
    # Displays and Logs Errors
    logger.error(e)
    print('Error! Please Check Your Code.')


try:
    # Query String
    qry_read = "SELECT * FROM Movies"

    # Query Execution
    cursr.execute(qry_read)
    rows = cursr.fetchall()
    for row in rows:
        print(row)

    # Logging info as data is queried successfully
    logging.info('Table Queried')

except Exception as e:
    # Displays and Logs Errors
    logger.error(e) 
    print('Error! Please Check Your Code.')


try:
    # Query String
    qry_update = "UPDATE Movies SET mid = 10, mname = 'movie9' WHERE mid = 1"
    qry_read = "SELECT * FROM Movies"

    # Query Execution 
    cursr.execute(qry_update)
    cursr.execute(qry_read)
    rows = cursr.fetchall()
    for row in rows:
        print(row)

    # Logging info as data is updated successfully
    logging.info('Table Updated')

except Exception as e:
    # Displays and Logs Errors
    logger.error(e) 
    print('Error! Please Check Your Code.')


try:
    # Query String
    qry_delete = "DELETE FROM Movies WHERE mid = 2"

    # Query Execution 
    cursr.execute(qry_delete)
    cursr.execute(qry_read)
    rows = cursr.fetchall()
    for row in rows:
        print(row)

    # Logging info as data is deleted successfully
    logging.info('Table Entry Deleted')

except Exception as e:
    # Displays and Logs Errors
    logger.error(e) 
    print('Error! Please Check Your Code.')


# Finally Block to end the code
finally:
    # When all the queries are executed, commit all the changes
    connectn.commit()

    # CLose connection to RDS
    connectn.close()
