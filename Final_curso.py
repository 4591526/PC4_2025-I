# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta 
# o abrimos el folder desde visual Studio Code 


# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
# python -m venv .venv
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit 
# y observaremos la página web que se está generando en este script.

# Luego activamos el entorno virtual.
# En Windows:
# .venv\Scripts\activate
# En MacOS/Linux:
# source .venv/bin/activate

# Acontinuación instalamos Streamlit 
# pip install Streamlit

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu computadora, no en Jupyter Notebook.
# python -m streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
# streamlit run your_script.py
# python -m streamlit run your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Creamos una barra lateral
sidebar = st.sidebar

# Si usas el siguiente código mostrará un título en la aplicación Streamlit. 
# st.title("Nombre de tu blog"): Esta línea está creando un título en la aplicación web.
# Pero, a diferencia de st.markdown, el texto estará alineado a la izquierda y no podrás cambiar el color del texto.

# La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
st.markdown("<h1 style='text-align: center;'>Blog semestre 2025 - I</h1>", unsafe_allow_html=True)

# <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
# La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
# el atributo style se utiliza para agregar estilos CSS. 
# En este caso, el texto está alineado al centro (text-align: center;). 
# El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

# unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad. 
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

# Creamos dos columnas separadas para la imagen y el texto
col1, col2 = st.columns(2)

# col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
# La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
# Las columnas creadas se asignan a las variables col1 y col2.

# En la primera columna colocamos la imagen
col1.image("lego_luisa.jpg", caption='Arte con lego', width=300)

texto = """
Soy Luisa Gomez, soy egresada de Lingüística de la PUCP. Actualmente, estoy en mi penúltimo ciclo de la maestría en Lingüística. 
Mis intereses están ligados a la lingüística computacional, la psicolingüística y el estudio de lenguas originarias. 
Mi tesis de maestría está orientado en generar un clasificador automático de lenguas y analizar la distribución de las lenguas aisladas tomando en cuenta la base de datos de Grambank.
Asimismo, buscaré responder qué sucede con las lenguas aisladas que en la literatura se menciona que son peculiares al no compartir rasgos con lenguas que sí conforman una familia lingüística. 
Por otro lado, fuera del ambito académico, soy capricornio. Disfruto de la música por la letra y las melodías, me gustan los legos, tejer, jugar sudoku y leer.
Realizo contenido de difusión sobre temas de literatura en medios digitales junto con egresados de literatura.
"""

# Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
# Mostramos el texto
col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

# Agregamos un subtítulo
st.markdown("<h2 style='text-align: center;'>Un breve mensaje para ustedes 💻</h2>", unsafe_allow_html=True)

# Agregar un  texto para la respuesta
texto_2 = """
Ha sido muy grato ser su jefa de prácticas este semestre. Fueron un grupo muy diverso, en su mayoría entusiasta y comprometido.
Gracias por tomarse el tiempo de dejar comentarios en la encuesta docente. Leerlos me sacó sonrisas y también me permite seguir creciendo.
Me alegra haber contribuido a su aprendizaje y que se hayan sentido acompañados en el proceso.
Al igual que yo dicté las clases, también aprendí de ustedes al resolver sus dudas e indagar en sus intereses.
El mejor consejo que puedo darles es que no se queden con las dudas y que organicen sus tiempos para evitar la procrastinación.
No se olviden de disfrutar el proceso de aprendizaje y de celebrar cada uno de sus logros, por pequeños que parezcan.
Caer, equivocarse y errar son parte del camino, pero nada de eso define el resultado final.
El verdadero reto está en levantarse y aprender de cada error.
Les deseo lo mejor en lo que viene. Sigan confiando en sus capacidades.
"""

# Mostramos el texto
st.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_2}</div>", unsafe_allow_html=True)

# <div style='text-align: justify; font-size: 15px;'>{texto_2}</div>: Esta es una cadena de código HTML.
# La etiqueta <div> se utiliza para agrupar contenido en HTML.
# En este caso, el texto está justificado (text-align: justify;).
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto_2.
# f"": Esta es una cadena de formato en Python.
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena.
# En este caso, {texto_2} se reemplaza por el valor de la variable texto_2.

