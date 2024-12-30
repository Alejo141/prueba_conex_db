import streamlit as st
import mysql.connector

# Función para conectar a la base de datos
def conectar_a_base_datos():
    return mysql.connector.connect(
        host="localhost",      # XAMPP utiliza 'localhost'
        user="root",           # Usuario predeterminado de MySQL en XAMPP
        password="",           # Contraseña predeterminada está vacía
        database="dbprueba"  # Nombre de la base de datos creada
    )

# Función para obtener datos de la tabla
def obtener_datos():
    conexion = conectar_a_base_datos()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios")
    resultados = cursor.fetchall()
    conexion.close()
    return resultados

# Interfaz de Streamlit
st.title("Conexión Streamlit con XAMPP")

if st.button("Mostrar usuarios"):
    datos = obtener_datos()
    if datos:
        st.write("Usuarios registrados:")
        st.dataframe(datos)
    else:
        st.write("No hay datos disponibles.")
