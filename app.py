import streamlit as st

st.set_page_config(
    page_title="Alba Romero | Data Portfolio",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
            
#MainMenu {
    visibility: hidden;
}

header[data-testid="stHeader"] {
    display: none;
}

footer {
    visibility: hidden;
}
            
header[data-testid="stHeader"]{
    background: transparent;
    height:0;
}

div[data-testid="stToolbar"]{
    background: transparent !important;
}

div[data-testid="stDecoration"]{
    background: transparent;
}

button[kind="header"]{
    background: rgba(20,20,30,.35) !important;
    backdrop-filter: blur(12px);
    border:1px solid rgba(255,255,255,.08) !important;
    border-radius:12px !important;
}

[data-testid="stAppViewContainer"]{
    border:none;
}

.stApp{
    background:
        radial-gradient(circle at top left, rgba(124,133,243,.20), transparent 35%),
        radial-gradient(circle at bottom right, rgba(0,200,180,.12), transparent 30%),
        linear-gradient(180deg,#11151f 0%,#0e1117 100%);
}

.block-container{
    width: clamp(320px, 92vw, 1600px);
    margin:auto;
    padding:2rem 2rem 4rem;
}

.nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.9rem 0;
    margin-bottom: 3rem;
}

.logo {
    font-weight: 800;
    font-size: 1.1rem;
    letter-spacing: 0.08em;
    color: #ffffff;
}

.nav-links a {
    color: #b7b9d8;
    text-decoration: none;
    margin-left: 1.4rem;
    font-size: 0.95rem;
}

.hero{
    min-height:85vh;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    text-align:center;
}

.first-section{
    margin-top:8rem;
}

.badge {
    display: inline-block;
    padding: 0.45rem 0.8rem;
    border: 1px solid rgba(124,133,243,0.45);
    border-radius: 999px;
    color: #c7cbff;
    background: rgba(124,133,243,0.12);
    font-size: 0.9rem;
    margin-bottom: 1.2rem;
}

.hero h1 {
    font-size: clamp(3rem, 7vw, 5.8rem);
    line-height: 0.95;
    font-weight: 900;
    margin: 0;
    color: #ffffff;
}