# Ahora agregamos un video a mi blog donde explico algún tema de las clases
# Agregamos un subtítulo
st.markdown("<h2 style='text-align: center;'>¡Dale play! </h2>", unsafe_allow_html=True)
# <h2 style='text-align: center;'>Explicación de un tema de las clases 📚</h2>: Esta es una cadena de código HTML
# La etiqueta <h2> se utiliza para el encabezado secundario de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h2> ("A continuación una pequeña despedida ... ") es el contenido del encabezado
# unsafe_allow_html=True: Este es un argumento opcional en la función markdown.

# Agregamos un video a la aplicación web ( menor a 20 MB)
st.video("1CCO19-2025-1.mp4")
# st.video("ppc-2024-1.mp4"): Esta línea está agregando un video a la aplicación web.

st.markdown("<h2 style='text-align: center;'>⭐ Blogs destacados del curso ⭐</h2>", unsafe_allow_html=True)

top_posts = [
    {"titulo": "El mundo de Chacabuco", "url": "https://chacabuco27.streamlit.app"},
    {"titulo": "La persona detrás de las palabras", "url": "https://pc4-20230977.streamlit.app"},
    {"titulo": "¡Hola mundo! Esta es mi bitácora en programación", "url": "https://blogpccmalenaaldazabal.streamlit.app"},
    {"titulo": "MI BLOG PERSONAL: ¡aprendí a programar!", "url": "https://pc4-miblog.streamlit.app"},
]

for i, post in enumerate(top_posts, start=1):
    st.markdown(f"{i}. [{post['titulo']}]({post['url']})")

# Agregamos un subtítulo
st.subheader("🔎 Buscador de blogs")

