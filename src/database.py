import sqlite3
import json

def run_db(data):
     conn = sqlite3.connect('local.db')
     cursor = conn.cursor()
     cursor.execute("CREATE TABLE IF NOT EXISTS bill_table (invoice_no TEXT, tax_id TEXT, client_name TEXT, gross_worth TEXT)")

     if isinstance(data, dict):
          cursor.execute("INSERT INTO bill_table VALUES (?, ?, ?, ?)",
                         (data.get('InvoiceNo'), data.get('TaxId'), data.get('ClientName'), data.get('GrossWorth')))
     elif isinstance(data, str):
          try:
               json_data = json.loads(data)
               print("Before.......",json_data)
               json_data = json.loads(data.replace("'", '"'))
               print("After.",json_data)
               cursor.execute("INSERT INTO bill_table VALUES (?, ?, ?, ?)",
                              (json_data.get('InvoiceNo'), json_data.get('TaxId'), json_data.get('ClientName'), json_data.get('GrossWorth')))
          except json.decoder.JSONDecodeError:
               # Handle the JSONDecodeError here
               print("Invalid JSON data:", data)
               json_data = {
                    'InvoiceNo': None,
                    'TaxId': None,
                    'ClientName': None,
                    'GrossWorth': None
               }
     else:
          # Handle the case when data is neither a dictionary nor a string
          print("Invalid data type. Expected dictionary or string.")

     conn.commit()
     conn.close()
     print("Successfully updated the database...")


