import traceback
from util.db_connection import Db_Connection
import pandas as pd

def persistir_staging (df_stg, tab_name):

    try:
        type = 'mysql'
        host = '10.10.10.2'
        port = '3306'
        user = 'dwh'
        pwd = 'upORo-D?Y4V&'
        db = 'staging'

        con_db = Db_Connection(type, host, port, user, pwd, db)
        ses_db = con_db.start()
        if ses_db == -1:
            raise Exception(f"El tipo de base de datos {type} no es válido")
        elif ses_db == -2:
            raise Exception("Error al establecer la conexión de pruebas")        
        
        df_stg.to_sql(tab_name, ses_db, if_exists='replace', index=False)

    except:
        traceback.print_exc()
    finally:
        pass
