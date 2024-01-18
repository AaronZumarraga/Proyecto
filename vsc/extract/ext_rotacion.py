import traceback
from util.db_connection import Db_Connection
import pandas as pd

def extraer_rotacion ():

    try:
        filename = './csvs/rotacion_equipos.csv'
        rot = pd.read_csv(filename)
        return rot

    except:
        traceback.print_exc()
    finally:
        pass
