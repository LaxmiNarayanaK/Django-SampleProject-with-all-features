from sqlalchemy import create_engine
import pandas as pd
     
def dump(df,table):

    engine = create_engine('postgresql+psycopg2://postgres:1234@localhost/telusko')
    df.to_sql(table, engine, if_exists='replace', index = False)
    print("DATA DUMPED")
