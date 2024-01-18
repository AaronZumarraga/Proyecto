import traceback
from util.db_connection import Db_Connection
import pandas as pd

def extraer_compras ():

    try:
        filename = './csvs/compras_suplementos.csv'
        comp = pd.read_csv(filename)
        return comp

    except:
        traceback.print_exc()
    finally:
        pass
