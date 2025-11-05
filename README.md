# 📧 Generador de Email Automático – App Web con Python Flask

**Generador de Email Automático** es una aplicación web desarrollada con **Python (Flask)**, **HTML** y **CSS**, creada para **generar correos electrónicos personalizados de forma rápida y automática**.  
Ideal para profesores, empresas o usuarios que necesiten redactar correos con estructura profesional sin perder tiempo.

---

## 🚀 Tecnologías utilizadas

- **Python (Flask)** – Framework web ligero y eficiente  
- **HTML5** – Estructura y maquetación de la interfaz  
- **CSS3** – Estilos y diseño visual del sitio  
- **Jinja2** – Motor de plantillas para generar mensajes dinámicos  

---

## ⚙️ Instalación y configuración

Sigue estos pasos para ejecutar el proyecto localmente:

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Aaronisaias/Generador-de-Email-Automatico.git
Ingresa al directorio del proyecto:

cd Generador-de-Email-Automatico
(Opcional) Crea y activa un entorno virtual:

python -m venv venv
source venv/Scripts/activate   # En Windows
source venv/bin/activate       # En Linux o macOS
Instala las dependencias:

pip install -r requirements.txt
Ejecuta la aplicación:

python app.py
Abre tu navegador y visita:
👉 http://localhost:5000

💡 Características principales
📝 Genera automáticamente emails personalizados con datos ingresados por el usuario.

⚙️ Permite definir el asunto, destinatario y cuerpo del mensaje.

🧠 Usa plantillas dinámicas de Jinja2 para crear textos automáticos.

💾 Opción para copiar o guardar el email generado.

🎨 Interfaz simple, limpia y responsive con HTML y CSS puros.

🧱 Estructura del proyecto

📦 Generador-de-Email-Automatico
├── 📁 static           # Archivos estáticos (CSS, imágenes, etc.)
├── 📁 templates        # Archivos HTML (interfaz y plantillas de correo)
├── app.py              # Archivo principal de Flask
├── requirements.txt    # Dependencias del proyecto
└── README.md
🔧 Dependencias principales
Flask – Framework web principal

Jinja2 – Motor de plantillas HTML

🧠 Uso recomendado
Abre la aplicación en tu navegador.

Completa los campos solicitados (nombre, correo, asunto, mensaje, etc.).

Presiona el botón para generar el email automático.

Copia o guarda el resultado según necesites.

Ideal para:

Profesores que deben enviar correos a múltiples alumnos.

Emprendedores o empresas que automatizan respuestas.

Usuarios que desean ahorrar tiempo redactando emails.

📘 Recomendaciones de desarrollo
Agrega validación de campos con Flask-WTF.

Integra el envío real de emails con smtplib o Flask-Mail.

Aplica estilos modernos con Bootstrap o CSS Grid.

Añade historial de mensajes generados usando una base de datos.

🧑‍💻 Autor
Desarrollado por: Aaron Isaías Medina
📧 Contacto: medinaisaias484@gmail.com
📂 Repositorio: Generador de Email Automático
📅 Proyecto Flask – Aplicación web para generación automática de correos
