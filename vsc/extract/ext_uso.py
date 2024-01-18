import traceback
from util.db_connection import Db_Connection
import pandas as pd

def extraer_uso ():

    try:
        filename = './csvs/uso_equipos_cardio.csv'
        uso = pd.read_csv(filename)
        return uso

    except:
        traceback.print_exc()
    finally:
        pass