#Pour que python reconnaisse un dossier comme un module il faut ajouter en son sein un chicchier __init__.py 
#et également l'ajouter au PATH
import pandas as pd 
import sys
sys.path.insert(0, "/home/apprenant/Documents/simplon_dev/pyhon_sql/american-dream")


#On peut ensuite importer le dossier comme un module

from src.d00_utils.sqlite_utils import db_connect, save_to_database, rename_cols 


# Connection with BDD version 1 (raw data lives there).

con = db_connect('./Data/01_raw/american_dream_v1.db')
cur = con.cursor()
cur.execute('pragma encoding=UTF8')


# Importing the data from the Data file

df_survey = pd.read_excel('./Data/01_raw/2020_Data_Professional_Salary_Survey_Responses.xlsx', skiprows=3)
df_kaggle = pd.read_csv('./Data/01_raw/american_jobs.csv')

# Renaming all columns before stocking data into database

df_survey.columns = rename_cols(df_survey)
df_kaggle.columns = rename_cols(df_kaggle)

# Feeding the data into our first version database

save_to_database('./Data/01_raw/american_dream_v1.db','salary_survey', df_survey, False)
save_to_database('./Data/01_raw/american_dream_v1.db','dataset_kaggle', df_kaggle, False)
