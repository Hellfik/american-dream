import sqlite3

# BDD connexion

def db_connect(db_name):
    con = sqlite3.connect(db_name)
    return con

# Function to save data into a sqlite database

def save_to_database(db_name, table_name, df_name, is_index):
    con = db_connect(db_name)
    df_name.to_sql(
        name=table_name,
        con=con,
        index=is_index,
        if_exists='replace',
        chunksize=500
)

# Function for renaming columns name of each dataset

def rename_cols(dataset):
    dataset_cols_list = []
    for col in dataset.columns:
        col = col.strip()
        col = col.lower()
        col = col.replace(' ','_')
        dataset_cols_list.append(col)
    return dataset_cols_list