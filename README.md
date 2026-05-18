
***

# 🥤 Sistema de Gestión de Nómina e Inventario - Malteadas Michaeloth

¡Bienvenido al repositorio oficial del sistema administrativo de **Malteadas Michaeloth**! Esta es una aplicación web interactiva desarrollada en **Python** que automatiza y unifica el control de ventas de productos, el cálculo de la nómina del personal y el monitoreo del stock en almacén en tiempo real.

El proyecto ha sido diseñado pensando en la optimización del tiempo de los administradores, reduciendo el margen de error humano en cálculos financieros y asegurando que los datos clave del negocio estén siempre a la mano a través de una interfaz limpia y responsiva.

---

## 🚀 Características Principales

* **Frontend Web Interactivo:** Desarrollado completamente en un entorno web intuitivo y accesible, eliminando la clásica y tediosa consola negra.
* **Gestión Dinámica de Empleados:** Control estructurado para un ciclo secuencial de **6 empleados** por mes.
* **Base de Datos en Memoria:** Almacenamiento temporal y persistente durante la sesión (`Session State`) para consolidar reportes sin saturar el almacenamiento físico.
* **Validación Robusta de Entradas (Anti-Errores):**
    * *Filtro Alfabético:* El campo de nombres solo admite texto y espacios (bloquea números o caracteres especiales).
    * *Filtro Numérico:* El campo de ventas restringe de manera estricta la entrada de texto y asegura valores enteros limpios.
* **Cálculo Automático de Bonificaciones:** Evaluación inmediata de metas individuales (Bono de **$40.00** si el empleado supera la meta de **20 malteadas**).
* **Módulo Fiscal/Retenciones:** Subrutina modular que aplica automáticamente una retención legal del **5%** sobre el sueldo bruto total.
* **Control Inteligente de Inventario:** Resta automática de malteadas del stock inicial (**400 unidades**) con un sistema de alertas visuales si el inventario cae por debajo del nivel crítico (15% o 60 unidades).
* **Reporte Consolidado:** Generación de tablas administrativas profesionales con Pandas, promedios de rendimiento del equipo y desembolso total de la empresa.

---

## 🛠️ Tecnologías y Librerías Utilizadas

Para el desarrollo de este software de nivel profesional, se seleccionaron las siguientes herramientas del ecosistema de Python:

1.  **Streamlit:** Utilizada como el framework principal para la construcción del **Frontend y la Interfaz Web**. Permite transformar scripts de Python en aplicaciones web interactivas en cuestión de minutos sin necesidad de escribir HTML, CSS o JavaScript independientes.
2.  **Pandas:** La librería estrella en ciencia de datos. En este proyecto se utilizó para estructurar la **Base de Datos**, convirtiendo las listas dinámicas de la sesión en un `DataFrame` tabular que organiza la información de los empleados de forma elegante y profesional en pantalla.
3.  **Python Standard Libraries (`streamlit.session_state`):** Utilizada para la persistencia de datos del estado de la sesión web, simulando de manera perfecta el comportamiento de una base de datos local mientras el navegador se encuentra activo.

---

## 💻 Requisitos del Sistema

Antes de ejecutar la aplicación, asegúrate de tener instalado Python (versión 3.9 o superior) en tu sistema de cómputo.

### Instalación de Dependencias
Para que el proyecto funcione en tu entorno local, abre la terminal en la carpeta raíz del proyecto e instala las librerías necesarias con el siguiente comando:

```bash
pip install streamlit pandas
