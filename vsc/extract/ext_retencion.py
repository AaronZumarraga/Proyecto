import traceback
from util.db_connection import Db_Connection
import pandas as pd

def extraer_retencion ():

    try:
        filename = './csvs/retencion_post_clase.csv'
        ret = pd.read_csv(filename)
        return ret

    except:
        traceback.print_exc()
    finally:
        pass
