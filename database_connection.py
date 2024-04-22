import mysql.connector
from sqlalchemy import create_engine
import pandas as pd


class MySQL_API:
    def __init__(self, path):
        self.path = path
        self.df = pd.read_csv(self.path)

    def connection_parameters(self):
        self.engine = create_engine(
            r"mysql+mysqlconnector://root:@localhost/db_name"       #db_name refers to the database
        )                                                           #that you have to create in
        self.connection = mysql.connector.connect(                  #MySQL Workbench before running
            user="root",                                            #this script
            host="127.0.0.1",
            database="db_name",
            auth_plugin="mysql_native_password",                    #table_name (below) is name of the table
        )                                                           #which will contain your data
        self.cursor = self.connection.cursor()
                                                                    #below example of creating the table
    def database_constructor(self):                                 #you can define your own principles
        self.cursor.execute("DROP TABLE IF EXISTS table_name")      #and datatypes in columns (edit 
        self.sql_statement = f"""create table table_name(           
            id int primary key not null auto_increment unique,
            {self.df.columns[0]} varchar(50) not null,
            {self.df.columns[1]} varchar(30),
            {self.df.columns[2]} varchar(2) not null,
            {self.df.columns[3]} varchar(3),
            {self.df.columns[4]} float not null,       
        );
        """
        self.cursor.execute(self.sql_statement)
        self.df.to_sql(
            "table_name", con=self.engine, if_exists="append", index=False
        )


def main():
    obj1 = MySQL_API(
        r"C:\filedirectory\file.csv"                                 #path to your file with
    )                                                                #data which you want to use
    obj1.connection_parameters()
    obj1.database_constructor()


if __name__ == "__main__":
    main()
