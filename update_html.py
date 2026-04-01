import json
import re

# 30 existing + 24 new = 54 unique questions!
new_questions = [
    {
        "text": "¿Quién debe registrar las novedades operativas o disciplinarias detectadas durante el turno en la bitácora correspondiente?",
        "options": ["a. Instituciones articuladas", "b. Despacho", "c. El Analista de Operaciones (Videovigilancia)", "d. Ninguno"],
        "correct": "c. El Analista de Operaciones (Videovigilancia)"
    },
    {
        "text": "¿El objetivo del procedimiento busca precautelar la seguridad y bienestar de la ciudadanía?",
        "options": ["Verdadero", "Falso"],
        "correct": "Verdadero"
    },
    {
        "text": "Seleccione las respuestas correctas. ¿Cuál de los siguientes es un lugar de interés?",
        "options": ["a. Estaciones espaciales", "b y c. Paradas de bus y Centros de diversión", "d. Propiedad privada"],
        "correct": "b y c. Paradas de bus y Centros de diversión"
    },
    {
        "text": "Durante el monitoreo de cámaras, el evaluador debe utilizar:",
        "options": ["a. Paneo automático o control manual de la cámara", "b. El celular personal", "c. Pantallas de televisión", "d. Audífonos con música"],
        "correct": "a. Paneo automático o control manual de la cámara"
    },
    {
        "text": "¿La configuración del paneo automático se basa únicamente en la marca de la cámara?",
        "options": ["Verdadero", "Falso"],
        "correct": "Falso"
    },
    {
        "text": "¿En qué sistemas se debe modificar el nombre de la cámara para identificar la megafonía IP?",
        "options": ["a. Software de Video Vigilancia y GIS", "b. Procesador de texto", "c. Sistema de nómina", "d. Redes sociales"],
        "correct": "a. Software de Video Vigilancia y GIS"
    },
    {
        "text": "¿El alcance se limita solamente a la instalación física de las cámaras?",
        "options": ["Verdadero", "Falso"],
        "correct": "Falso"
    },
    {
        "text": "En escenarios deportivos durante eventos se recomienda:",
        "options": ["a. Apagar la cámara", "b. Monitoreo manual de graderíos", "c. Dejar en automático siempre", "d. Ninguna de las anteriores"],
        "correct": "b. Monitoreo manual de graderíos"
    },
    {
        "text": "Cuando el Evaluador detecta un incidente o emergencia debe:",
        "options": ["a. Informar al área de despacho", "b. Comunicar verbalmente al Analista de Operaciones Zonal/ Local (videovigilancia)", "c. Enviar directamente la ficha electrónica"],
        "correct": "b. Comunicar verbalmente al Analista de Operaciones Zonal/ Local (videovigilancia)"
    },
    {
        "text": "¿Qué letra se incluye en la nomenclatura de la cámara para identificar que posee servicio de megafonía IP?",
        "options": ["a. P", "b. M", "c. S", "d. V"],
        "correct": "b. M"
    },
    {
        "text": "¿El paneo debe ejecutarse con una velocidad y zoom que permita distinguir mediante visión periférica actividades de interés?",
        "options": ["Verdadero", "Falso"],
        "correct": "Verdadero"
    },
    {
        "text": "¿Una emergencia es un evento que pone en peligro la vida de las personas, los bienes o la continuidad de los servicios y requiere atención inmediata?",
        "options": ["Verdadero", "Falso"],
        "correct": "Verdadero"
    },
    {
        "text": "¿La herramienta de megafonía IP permite emitir mensajes de alerta a la ciudadanía en situaciones de emergencia?",
        "options": ["Verdadero", "Falso"],
        "correct": "Verdadero"
    },
    {
        "text": "¿Cuál es una responsabilidad dentro del alcance?",
        "options": ["a. Videovigilancia y detección de incidentes", "b. Decoración de la sala de monitoreo", "c. Limpieza de las cámaras", "d. Venta de equipos"],
        "correct": "a. Videovigilancia y detección de incidentes"
    },
    {
        "text": "El monitoreo de las cámaras de videovigilancia, la detección de eventos preventivos e incidentes, y el direccionamiento de la ficha a la(s) institución(es) articulada(s) al Servicio Integrado de Seguridad ECU 911 no forma parte del Procedimiento de Video Vigilancia.",
        "options": ["Verdadero", "Falso"],
        "correct": "Falso"
    },
    {
        "text": "¿El monitoreo del incidente finaliza inmediatamente después de enviar la ficha electrónica?",
        "options": ["Verdadero", "Falso"],
        "correct": "Falso"
    },
    {
        "text": "Los lugares de interés se identifican principalmente porque:",
        "options": ["a. Tienen mayor iluminación", "b. Son lugares con cámaras nuevas", "c. Son lugares turísticos", "d. Son zonas con mayor vulnerabilidad a delitos"],
        "correct": "d. Son zonas con mayor vulnerabilidad a delitos"
    },
    {
        "text": "¿Los eventos de emergencia están relacionados con incidentes detectados como T2 o T3?",
        "options": ["Verdadero", "Falso"],
        "correct": "Verdadero"
    },
    {
        "text": "¿La presencia de unidades de atención de emergencia puede ser considerada una actividad de interés?",
        "options": ["Verdadero", "Falso"],
        "correct": "Verdadero"
    },
    {
        "text": "¿El Evaluador de Operaciones de Videovigilancia debe justificar cualquier Cámara PTZ estática que deje sin justificación alguna?",
        "options": ["Verdadero", "Falso"],
        "correct": "Verdadero"
    },
    {
        "text": "Las cámaras térmicas deben permanecer:",
        "options": ["a. Girando continuamente", "b. Detenidas en toma panorámica", "c. En movimiento constante", "d. Solo en zoom"],
        "correct": "b. Detenidas en toma panorámica"
    },
    {
        "text": "¿Quién debe modificar el nombre de la cámara en la plataforma tecnológica para identificar la megafonía IP?",
        "options": ["a. Dirección Zonal de Tecnología y Soporte / Unidad Local de Soporte Tecnológico", "b. Policía Nacional", "c. Operadores de radio", "d. Personal de seguridad privada"],
        "correct": "a. Dirección Zonal de Tecnología y Soporte / Unidad Local de Soporte Tecnológico"
    },
    {
        "text": "El alcance del documento incluye:",
        "options": ["a. Solo la compra de equipos", "b. El conocimiento de características y parámetros de las cámaras", "c. Solo el mantenimiento", "d. Solo la instalación eléctrica"],
        "correct": "b. El conocimiento de características y parámetros de las cámaras"
    },
    {
        "text": "¿Las instituciones públicas pueden presentar manifestaciones que pongan en riesgo el edificio?",
        "options": ["Verdadero", "Falso"],
        "correct": "Verdadero"
    }
]

