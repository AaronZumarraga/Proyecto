import traceback
from util.db_connection import Db_Connection
import pandas as pd

def extraer_evaluaciones():

    try:
        filename = './csvs/evaluaciones_rendimiento.csv'
        eva = pd.read_csv(filename)
        return eva

    except:
        traceback.print_exc()
    finally:
        pass
