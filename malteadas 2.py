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

# Función auxiliar para transformar números en formato de dinero "350,00$"
def formatear_dinero(cantidad):
    # Toma el número, lo redondea a 2 decimales, cambia el punto por coma y le pone el $ al final
    return f"{cantidad:,.2f}".replace(".", ",").replace(",", ".", f"{cantidad:,.2f}".count(",") - 1) + "$"

# Truco manual más seguro para el formato en español:
def formato_moneda(valor):
    return f"{valor:.2f}".replace(".", ",") + "$"

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
            # 1. VALIDACIÓN DEL NOMBRE (Solo letras y espacios)
            if nombre_input.strip() == "" or not nombre_input.replace(" ", "").isalpha():
                st.error("⚠️ Por favor ingresa un nombre válido (solo letras).")
            
            # 2. VALIDACIÓN DE LAS MALTEADAS (Evita texto o valores vacíos)
            elif cantidad_input is None or str(cantidad_input).strip() == "":
                st.error("⚠️ Por favor ingresa una cantidad válida de malteadas (solo números).")
            else:
                # Lógica de bono
                bruto = SUELDO_BASE + BONO_PRODUCTIVIDAD if cantidad_input >= META_INDIVIDUAL else SUELDO_BASE
                neto = calcular_sueldo_neto(bruto)
                
                # GUARDAR EN LA "BASE DE DATOS"
                nuevo_registro = {
                    "Nombre": nombre_input.strip(),
                    "Ventas": int(cantidad_input),
                    "Sueldo Neto": formato_moneda(neto) # Guardamos directamente con el formato 350,00$
                }
                st.session_state.db_empleados.append(nuevo_registro)
                st.success(f"✅ {nombre_input} registrado con éxito.")

# --- REPORTE FINAL Y BASE DE DATOS ---
else:
    st.subheader("📊 Reporte Final y Base de Datos")
    
    # Convertimos la lista en un DataFrame (Tabla profesional)
    df = pd.DataFrame(st.session_state.db_empleados)
    st.table(df) # Muestra la base de datos con los sueldos en "350,00$"

    # Para hacer operaciones matemáticas en el reporte final, limpiamos temporalmente el formato
    total_v = df["Ventas"].sum()
    
    # Calculamos la nómina total sumando los netos puros de la sesión de nuevo
    valores_netos = []
    for emp in st.session_state.db_empleados:
        # Recalculamos rápido para los totales numéricos del reporte
        bruto = SUELDO_BASE + BONO_PRODUCTIVIDAD if emp["Ventas"] >= META_INDIVIDUAL else SUELDO_BASE
        valores_netos.append(calcular_sueldo_neto(bruto))
        
    total_n = sum(valores_netos)
    inv_final = INVENTARIO_INICIAL - total_v
    
    col1, col2 = st.columns(2)
    col1.metric("Total Ventas", f"{total_v} und")
    col1.metric("Promedio de Ventas", f"{total_v / CANTIDAD_EMPLEADOS:.1f} und")
    col2.metric("Nómina Total", formato_moneda(total_n)) # Muestra ej: 2100,00$
    col2.metric("Inventario Restante", f"{inv_final} und")

    if inv_final < 60:
        st.warning("⚠️ ALERTA: Reponer inventario inmediato.")

    if st.button("Reiniciar Sistema"):
        st.session_state.db_empleados = []
        # Limpieza limpia compatible con navegadores sin forzar bugs visuales
        st.write("Sistema reiniciado. Registre nuevos empleados arriba.")