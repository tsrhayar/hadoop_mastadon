#!/usr/bin/env python3

import happybase
import json
from hdfs import InsecureClient

# HBase connection parameters
hbase_host = 'localhost'  #  HBase host
hbase_port = 9090     #  HBase port

# HDFS client
hdfs_url = 'http://localhost:9870'
hdfs_client = InsecureClient(hdfs_url, user='hadoop')

# Path to reduce output
hdfs_file_path = '/output/ReducerResults1/part-00000'

# Initialize a connection to HBase
try:
    connection = happybase.Connection(host=hbase_host, port=hbase_port )
    #connection = happybase.Connection()
    print("Connected to HBase")

    # Open the table
    table_name = 'Language'
    table = connection.table(table_name)
    print("Connected to table")

    # Read data from HDFS
    with hdfs_client.read(hdfs_file_path) as hdfs_file:
        try:
            data = json.loads(hdfs_file.read())

            # 'Tootslanguage' dictionary
            toots_language = data.get('Tootslanguage')
            
            if toots_language:
                for language, count in toots_language.items():
                    
                    print(f"{language} , {count}")
                    #Insert data into HBase
                    table.put(
                        language.encode('utf-8'),
                        {'Language:Count': str(count).encode('utf-8')}
                    )
            else:
                print("No 'Tootslanguage' data in the JSON")

        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")

    # Close the connection
    #connection.close()
    print("Connection closed")

except Exception as ex:
    print(f"An error occurred: {ex}")