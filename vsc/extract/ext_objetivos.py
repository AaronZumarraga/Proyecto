import traceback
from util.db_connection import Db_Connection
import pandas as pd

def extraer_objetivos ():

    try:
        filename = './csvs/objetivos_individuales.csv'
        obj = pd.read_csv(filename)
        return obj

    except:
        traceback.print_exc()
    finally:
        pass