.gradient-text {
    background: linear-gradient(90deg, #ffffff, #8f97ff, #72f0d1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    font-size: 1.25rem;
    color: #b7b9d8;
    max-width: 760px;
    margin: 1.5rem auto 0 auto;
    line-height: 1.7;
    text-align: center;
}

.cta-row {
    margin-top: 2rem;
}

.cta {
    display: inline-block;
    padding: 0.85rem 1.1rem;
    margin-right: 0.8rem;
    border-radius: 12px;
    text-decoration: none;
    font-weight: 700;
}

.cta-primary {
    background: #7c85f3;
    color: #ffffff !important;
}

.cta-secondary {
    border: 1px solid rgba(255,255,255,0.18);
    color: #ffffff !important;
}

.section {
    margin-top: 5rem;
}


.section-title {
    font-size: 2rem;
    font-weight: 850;
    color: #ffffff;
    margin-bottom: 0.5rem;
}

.section-subtitle {
    color: #aeb1d0;
    margin-bottom: 1.8rem;
}

.card {
    padding: 1.4rem;
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 22px;
    background: rgba(255,255,255,0.045);
    backdrop-filter: blur(10px);
    height: 100%;
}

.card h3 {
    color: #ffffff;
    margin-top: 0;
}

.card p {
    color: #b7b9d8;
    line-height: 1.65;
}

.tag {
    display: inline-block;
    padding: 0.32rem 0.62rem;
    border-radius: 999px;
    background: rgba(124,133,243,0.16);
    color: #d6d8ff;
    margin: 0.2rem 0.2rem 0.2rem 0;
    font-size: 0.82rem;
}

.hero-metrics {
    display: flex;
    justify-content: center;
    gap: 1.5rem;
    margin-top: 3rem;
    width: 100%;
    max-width: 820px;
}

.metric-box {
    text-align: center;
    padding: 1.2rem 2.2rem;
    border: 1px solid rgba(124,133,243,0.22);
    border-radius: 18px;
    background: rgba(124,133,243,0.07);
    backdrop-filter: blur(12px);
    flex: 1;
    transition: border-color 0.25s, background 0.25s;
}

.metric-box:hover {
    border-color: rgba(124,133,243,0.55);
    background: rgba(124,133,243,0.14);
}

.metric-number {
    font-size: 1.5rem;
    font-weight: 800;
    letter-spacing: 0.04em;
    background: linear-gradient(90deg, #ffffff, #a5aaff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.metric-label {
    color: #aeb1d0;
    font-size: 0.82rem;
    margin-top: 0.35rem;
    letter-spacing: 0.03em;
}

.about-grid {
    display: grid;
    grid-template-columns: 1.5fr 1fr;
    gap: 1.5rem;
    margin-top: 0;
}

.about-story {
    padding: 2rem 2.2rem;
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 22px;
    background: rgba(255,255,255,0.045);
    backdrop-filter: blur(10px);
}

.story-block {
    display: flex;
    gap: 1.2rem;
    margin-bottom: 1.6rem;
    align-items: flex-start;
}

.story-block:last-child {
    margin-bottom: 0;
}

.story-dot {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1rem;
    flex-shrink: 0;
    margin-top: 0.1rem;
}

.dot-psych  { background: rgba(114,240,209,0.15); border: 1px solid rgba(114,240,209,0.35); }
.dot-code   { background: rgba(143,151,255,0.15); border: 1px solid rgba(143,151,255,0.35); }
.dot-work   { background: rgba(124,133,243,0.15); border: 1px solid rgba(124,133,243,0.40); }

.story-text p {
    color: #b7b9d8;
    line-height: 1.7;
    margin: 0;
    font-size: 0.95rem;
}

.about-traits {
    padding: 2rem 2.2rem;
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 22px;
    background: rgba(255,255,255,0.045);
    backdrop-filter: blur(10px);
    display: flex;
    flex-direction: column;
}

.traits-title {
    font-weight: 700;
    font-size: 1rem;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    margin-bottom: 1.4rem;
    color: #aeb1d0;
}

.trait-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.75rem 0;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    color: #e0e2ff;
    font-size: 0.93rem;
}

.trait-item:last-child {
    border-bottom: none;
}

.trait-icon {
    width: 28px;
    height: 28px;
    border-radius: 8px;
    background: rgba(124,133,243,0.15);
    border: 1px solid rgba(124,133,243,0.28);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.8rem;
    flex-shrink: 0;
}

.footer {
    margin-top: 5rem;
    padding-top: 2rem;
    border-top: 1px solid rgba(255,255,255,0.1);
    color: #9da0bf;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)


# NAV
st.markdown("""
<div class="nav">
    <div class="logo">ALBA ROMERO</div>
    <div class="nav-links">
        <a href="#sobre-mi">Conóceme</a>
        <a href="#stack">Stack</a>
        <a href="#proyectos">Proyectos</a>
        <a href="#contacto">Contacto</a>
    </div>
</div>
""", unsafe_allow_html=True)


# HERO
st.markdown("""
<section class="hero">
    <div class="badge">Junior Data Engineer · Data Quality · Data Governance</div>
    <h1>Transformando datos en <span class="gradient-text">historias que deciden.</span></h1>
    <p class="subtitle">
        Soy Alba Romero, Junior Data Engineer especializada en calidad y gobierno del dato dentro del sector financiero. Trabajo diariamente con SQL, AWS Athena y SageMaker para analizar datos, investigar incidencias y mejorar la fiabilidad de la información. Mi objetivo es seguir creciendo como Data Engineer, profundizando en tecnologías cloud, procesamiento de datos y arquitecturas Big Data.
    </p>
    <div class="hero-metrics">
        <div class="metric-box">
            <div class="metric-number">Explore</div>
            <div class="metric-label">Datos y metadatos</div>
        </div>
        <div class="metric-box">
            <div class="metric-number">Analyze</div>
            <div class="metric-label">Reglas de calidad</div>
        </div>
        <div class="metric-box">
            <div class="metric-number">Improve</div>
            <div class="metric-label">Gobierno del dato</div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)


# SOBRE MÍ
st.markdown("""
<section class="section" id="sobre-mi">
    <div class="section-title">Conóceme</div>
    <div class="section-subtitle">
        Perfil técnico con sensibilidad visual, pensamiento analítico y ganas de crear productos útiles.
    </div>
</section>
""", unsafe_allow_html=True)

st.markdown("""
<div class="about-grid">
    <div class="about-story">
        <div class="story-block">
            <div class="story-dot dot-psych">🧠</div>
            <div class="story-text">
                <p>Mi camino hacia el mundo de los datos no fue el más habitual. Comencé estudiando <strong style="color:#72f0d1;">Psicología</strong>, una etapa que me ayudó a desarrollar pensamiento crítico, capacidad de análisis y una forma estructurada de afrontar los problemas.</p>
            </div>
        </div>
        <div class="story-block">
            <div class="story-dot dot-code">💻</div>
            <div class="story-text">
                <p>Años después descubrí en <strong style="color:#a5aaff;">Desarrollo de Aplicaciones Web</strong> que lo que realmente me apasionaba eran las bases de datos. SQL se convirtió en la asignatura que más disfrutaba y ese interés me llevó a especializarme en Big Data e Inteligencia Artificial.</p>
            </div>
        </div>
        <div class="story-block">
            <div class="story-dot dot-work">📊</div>
            <div class="story-text">
                <p>Actualmente trabajo en el área de <strong style="color:#c7cbff;">Calidad del Dato</strong> dentro del sector financiero, donde utilizo SQL y herramientas de AWS para analizar datos, investigar incidencias y colaborar en la mejora continua de la calidad de la información. Mi objetivo es seguir creciendo profesionalmente hasta convertirme en Data Engineer.</p>
            </div>
        </div>
    </div>
    <div class="about-traits">
        <div class="traits-title">Lo que me define</div>
        <div class="trait-item"><div class="trait-icon">🔍</div> Pensamiento analítico</div>
        <div class="trait-item"><div class="trait-icon">🗄️</div> SQL como principal herramienta</div>
        <div class="trait-item"><div class="trait-icon">✅</div> Calidad y gobierno del dato</div>
        <div class="trait-item"><div class="trait-icon">📚</div> Aprendizaje continuo</div>
        <div class="trait-item"><div class="trait-icon">☁️</div> Trabajo en entornos AWS</div>
        <div class="trait-item"><div class="trait-icon">🤝</div> Comunicación con equipos técnicos y de negocio</div>
    </div>
</div>
""", unsafe_allow_html=True)


# STACK
st.markdown("""
<section class="section" id="stack">
    <div class="section-title">Stack tecnológico</div>
    <div class="section-subtitle">
        Herramientas que uso para analizar, construir y presentar soluciones basadas en datos.
    </div>
</section>
""", unsafe_allow_html=True)

stack_cols = st.columns(4)
stack = {
    "Lenguajes": ["Python", "SQL", "JavaScript", "HTML", "CSS"],
    "Datos": ["Pandas", "NumPy", "Power BI", "Excel", "ETL"],
    "Web": ["Streamlit", "Flask", "Git", "GitHub", "APIs"],
    "Enfoque": ["Dashboards", "Data Cleaning", "Storytelling", "UX", "Automatización"]
}

for col, (title, tools) in zip(stack_cols, stack.items()):
    with col:
        tags = "".join([f"<span class='tag'>{tool}</span>" for tool in tools])
        st.markdown(f"""
        <div class="card">
            <h3>{title}</h3>
            {tags}
        </div>
        """, unsafe_allow_html=True)


# PROYECTOS
st.markdown("""
<section class="section" id="proyectos">
    <div class="section-title">Proyectos destacados</div>
    <div class="section-subtitle">
        Selección inicial. Cambia textos, enlaces y tecnologías por tus proyectos reales.
    </div>
</section>
""", unsafe_allow_html=True)

projects = [
    {
        "title": "Dashboard de Ventas",
        "desc": "Análisis interactivo de ventas, márgenes, categorías y evolución temporal para detectar patrones de negocio.",
        "tags": ["Python", "Pandas", "Streamlit", "Visualización"],
        "link": "#"
    },
    {
        "title": "Limpieza de Datos Financieros",
        "desc": "Proceso ETL para normalizar datos, tratar nulos, detectar duplicados y preparar datasets listos para análisis.",
        "tags": ["Python", "ETL", "Data Cleaning", "SQL"],
        "link": "#"
    },
    {
        "title": "Análisis de Clientes",
        "desc": "Segmentación de usuarios mediante métricas de comportamiento para apoyar decisiones comerciales.",
        "tags": ["Pandas", "KPIs", "BI", "Storytelling"],
        "link": "#"
    },
    {
        "title": "Portfolio Data App",
        "desc": "Aplicación web personal para mostrar proyectos, experiencia y evolución profesional en formato CV digital.",
        "tags": ["Streamlit", "HTML", "CSS", "UX"],
        "link": "#"
    }
]

for i in range(0, len(projects), 2):
    cols = st.columns(2)
    for col, project in zip(cols, projects[i:i+2]):
        with col:
            tags = "".join([f"<span class='tag'>{tag}</span>" for tag in project["tags"]])
            st.markdown(f"""
            <div class="card">
                <h3>{project["title"]}</h3>
                <p>{project["desc"]}</p>
                <div>{tags}</div>
                <br>
                <a class="cta cta-secondary" href="{project["link"]}">Ver proyecto</a>
            </div>
            """, unsafe_allow_html=True)


# CONTACTO
st.markdown("""
<section class="section" id="contacto">
    <div class="section-title">Contacto</div>
    <div class="section-subtitle">
        ¿Buscas un perfil junior con base técnica, criterio visual y ganas de aportar?
    </div>
    <div class="card">
        <h3>Trabajemos juntos</h3>
        <p>
            Estoy abierta a oportunidades en desarrollo web, análisis de datos,
            business intelligence y proyectos donde pueda combinar tecnología y creatividad.
        </p>
        <p>
            📧 Email: <strong>tu-email@ejemplo.com</strong><br>
            💼 LinkedIn: <strong>linkedin.com/in/tu-perfil</strong><br>
            🧑‍💻 GitHub: <strong>github.com/tu-usuario</strong>
        </p>
    </div>
</section>

<div class="footer">
    © 2026 Alba Romero · Data Portfolio
</div>
""", unsafe_allow_html=True)