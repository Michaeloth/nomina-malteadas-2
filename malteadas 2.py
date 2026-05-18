import streamlit as st
import pandas as pd # Para manejar la base de datos

# --- CONSTANTES ---
SUELDO_BASE = 350.0
BONO_PRODUCTIVIDAD = 40.0
TASA_RETENCION = 0.05
META_INDIVIDUAL = 20
CANTIDAD_EMPLEADOS = 6
INVENTARIO_INICIAL = 400

def calcular_sueldo_neto(monto_bruto):
    return monto_bruto - (monto_bruto * TASA_RETENCION)

st.set_page_config(page_title="Nómina Michaeloth", page_icon="🥤")
st.title("🥤 Administración - Malteadas Michaeloth")

# --- LÓGICA DE "BASE DE DATOS" (Session State) ---
if 'db_empleados' not in st.session_state:
    st.session_state.db_empleados = [] # Aquí se guardará todo

# --- FORMULARIO ---
if len(st.session_state.db_empleados) < CANTIDAD_EMPLEADOS:
    st.subheader(f"Registro: Empleado #{len(st.session_state.db_empleados) + 1} de {CANTIDAD_EMPLEADOS}")
    
    with st.form(key='mi_formulario', clear_on_submit=True): # clear_on_submit limpia el texto al enviar
        nombre_input = st.text_input("Nombre del empleado:")
        cantidad_input = st.number_input("Malteadas vendidas:", min_value=0, step=1)
        
        boton_enviar = st.form_submit_button("Registrar Empleado")
        
        if boton_enviar:
            # Validación de solo letras
            if nombre_input.strip() == "" or not nombre_input.replace(" ", "").isalpha():
                st.error("⚠️ Por favor ingresa un nombre válido (solo letras).")
            else:
                # Lógica de bono
                bruto = SUELDO_BASE + BONO_PRODUCTIVIDAD if cantidad_input >= META_INDIVIDUAL else SUELDO_BASE
                neto = calcular_sueldo_neto(bruto)
                
                # GUARDAR EN LA "BASE DE DATOS"
                nuevo_registro = {
                    "Nombre": nombre_input.strip(),
                    "Ventas": cantidad_input,
                    "Sueldo Neto": round(neto, 2)
                }
                st.session_state.db_empleados.append(nuevo_registro)
                st.success(f"✅ {nombre_input} registrado con éxito.")
                st.rerun() # Recarga para mostrar el siguiente número de empleado

# --- REPORTE FINAL Y BASE DE DATOS ---
else:
    st.subheader("📊 Reporte Final y Base de Datos")
    
    # Convertimos la lista en un DataFrame (Tabla profesional)
    df = pd.DataFrame(st.session_state.db_empleados)
    st.table(df) # Muestra la base de datos en pantalla

    # Cálculos finales
    total_v = df["Ventas"].sum()
    total_n = df["Sueldo Neto"].sum()
    inv_final = INVENTARIO_INICIAL - total_v
    
    col1, col2 = st.columns(2)
    col1.metric("Total Ventas", total_v)
    col1.metric("Promedio", f"{df['Ventas'].mean():.2f}")
    col2.metric("Nómina Total", f"${total_n:.2f}")
    col2.metric("Inventario Restante", inv_final)

    if inv_final < 60:
        st.warning("⚠️ ALERTA: Reponer inventario.")

    if st.button("Reiniciar Sistema"):
        st.session_state.db_empleados = []
        st.rerun()