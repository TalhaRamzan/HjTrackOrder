import pyodbc
from datetime import datetime
def get_job_order_data(target_order_no):
    server = '65.108.97.18\MSSQLSERVER2019'
    database = 'MedCare'
    username = 'fizza'
    password = '5rQ&57y8s'
    connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()

    job_order_query = f'''
    SELECT
        js.StatusID,
        js.StatusName,
        j.JobID,
        j.OrderNo,
        j.DueDate,
        j.JobDate AS OrderPlacedDate
    FROM
        [Medcare].[dbo].[tblJobStatus] js
        JOIN [Medcare].[dbo].[tblJobs] j ON js.StatusID = j.StatusID
    WHERE
        j.OrderNo = {target_order_no}
    '''
    
    cursor.execute(job_order_query)
    row = cursor.fetchone()
    cursor.close()
    connection.close()
    #change the date in row to this format November 25, 2023
    if row:
        row = list(row)
        row[4] = datetime.strftime(row[4], '%B %d, %Y')
        row[5] = datetime.strftime(row[5], '%B %d, %Y')
        row = tuple(row)
    return row
