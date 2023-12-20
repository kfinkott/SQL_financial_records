#scr_sql_tasks.py
#kevin fink
#kevin@shorecode.org
#Oct 7 2023

from datetime import datetime
import sqlalchemy
import env_key
from dataclasses import dataclass
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, Date, Float

@dataclass
class SqlTasks:

    # Fetches the encrypted password
    with open('passkey.txt', 'r') as fn:
        passkey = fn.read()
    passwd = env_key.decrypt_passwd('KEVIN_SQL', passkey)
    engine = create_engine(f'mysql://kevin:{passwd}@localhost/shorecode_monthly')

    def create_table(self, month, year, record_type):
        """
        Creates a meta object containing the criteria for a table and creates that table in the SQL server
        
        Args:
        self ( _obj_ ) : Parent class object
        month ( _obj_ ) : Two digit month, for the table title
        year ( _obj_ ) : Two digit year, for the table title
        record_type ( _obj_ ) : Transaction category for the table title
        
        Returns:
        Does not return
        """
        meta = MetaData()
        records_table = Table(
            f'{str(year)[2:]}-{str(month)}_{record_type}', meta,
            Column('id', Integer, primary_key = True, nullable=False),
            Column('amount', Float),
            Column('currency', String(15)),
            Column('tax_amount', Float),
            Column('date', Date),
            Column('description', String(100)),
            Column('party', String(70))
            )
        meta.create_all(self.engine)
        return records_table

    def add_record(self, record_type, data, columns):
        """
        Adds a transaction record to the SQL database
        
        Args:
        self ( _obj_ ) : Parent class object
        record_type ( _obj_ ) : Transaction category
        data ( _obj_ ) : User supplied transaction data
        columns ( _obj_ ) : Columns for the data
        
        Returns:
        Does not return
        """
        # Gets a dictionary containing the form data and a SQL meta object identifying the table
        # to be used
        data_dict, records_table = self.prepare_data(data, columns, record_type)
        stmt = sqlalchemy.insert(records_table).values(amount=data_dict['Amount'], 
                            currency=data_dict['Currency'], tax_amount=data_dict['TaxAmount'], 
                            date=data_dict['Date'], description=data_dict['Description'], 
                            party=data_dict['Party'])
        with self.engine.connect() as conn:
            conn.execute(stmt)
            conn.commit()
            
    def prepare_data(self, data, columns, record_type):
        """
        Combines the user supplied data and the corresponding type of this data into a dict. Also prepares the date for processing by ensuring the month value is two digits. Creates the table to be used
        
        Args:
        self ( _obj_ ) : Parent class object
        data ( _obj_ ) : User supplied data
        columns ( _obj_ ) : Columns
        record_type ( _obj_ ) : Transaction category
        
        Returns:
        Does not return
        """
        data_dict = dict()
        for i in range(len(data)):
            data_dict[columns[i]] = data[i]

        # Converts the user input (YYYY-MM-DD) to a datetime object
        record_date = datetime(int(data_dict['Date'][:4]), int(data_dict['Date'][5:7]),
                               int(data_dict['Date'][8:10]))
        # Adds a leading zero to months that are less than 10, two ensure consistent easy
        # reading in SQL
        if len(str(record_date.month)) == 1:
            two_digit_month = '0' + str(record_date.month)
        else:
            two_digit_month = str(record_date.month)
        records_table = self.create_table(two_digit_month, record_date.year, record_type)
        return data_dict, records_table

