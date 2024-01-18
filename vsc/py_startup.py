# this file is a kind of python startup module used for manual unit testing

import traceback
from extract.per_staging import persistir_staging
from extract.ext_adherencia import extraer_adherencia
from extract.ext_asistencia import extraer_asistencia
from extract.ext_compras import extraer_compras
from extract.ext_evaluaciones import extraer_evaluaciones
from extract.ext_objetivos import extraer_objetivos
from extract.ext_retencion import extraer_retencion
from extract.ext_rotacion import extraer_rotacion
from extract.ext_uso import extraer_uso
from load.load_asistencia import cargar_asistencia_clases

try:
    adh = extraer_adherencia()
    #print (adh)
    persistir_staging(adh, 'Ext_AdherenciaPlanesNutricionales')
    print("Datos de adherencia nutricional en staging")

    asis = extraer_asistencia()
    persistir_staging(asis, 'Ext_AsistenciaClases')
    print("Datos de asistencia clases en staging")

    comp = extraer_compras()
    persistir_staging(comp, 'Ext_ComprasSuplementosNutricionales')
    print("Datos de compras de suplementos en staging")

    eva = extraer_evaluaciones()
    persistir_staging(eva, 'Ext_EvaluacionesRendimiento')
    print("Datos de evaluaciones en staging")

    obj = extraer_objetivos()
    persistir_staging(obj, 'Ext_ObjetivosIndividuales')
    print("Datos de objetivos en staging")

    ret = extraer_retencion()
    persistir_staging(ret, 'Ext_RetencionPostClase')
    print("Datos de retencion en staging")

    rot = extraer_rotacion()
    persistir_staging(rot, 'Ext_RotacionEquipos')
    print("Datos de rotacion de equipos en staging")

    uso = extraer_uso()
    persistir_staging(uso, 'Ext_UsoEquiposCardio')
    print("Datos de uso de equipos de cardio en staging")

    cargar_asistencia_clases()
    print("Datos de asistencia cargados al sor")
    
except:
    traceback.print_exc()
finally:
    pass