codigo = st.text_input("Escribe tu código")
if codigo:
    if codigo == '20151633':
        st.markdown("""
        <a href="https://pc4-emerson.streamlit.app/" target="_blank">
            <button style='padding:10px 18px; font-size:16px; cursor:pointer;'>LA BITÁCORA DE EMERSON</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    elif codigo == '20193527':
        st.markdown("""
        <a href="https://pc4-diegoparedes-2025-1.streamlit.app" target="_blank">
            <button style='padding:10px 18px; font-size:16px; cursor:pointer;'>BLOG PERSONAL</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    elif codigo == '20211626': ##
        st.markdown("""
        <a href="https://myguel86pc4.streamlit.app" target="_blank">
            <button style='padding:10px 18px; font-size:16px; cursor:pointer;'>Python y yo 🥵</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    elif codigo == '20212263':
        st.markdown("""
        <a href="https://pc4-pensamiento.streamlit.app" target="_blank">
            <button style='padding:10px 18px; font-size:16px; cursor:pointer;'>Publicista Codificando</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    elif codigo == '20221575':
        st.markdown("""
        <a href="https://pc4blog.streamlit.app" target="_blank">
            <button style='padding:10px 18px; font-size:16px; cursor:pointer;'>Mente en Movimiento</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    elif codigo == '20221841':###
        st.markdown("""
        <a href="https://blognath.streamlit.app" target="_blank">
            <button style='padding:10px 18px; font-size:16px; cursor:pointer;'>Futura publicista vs Python</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    elif codigo == '20222931':
        st.markdown("""
        <a href="https://blog-diegozevallos.streamlit.app" target="_blank">
            <button style='padding:10px 18px; font-size:16px; cursor:pointer;'>Mi computadora se malogró</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    elif codigo == '20225093':
        st.markdown("""
        <a href="https://chacabuco27.streamlit.app" target="_blank">
            <button style='padding:10px 18px; font-size:16px; cursor:pointer;'>El mundo de Chacabuco 📝</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    elif codigo == '20230400': ###
        st.markdown("""
        <a href="https://blogpc4camille.streamlit.app" target="_blank">
            <button style='padding:10px 18px; font-size:16px; cursor:pointer;'>El server de Camille</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    elif codigo == '20230457':
        st.markdown("""
        <a href="https://fx85wuzqge8lnfwxtvqzne.streamlit.app" target="_blank">
            <button style='padding:10px 18px; font-size:16px; cursor:pointer;'>gis blog :3</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    elif codigo == '20230532':
        st.markdown("""
        <a href="https://blog-abigailuceda.streamlit.app" target="_blank">
            <button style='padding:10px 18px; font-size:16px; cursor:pointer;'>Abi's space :)</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    elif codigo == '20230654':###
        st.markdown("""
        <a href="https://blog-pcc.streamlit.app" target="_blank">
            <button style='padding:10px 18px; font-size:16px; cursor:pointer;'>¡Sandra, print 'Hola mundo'!</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    elif codigo == '20230836':
        st.markdown("""
        <a href="https://alejandro-blog-primera-vez.streamlit.app" target="_blank">
            <button style='padding:10px 18px; font-size:16px; cursor:pointer;'>Un poco de mi Mundo 🌍</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    elif codigo == '20230977':
        st.markdown("""
        <a href="https://pc4-20230977.streamlit.app" target="_blank">
            <button style='padding:10px 18px; font-size:16px; cursor:pointer;'>La persona detrás de las palabras 💗</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    elif codigo == '20231005':###
        st.markdown("""
        <a href="https://quieresvermipc4.streamlit.app" target="_blank">
            <button style='padding:10px 18px; font-size:16px; cursor:pointer;'>mmmmeeenna_'s blog C:</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    elif codigo == '20231306':
        st.markdown("""
        <a href="https://elcomicdeadri.streamlit.app" target="_blank">
            <button style='padding:10px 18px; font-size:16px; cursor:pointer;'>💥El cómic de Adri💥</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    elif codigo == '20232102':
        st.markdown("""
        <a href="https://pythonnoesunaserpiente.streamlit.app" target="_blank">
            <button style='padding:10px 18px; font-size:16px; cursor:pointer;'>Python no es solo una serpiente</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    elif codigo == '20232189':###
        st.markdown("""
        <a href="https://adriblog.streamlit.app" target="_blank">
            <button style='padding:10px 18px; font-size:16px; cursor:pointer;'>Adriblog🎀</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    elif codigo == '20232271':
        st.markdown("""
        <a href="https://joaolandiapc4.streamlit.app" target="_blank">
            <button style='padding:10px 18px; font-size:16px; cursor:pointer;'>¡Bienvenidos a Joaolandia 🪐!</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    elif codigo == '20232321':
        st.markdown("""
        <a href="https://pc4-blog-jesusquiroga.streamlit.app" target="_blank">
            <button style='padding:10px 18px; font-size:16px; cursor:pointer;'>Jesus Quiroga blog :)</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    elif codigo == '20232359': ###
        st.markdown("""
        <a href="https://pc4-miblog.streamlit.app" target="_blank">
            <button style='padding:10px 18px; font-size:16px; cursor:pointer;'>MI BLOG PERSONAL: ¡aprendí a programar! 👩‍💻</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    elif codigo == '20232462':
        st.markdown("""
        <a href="https://blogpccmalenaaldazabal.streamlit.app" target="_blank">
            <button style='padding:10px 18px; font-size:16px; cursor:pointer;'>¡Hola mundo! Esta es mi bitácora en programación 📝💻</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    elif codigo == '20233836':
        st.markdown("""
        <a href="https://blog-adrianita.streamlit.app" target="_blank">
            <button style='padding:10px 18px; font-size:16px; cursor:pointer;'>Adrianita sobrevive a Python</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    elif codigo == '20234059':
        st.markdown("""
        <a href="https://un-pedacito-de-mi-para-el-mundo.streamlit.app" target="_blank">
            <button style='padding:10px 18px; font-size:16px; cursor:pointer;'>print('Blog Mi Experiencia Personal')</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    elif codigo == '20253389':
        st.markdown("""
        <a href="https://marcelaismodes.streamlit.app" target="_blank">
            <button style='padding:10px 18px; font-size:16px; cursor:pointer;'>Crónicas de una publicista perdida en el mundo de Python 👩🏻‍💻</button>
        </a>
        """,
        unsafe_allow_html=True
    )
    else:
        st.write("Código incorrecto")

## Proyectos finales
st.markdown("<h2 style='text-align: center;'> 🖥️ Proyectos finales 💻 </h2>", unsafe_allow_html=True)

proyectos = [
    {"titulo": "Soundmood", "url": "https://soundmood-h2ir2vipiseuvaqcjdvett.streamlit.app"},
    {"titulo": "Ecos del Perú", "url": "https://ecosdelperu.streamlit.app"},
    {"titulo": "Fonkilla: ¿Dónde comer en PUCP?", "url": "https://trabajo-final-pensamiento.streamlit.app"},
    {"titulo": "ANATOMÍA DE UN ÍCONO: Explorando la discografía de Taylor Swift", "url": "https://discografia-taylor-swift.streamlit.app"},
    {"titulo": "Descubre tu match musical entre María Becerra y Taylor Swift", "url": "https://descubre-tu-match-musical-entre-maria-becerra-y-taylor-swift.streamlit.app"},
    {"titulo": "Bits & Beats: Análisis de usuarios Spotify 2023", "url": "https://bitsandbeats.streamlit.app/"},
    {"titulo": "Escena Cero", "url": "https://escena-cero.streamlit.app"},
    {"titulo": "¿No son 24 demasiadas?: La desigualdad de contenido entre las 24 integrantes del grupo tripleS. Un análisis de datos sobre su primer año como grupo completo.", "url": "https://triples24mediaanalysis.streamlit.app"},
    {"titulo": "Buscador de Chocolates", "url": "https://quierescomerchocolateaaaaa.streamlit.app"},
    {"titulo": "¡Hola Aitaner!", "url": "https://hola-aitaner.streamlit.app"},
    {"titulo": "Portal de Transparencia Electoral 2026", "url": "https://bajolalupa.streamlit.app"},
    {"titulo": "Zona Gamer", "url": "https://zonagamer.streamlit.app"},
    {"titulo": "Análisis Epidemiológico de Piura", "url": "https://emersonfinal.streamlit.app"},
]

for i, post in enumerate(proyectos, start=1):
    st.markdown(f"{i}. [{post['titulo']}]({post['url']})")

# Agregamos un subtítulo en la barra lateral
sidebar.markdown("<h1 style='text-align: center;'>Enlaces importantes</h1>", unsafe_allow_html=True)


repositorio = f'<a href="https://github.com/4591526/1CCO19-2025/tree/main/2025-I" target="_blank"><button>Repositorio del curso</button></a>'
pagina = f'<a href="https://pcc-interactivo.streamlit.app" target="_blank"><button>Curso interactivo</button></a>'
libreria1 = f'<a href="https://matplotlib.org/stable/gallery/index.html" target="_blank"><button>Matplotlib</button></a>'
libreria2 = f'<a href="https://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html" target="_blank"><button>WordCloud</button></a>'
libreria3 = f'<a href="https://python-visualization.github.io/folium/latest/getting_started.html" target="_blank"><button>Folium</button></a>'
libreria4 = f'<a href="https://seaborn.pydata.org/examples/index.html" target="_blank"><button>Seaborn</button></a>'
libreria5 = f'<a href="https://plotly.com/python/plotly-express/" target="_blank"><button>Plotly Express</button></a>'
libreria6 = f'<a href="https://streamlit.io" target="_blank"><button>Streamlit</button></a>'
libreria7 = f'<a href="https://www.nltk.org/howto/corpus.html" target="_blank"><button>NLTK</button></a>'
programa = f'<a href="https://code.visualstudio.com" target="_blank"><button>Visual Studio Code</button></a>'

with st.sidebar:
    st.markdown(repositorio, unsafe_allow_html=True)
    st.markdown(pagina, unsafe_allow_html=True)
    st.markdown(libreria1,  unsafe_allow_html=True)
    st.markdown(libreria2,  unsafe_allow_html=True)
    st.markdown(libreria3,  unsafe_allow_html=True)
    st.markdown(libreria4,  unsafe_allow_html=True)
    st.markdown(libreria5,  unsafe_allow_html=True)
    st.markdown(libreria6,  unsafe_allow_html=True)
    st.markdown(libreria7,  unsafe_allow_html=True)
    st.markdown(programa,  unsafe_allow_html=True)