html_path = "d:/examen/modulo_estudio_interactivo.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Extract the existing questions
json_match = re.search(r"const questions \s*=\s*(\[\s*\{.*?\}\s*\]);", content, re.DOTALL)
if json_match:
    existing_json = json_match.group(1)
    # the existing_json is a JS object representation, let's parse it as json safely
    try:
        existing_questions = json.loads(existing_json)
    except:
        # Fallback if there are trailing commas or issues
        # Actually in HTML it was precisely generated using json.dumps! So it should work.
        existing_questions = json.loads(existing_json)
        
    # Append the newly parsed questions
    
    # Let's deduplicate text just in case (e.g. Q28 duplicate we saw earlier)
    all_q_texts = set(q['text'].strip() for q in existing_questions)
    
    for nq in new_questions:
        if nq['text'].strip() not in all_q_texts:
            existing_questions.append({
                "text": nq['text'],
                "type": "true_false" if "Verdadero" in nq['options'] else "multiple_choice",
                "options": nq['options'],
                "correct": nq['correct']
            })
            all_q_texts.add(nq['text'].strip())

    
    # We want exactly that array serialized
    new_json_str = json.dumps(existing_questions, indent=4, ensure_ascii=False)
    
    # Inject back
    new_content = content.replace(json_match.group(0), f"const questions = {new_json_str};")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Total questions merged: {len(existing_questions)}")
else:
    print("Could not find the questions array in HTML.")
