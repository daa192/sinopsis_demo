# Import Libraries
import streamlit as st
from streamlit_extras.dataframe_explorer import dataframe_explorer
import pandas as pd

# Set Page Config
st.set_page_config(
    page_title="Lista de Precios de Productos en Miami :beach_with_umbrella:",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Sidebar
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

# Set Title
st.header("Lista de Precios de Productos en Miami :beach_with_umbrella:", divider = "grey")

# Set Tagline
st.markdown("*¡Mejora tu estrategia de precios y crece tus ventas!*")

# Set Welcome Text
welcome_text = '''
Bienvenidos a nuestro **demo** de la base de datos de precios mas completa en Miami.
Nos complace tenerlos aquí para mostrarles cómo nuestra innovadora solución de datos puede revolucionar la gestión y el análisis de la información en su empresa. 
'''
st.markdown(welcome_text)

# Set Instructions Text
inst_text = '''
Cómo utilizar la tabla de datos en el sitio web:
- Acceder a la tabla: Desplázate hacia abajo para encontrar la tabla de datos.
- Filtrar datos: Usa los cuadros de búsqueda o menús desplegables en la parte superior de cada columna.
- Descargar datos: Usa el boton de descargar en la parte de de abajo de la tabla de datos.
'''
st.markdown(inst_text)

# Set Data Url
dataset_url = "/users/diegoarguello/superpuntos/Product_Data_Pipeline/Pricing_Data_Final.csv"

# Read CSV
@st.cache_data
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)

# Create Df
df = get_data()

# Fix nulls
df['Fecha'] = df['Fecha'].fillna('N/A')
df['Nombre del Comercio'] = df['Nombre del Comercio'].fillna('N/A')
df['Direccion del Comercio'] = df['Direccion del Comercio'].fillna('N/A')
df['Vecindario del Comercio'] = df['Vecindario del Comercio'].fillna('N/A')
df['Area del Comercio'] = df['Area del Comercio'].fillna('N/A')
df['Codigo Postal del Comercio'] = df['Codigo Postal del Comercio'].fillna('N/A')
df['Categoria del Comercio'] = df['Categoria del Comercio'].fillna('N/A')
df['Web del Comercio'] = df['Web del Comercio'].fillna('N/A')
df['Descripcion del Producto'] = df['Descripcion del Producto'].fillna('N/A')
df['SKU del Producto'] = df['SKU del Producto'].fillna('N/A')
df['UoM del Producto'] = df['UoM del Producto'].fillna('N/A')
df['Categoria del Producto'] = df['Categoria del Producto'].fillna('N/A')

# Fix data types
df['Telefono del Comercio'] = df['Telefono del Comercio'].astype(str)

# Delete negatives
df = df[df['Precio Unitario del Producto']>0]

# Drop dups
df = df.drop_duplicates()

# Drop
df = df.drop('Cantidad Total', axis = 1)

# Set Subtitle
st.subheader("Lista de Precios")
    
# Create 3 Columns for KPIs
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

# Set KPI 1
kpi1.metric(
    label="Num. de Categorias",
    value=round(df['Categoria del Producto'].nunique())
)

# Set KPI 2
kpi2.metric(
    label="Num. de Puntos de Venta",
    value=round((df['Nombre del Comercio']+df['Direccion del Comercio']).nunique())
)

# Set KPI 3
kpi3.metric(
    label="Num. de Productos",
    value=round(df['Descripcion del Producto'].nunique())
)

# Set KPI 4
kpi4.metric(
    label="Num. de Precios",
    value=round(df['Precio Unitario del Producto'].shape[0])
)

# Create df
filtered_df = dataframe_explorer(df, case=False)

# Show df
st.dataframe(filtered_df, 
             use_container_width=True,
             column_config={
                 "Web del Comercio": st.column_config.LinkColumn("Web del Comercio"),
                 "Precio Unitario del Producto": st.column_config.NumberColumn(format='$%.2f')
             })

st.markdown("*Esta tabla es solo una demostración y no representa la base de datos completa de precios de productos en Miami. Los datos mostrados son solo ejemplos y pueden no reflejar la información más actualizada disponible en nuestra plataforma. Para acceder a la base de datos completa y obtener información en tiempo real, por favor, suscríbase a nuestro servicio.*")

# Create button
@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode("utf-8")

csv = convert_df(df)

st.download_button(
    label="Descargar CSV",
    data=csv,
    file_name="df.csv",
    mime="text/csv",
)

## Create a sample DataFrame with latitude and longitude values
data = pd.DataFrame({
    'latitude': [37.7749, 34.0522, 40.7128],
    'longitude': [-122.4194, -118.2437, -74.0060]
})
 
# Add the highlight points to the map
#st.map(data, highlight)
 
# Set subtitle
st.subheader("Preguntas Frecuentes")

st.markdown("**1. ¿Qué es la base de datos de precios de productos en Miami?** La base de datos de precios de productos en Miami es una recopilación en tiempo real de los precios de diversos productos en tiendas y supermercados de la ciudad de Miami.")

st.markdown("**2. ¿Qué tipo de productos están incluidos en la base de datos?** La base de datos incluye una amplia variedad de productos, desde alimentos y bebidas hasta productos de limpieza y artículos de cuidado personal.")

st.markdown("**3. ¿Con qué frecuencia se actualizan los precios en la base de datos?** Los precios se actualizan en tiempo real, lo que garantiza que siempre tenga acceso a la información más reciente.")

st.markdown("**4. ¿Puedo filtrar los datos por tienda o por categoría de producto?** Sí, nuestra plataforma le permite filtrar los datos por tienda, categoría de producto, y otros criterios específicos para facilitar su búsqueda.")

st.markdown("**5. ¿Qué beneficios ofrece utilizar esta base de datos?** Utilizar nuestra base de datos le permite comparar precios fácilmente, identificar tendencias de precios, y tomar decisiones de compra más informadas.")

st.markdown("**6. ¿Cómo puedo suscribirme al servicio?** Puede suscribirse al servicio poniendose en contacto con nosotros en info@sinopsisdata.com.")

st.divider()

st.markdown("*&copy; 2024 Sinopsis Data, LLC. All Rights Reserved. Unauthorized use and/or duplication of this material without express and written permission from this site’s author and/or owner is strictly prohibited.*")