import traceback
from util.db_connection import Db_Connection
import pandas as pd

def cargar_adherencia_planes_nutricionales():
    try:
        # Configuración para la base de datos de staging
        type_stg = 'mysql'
        host_stg = '10.10.10.2'
        port_stg = '3306'
        user_stg = 'dwh'
        pwd_stg = 'upORo-D?Y4V&'
        db_stg = 'staging'

        # Conexión a la base de datos de staging
        con_db_stg = Db_Connection(type_stg, host_stg, port_stg, user_stg, pwd_stg, db_stg)
        ses_db_stg = con_db_stg.start()
        if ses_db_stg == -1:
            raise Exception(f"El tipo de base de datos {type_stg} no es válido")
        elif ses_db_stg == -2:
            raise Exception("Error al establecer la conexión de pruebas")

        # Configuración para la base de datos de sor
        type_sor = 'mysql'
        host_sor = '10.10.10.2'
        port_sor = '3306'
        user_sor = 'dwh'
        pwd_sor = 'upORo-D?Y4V&'
        db_sor = 'sor'

        # Conexión a la base de datos de sor
        con_db_sor = Db_Connection(type_sor, host_sor, port_sor, user_sor, pwd_sor, db_sor)
        ses_db_sor = con_db_sor.start()
        if ses_db_sor == -1:
            raise Exception(f"El tipo de base de datos {type_sor} no es válido")
        elif ses_db_sor == -2:
            raise Exception("Error al establecer la conexión de pruebas")

        # Consulta para seleccionar datos de la tabla Ext_AdherenciaPlanesNutricionales en la base de datos de staging
        sql_stmt = "SELECT ID_Miembro, Fecha, Adherencia FROM Ext_AdherenciaPlanesNutricionales"
        adherencia_planes_data = pd.read_sql(sql_stmt, ses_db_stg)

        # Verificar si hay datos para procesar
        if not adherencia_planes_data.empty:
            # Renombrar las columnas según la estructura de Dim_AdherenciaPlanesNutricionales
            adherencia_planes_data.rename(columns={'ID_Miembro': 'ID_Miembro', 'Fecha': 'Fecha', 'Adherencia': 'Adherencia'}, inplace=True)

            # Insertar datos en la tabla Dim_AdherenciaPlanesNutricionales en la base de datos de sor
            adherencia_planes_data.to_sql('Dim_AdherenciaPlanesNutricionales', ses_db_sor, if_exists='append', index=False)

    except:
        traceback.print_exc()
    finally:
        pass

# Llamar a la función para cargar los datos
cargar_adherencia_planes_nutricionales()
