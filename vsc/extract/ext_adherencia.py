import traceback
from util.db_connection import Db_Connection
import pandas as pd

def extraer_adherencia ():

    try:
        filename = './csvs/adherencia_nutricional.csv'
        adh = pd.read_csv(filename)
        return adh

    except:
        traceback.print_exc()
    finally:
        pass
