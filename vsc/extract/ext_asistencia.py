import traceback
from util.db_connection import Db_Connection
import pandas as pd

def extraer_asistencia ():

    try:
        filename = './csvs/asistencia_clases.csv'
        asis = pd.read_csv(filename)
        return asis

    except:
        traceback.print_exc()
    finally:
        pass
