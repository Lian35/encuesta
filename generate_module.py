import json

questions = [
    {
        "text": "Para eventos de concurrencia masiva (deportivos, musicales, etc.), la ficha electrónica se debe crear con el tipo de captura \"T2\" o \"T3\" si fue detectado por el Evaluador, o si ya se tenía conocimiento previo del evento.",
        "type": "true_false",
        "options": ["Verdadero", "Falso"],
        "correct": "Verdadero"
    },
    {
        "text": "¿Cuál es el tiempo de monitoreo recomendado para las cámaras de menor índice de conflictividad?",
        "type": "multiple_choice",
        "options": ["a. 5 a 7 minutos", "b. 10 minutos", "c. 1 a 3 minutos", "d. 3 a 5 minutos"],
        "correct": "c. 1 a 3 minutos"
    },
    {
        "text": "¿Qué característica tiene el sonido emitido por los equipos de megafonía IP?",
        "type": "multiple_choice",
        "options": ["a. Es direccional", "b. Es silencioso", "c. Es omnidireccional", "d. Es automático"],
        "correct": "a. Es direccional"
    },
    {
        "text": "¿Qué actividad forma parte del alcance?",
        "type": "multiple_choice",
        "options": ["a. Configuración del paneo automático predeterminado", "b. Instalación de internet", "c. Fabricación de cámaras", "d. Diseño del edificio"],
        "correct": "a. Configuración del paneo automático predeterminado"
    },
    {
        "text": "Cuando el Evaluador detecta un incidente o emergencia debe:",
        "type": "multiple_choice",
        "options": ["a. Informar al área de despacho", "b. Enviar directamente la ficha electrónica", "c. Comunicar verbalmente al Analista de Operaciones Zonal/ Local (videovigilancia)"],
        "correct": "b. Enviar directamente la ficha electrónica"
    },
    {
        "text": "¿Cuando se detecta un incidente o emergencia, el evaluador debe comunicar verbalmente al Analista de Operaciones Zonal /Local (videovigilancia)?",
        "type": "true_false",
        "options": ["Verdadero", "Falso"],
        "correct": "Verdadero"
    },
    {
        "text": "¿Dónde se encuentra instalado el sistema de megafonía IP para emitir alertas?",
        "type": "multiple_choice",
        "options": ["a. En computadoras del centro de monitoreo", "b. En postes estratégicos de cámaras de videovigilancia", "c. En vehículos de emergencia", "d. En las oficinas administrativas"],
        "correct": "b. En postes estratégicos de cámaras de videovigilancia"
    },
    {
        "text": "El movimiento TILDEO (TILT) corresponde a:",
        "type": "multiple_choice",
        "options": ["a. Movimiento estático", "b. Movimiento vertical", "c. Movimiento circular", "d. Movimiento horizontal"],
        "correct": "b. Movimiento vertical"
    },
    {
        "text": "¿El tildeo (Tilt) verifica el movimiento de la cámara en un plano vertical de 180 grados?",
        "type": "true_false",
        "options": ["Verdadero", "Falso"],
        "correct": "Verdadero"
    },
    {
        "text": "Cámara estática que permite visualizar un área específica con un enfoque fijo.",
        "type": "multiple_choice",
        "options": ["a. Cámara fija", "b. Cámara Domo HD", "c. Cámara de Videovigilancia", "d. Cámara Domo PTZ"],
        "correct": "a. Cámara fija"
    },
    {
        "text": "El Tildeo (Tilt) rota en un plano vertical de 180 grados.",
        "type": "true_false",
        "options": ["Verdadero", "Falso"],
        "correct": "Verdadero"
    },
    {
        "text": "¿El Evaluador de Operaciones Zonal/ Local (videovigilancia) debe ingresar al sistema ECU 911 utilizando su usuario y contraseña asignados?",
        "type": "true_false",
        "options": ["Verdadero", "Falso"],
        "correct": "Verdadero"
    },
    {
        "text": "¿El Evaluador de Operaciones de Videovigilancia puede observar a través del GIS de su consola los incidentes que en ese momento hayan sido detectados por otro Evaluador de Operaciones de Videovigilancia?",
        "type": "true_false",
        "options": ["Verdadero", "Falso"],
        "correct": "Falso"
    },
    {
        "text": "¿El Analista de Operaciones de Videovigilancia o su back-up debe usar un tono de voz claro, pausado y que transmita seguridad al emitir mensajes por megafonía IP?",
        "type": "true_false",
        "options": ["Verdadero", "Falso"],
        "correct": "Verdadero"
    },
    {
        "text": "¿Qué debe hacer el Analista de Operaciones Zonal / Local (Videovigilancia) cuando se reportan novedades de hardware y software del sistema y consola por parte del Evaluador?",
        "type": "multiple_choice",
        "options": ["a. Intentar solventar las novedades por sí mismo antes de reportar", "b. Generar un ticket electrónico por medio de la plataforma GLPI de manera inmediata", "c. Esperar al cambio de turno para que el siguiente Evaluador lo reporte", "d. Notificar mediante correo electrónico al Director de Servicios, Procesos y Calidad"],
        "correct": "b. Generar un ticket electrónico por medio de la plataforma GLPI de manera inmediata"
    },
    {
        "text": "Movimiento de la cámara sobre su propio eje de izquierda a derecha o de derecha a izquierda en un plano horizontal.",
        "type": "multiple_choice",
        "options": ["a. Tildeo", "b. Paneo", "c. Zoom", "d. Grados"],
        "correct": "b. Paneo"
    },
    {
        "text": "¿Qué entidad utiliza las cámaras de videovigilancia para cumplir el objetivo del procedimiento?",
        "type": "multiple_choice",
        "options": ["a. Dirección Nacional de Operaciones", "b. Instituciones Articuladas.", "c. Servicio Integrado de Seguridad ECU 911.", "d. Gobiernos Autónomos Descentralizados."],
        "correct": "c. Servicio Integrado de Seguridad ECU 911."
    },
    {
        "text": "El Evaluador de Operaciones Zonal/Local (videovigilancia) debe monitorear el incidente o emergencia:",
        "type": "multiple_choice",
        "options": ["a. Solo hasta enviar la ficha electrónica", "b. Hasta que llegue la unidad de respuesta", "c. Hasta el cierre de la ficha electrónica"],
        "correct": "c. Hasta el cierre de la ficha electrónica"
    },
    {
        "text": "¿Cuál de las siguientes es una actividad del Evaluador de Operaciones (Videovigilancia) después de que las Instituciones Articuladas finalicen la atención en el lugar de la emergencia?",
        "type": "multiple_choice",
        "options": ["a. Iniciar un nuevo seguimiento de perfiles.", "b. Ejecutar el paneo automático o predeterminado de la cámara", "c. Elaborar una ficha multidespacho", "d. Realizar la consolidación de fichas"],
        "correct": "b. Ejecutar el paneo automático o predeterminado de la cámara"
    },
    {
        "text": "¿Si el Analista determina que no corresponde a un incidente o emergencia, se debe continuar con el monitoreo de cámaras?",
        "type": "true_false",
        "options": ["Verdadero", "Falso"],
        "correct": "Falso"
    },
    {
        "text": "En los eventos de concurrencia masiva, si se trata de Seguridad Ciudadana, ¿Qué categoría se debe usar en la ficha electrónica?",
        "type": "multiple_choice",
        "options": ["a. Seguridad Ciudadana", "b. Servicios", "c. Resguardo policial", "d. Tipo de captura T2"],
        "correct": "c. Resguardo policial"
    },
    {
        "text": "El Evaluador de Operaciones (Videovigilancia) debe seleccionar el tipo de captura \"FS\" para un incidente o emergencia detectada por videovigilancia.",
        "type": "true_false",
        "options": ["Verdadero", "Falso"],
        "correct": "Falso"
    },
    {
        "text": "¿Cuál es el objetivo del procedimiento de megafonía IP?",
        "type": "multiple_choice",
        "options": ["a. Instalar cámaras de seguridad", "b. Reparar equipos de audio", "c. Controlar el tráfico vehicular", "d. Estandarizar el despliegue y uso de la herramienta de megafonía IP"],
        "correct": "d. Estandarizar el despliegue y uso de la herramienta de megafonía IP"
    },
    {
        "text": "¿Quién verifica la información del incidente o emergencia reportada por el evaluador?",
        "type": "multiple_choice",
        "options": ["a. Analista de Operaciones Zonal/Local (Videovigilancia)", "b. Evaluador de Llamadas", "c. Evaluador de despacho"],
        "correct": "a. Analista de Operaciones Zonal/Local (Videovigilancia)"
    },
    {
        "text": "¿El Evaluador de Operaciones Zonal /Local (videovigilancia) debe verificar la operatividad de las cámaras asignadas al inicio de sus actividades?",
        "type": "true_false",
        "options": ["Verdadero", "Falso"],
        "correct": "Verdadero"
    },
    {
        "text": "¿Cuál de las siguientes acciones NO está permitida para el Evaluador de Operaciones durante el monitoreo?",
        "type": "multiple_choice",
        "options": ["a. Realizar paneo manual para revisar la zona.", "b. Utilizar dispositivos móviles dentro de la sala operativa durante el turno.", "c. Reportar novedades al Analista de Operaciones.", "d. Verificar el funcionamiento de las cámaras."],
        "correct": "b. Utilizar dispositivos móviles dentro de la sala operativa durante el turno."
    },
    {
        "text": "¿En qué se basa la configuración del paneo automático?",
        "type": "multiple_choice",
        "options": ["a. El número de operadores", "b. La zona de cobertura visual, la geografía del lugar y los puntos de interés", "c. La marca del equipo", "d. El color de la cámara"],
        "correct": "b. La zona de cobertura visual, la geografía del lugar y los puntos de interés"
    },
    {
        "text": "¿El monitoreo del incidente finaliza inmediatamente después de enviar la ficha electrónica?",
        "type": "true_false",
        "options": ["Verdadero", "Falso"],
        "correct": "Falso"
    },
    {
        "text": "¿Qué acciones contempla el Procedimiento de Videovigilancia, según el objetivo?",
        "type": "multiple_choice",
        "options": ["a. Dirección, Organización, Coordinación y Control de Personal.", "b. Recepción de llamadas, verificación de alertas y cierre de emergencias.", "c. Monitoreo, evaluación, análisis, detección y direccionamiento de alertas y emergencias.", "d. Únicamente el monitoreo y análisis."],
        "correct": "c. Monitoreo, evaluación, análisis, detección y direccionamiento de alertas y emergencias."
    },
    {
        "text": "El T2 - Tipo de captura reactiva se suscita de manera espontánea durante un monitoreo",
        "type": "true_false",
        "options": ["Verdadero", "Falso"],
        "correct": "Verdadero"
    }
]

html_template = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Módulo de Estudio - Operaciones de Videovigilancia ECU 911</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        :root {
            --primary: #2563eb;
            --primary-hover: #1d4ed8;
            --success: #10b981;
            --danger: #ef4444;
            --bg-color: #f8fafc;
            --card-bg: #ffffff;
            --text-main: #1e293b;
            --text-muted: #64748b;
            --border-color: #e2e8f0;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', sans-serif; }
        body { background-color: var(--bg-color); color: var(--text-main); line-height: 1.6; padding: 2rem; }
        .container { max-width: 800px; margin: 0 auto; }
        .header { text-align: center; margin-bottom: 2rem; }
        .header h1 { font-size: 2rem; font-weight: 700; color: #0f172a; margin-bottom: 0.5rem; }
        .header p { color: var(--text-muted); font-size: 1.1rem; }
        
        .question-card {
            background: var(--card-bg);
            border-radius: 12px;
            padding: 2rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
            display: none;
            animation: fadeIn 0.4s ease-out forwards;
        }
        .question-card.active { display: block; }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .q-number { font-size: 0.875rem; font-weight: 600; color: var(--primary); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 1rem; display: block; }
        .q-text { font-size: 1.25rem; font-weight: 600; margin-bottom: 1.5rem; color: #0f172a; }
        
        .options { display: flex; flex-direction: column; gap: 0.75rem; margin-bottom: 2rem; }
        .option-label {
            display: flex; align-items: center; padding: 1rem; border: 2px solid var(--border-color);
            border-radius: 8px; cursor: pointer; transition: all 0.2s; font-size: 1.05rem;
        }
        .option-label:hover { border-color: #cbd5e1; background-color: #f8fafc; }
        .option-input { margin-right: 1rem; transform: scale(1.2); cursor: pointer; }
        .option-label.selected { border-color: var(--primary); background-color: #eff6ff; }
        .option-label.correct { border-color: var(--success); background-color: #ecfdf5; color: #065f46; font-weight: 500; }
        .option-label.incorrect { border-color: var(--danger); background-color: #fef2f2; color: #991b1b; }
        
        .feedback { 
            padding: 1.25rem; border-radius: 8px; margin-bottom: 1.5rem; display: none;
            font-size: 1.05rem; 
        }
        .feedback.show { display: block; animation: fadeIn 0.3s; }
        .feedback.success { background-color: #ecfdf5; border-left: 4px solid var(--success); color: #065f46; }
        .feedback.error { background-color: #fef2f2; border-left: 4px solid var(--danger); color: #991b1b; }
        .feedback strong { display: block; margin-bottom: 0.25rem; }
        
        .actions { display: flex; justify-content: space-between; align-items: center; }
        .btn {
            padding: 0.75rem 1.5rem; font-size: 1rem; font-weight: 600; border-radius: 8px;
            border: none; cursor: pointer; transition: all 0.2s;
        }
        .btn-primary { background-color: var(--primary); color: white; }
        .btn-primary:hover { background-color: var(--primary-hover); }
        .btn-primary:disabled { background-color: #94a3b8; cursor: not-allowed; }
        
        .btn-secondary { background-color: #e2e8f0; color: #475569; }
        .btn-secondary:hover { background-color: #cbd5e1; }
        
        /* Summary UI */
        #summary { display: none; text-align: center; }
        .score-circle {
            width: 150px; height: 150px; border-radius: 50%; background: var(--primary);
            color: white; display: flex; flex-direction: column; justify-content: center;
            align-items: center; margin: 0 auto 2rem; font-size: 2.5rem; font-weight: 700;
            box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.3);
        }
        .score-circle span { font-size: 1rem; font-weight: 400; opacity: 0.9; }
        
        .failed-list { text-align: left; margin-top: 2rem; }
        .failed-item { background: #fff; padding: 1.5rem; border-radius: 8px; margin-bottom: 1rem; border-left: 4px solid var(--danger); box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
        .failed-item h4 { margin-bottom: 0.5rem; color: #0f172a; }
        .correct-answer-text { color: var(--success); font-weight: 600; margin-top: 0.5rem; }
        
        .progress-container { width: 100%; height: 8px; background: #e2e8f0; border-radius: 4px; margin-bottom: 2rem; overflow: hidden; }
        .progress-bar { height: 100%; background: var(--primary); width: 0%; transition: width 0.3s ease; }
    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <h1>Módulo de Estudio: Videovigilancia y MegaFonia</h1>
        <p>Responde las siguientes preguntas tal como aparecen en las evaluaciones oficiales. La IA evaluará tus respuestas automáticamente.</p>
    </div>
    
    <div class="progress-container">
        <div class="progress-bar" id="progressBar"></div>
    </div>

    <div id="quiz-container">
        <!-- Questions will be injected here -->
    </div>

    <div id="summary" class="question-card">
        <h2>¡Módulo Completado!</h2>
        <p style="margin-bottom: 2rem; color: var(--text-muted);">Aquí tienes un resumen de tu desempeño.</p>
        
        <div class="score-circle">
            <div id="score-text">0</div>
            <span>puntos</span>
        </div>
        
        <h3 style="margin-top: 2rem; margin-bottom: 1rem; color: #0f172a;" id="failed-title">Preguntas para repasar:</h3>
        <div class="failed-list" id="failed-list">
            <!-- Failed items injected here -->
        </div>
        
        <div style="margin-top: 2.5rem; display: flex; gap: 1rem; justify-content: center;">
            <button class="btn btn-secondary" onclick="exportMarkdown()">Exportar Resultados (MD)</button>
            <button class="btn btn-primary" onclick="location.reload()">Reiniciar Módulo</button>
        </div>
    </div>
</div>

<script>
    const questions = [JSON_QUESTIONS];
    
    let currentIdx = 0;
    let score = 0;
    let failedQuestions = [];
    
    const container = document.getElementById('quiz-container');
    const progressBar = document.getElementById('progressBar');
    
    function renderQuestions() {
        container.innerHTML = '';
        questions.forEach((q, index) => {
            const card = document.createElement('div');
            card.className = `question-card ${index === 0 ? 'active' : ''}`;
            card.id = `q-${index}`;
            
            let optionsHtml = '';
            q.options.forEach((opt, oIdx) => {
                optionsHtml += `
                    <label class="option-label" id="label-${index}-${oIdx}">
                        <input type="radio" name="q${index}" value="${opt.replace(/"/g, '&quot;')}" class="option-input" onchange="selectOption(${index})">
                        ${opt}
                    </label>
                `;
            });
            
            card.innerHTML = `
                <span class="q-number">Pregunta ${index + 1} de ${questions.length}</span>
                <div class="q-text">${q.text}</div>
                <div class="options">
                    ${optionsHtml}
                </div>
                <div class="feedback" id="feedback-${index}"></div>
                <div class="actions">
                    <button class="btn btn-primary" id="btn-verify-${index}" onclick="verify(${index})" disabled>Verificar Respuesta</button>
                    <button class="btn btn-secondary" id="btn-next-${index}" onclick="next(${index})" style="display:none;">${index === questions.length - 1 ? 'Ver Resultados' : 'Siguiente'}</button>
                </div>
            `;
            container.appendChild(card);
        });
        updateProgress();
    }
    
    window.selectOption = function(qIndex) {
        document.getElementById(`btn-verify-${qIndex}`).disabled = false;
        
        // Remove selected class from all
        const labels = document.querySelectorAll(`#q-${qIndex} .option-label`);
        labels.forEach(l => l.classList.remove('selected'));
        
        // Add selected class to checked
        const checked = document.querySelector(`input[name="q${qIndex}"]:checked`);
        if(checked) {
            checked.closest('.option-label').classList.add('selected');
        }
    }
    
    window.verify = function(qIndex) {
        const q = questions[qIndex];
        const selected = document.querySelector(`input[name="q${qIndex}"]:checked`);
        if(!selected) return;
        
        const answer = selected.value;
        const isCorrect = answer === q.correct;
        
        // Disable inputs
        const inputs = document.querySelectorAll(`input[name="q${qIndex}"]`);
        inputs.forEach(i => i.disabled = true);
        
        // Hide verify button, show next
        document.getElementById(`btn-verify-${qIndex}`).style.display = 'none';
        document.getElementById(`btn-next-${qIndex}`).style.display = 'inline-block';
        
        // Styling options
        const labels = document.querySelectorAll(`#q-${qIndex} .option-label`);
        labels.forEach(l => {
            const input = l.querySelector('input');
            if(input.value === q.correct) {
                l.classList.add('correct');
            } else if (input.checked && !isCorrect) {
                l.classList.add('incorrect');
            }
        });
        
        // Feedback
        const fb = document.getElementById(`feedback-${qIndex}`);
        fb.classList.add('show');
        
        if(isCorrect) {
            score++;
            fb.classList.add('success');
            fb.innerHTML = `<strong>¡Correcto!</strong> La respuesta es exactamente: "${q.correct}".`;
        } else {
            failedQuestions.push(q);
            fb.classList.add('error');
            fb.innerHTML = `<strong>Incorrecto.</strong><br>Seleccionaste: ${answer}<br>La respuesta correcta es: <b>${q.correct}</b>.`;
        }
    }
    
    window.next = function(qIndex) {
        document.getElementById(`q-${qIndex}`).classList.remove('active');
        if(qIndex + 1 < questions.length) {
            document.getElementById(`q-${qIndex + 1}`).classList.add('active');
            currentIdx++;
            updateProgress();
        } else {
            showSummary();
        }
    }
    
    function updateProgress() {
        const pct = (currentIdx / questions.length) * 100;
        progressBar.style.width = pct + '%';
    }
    
    function showSummary() {
        progressBar.style.width = '100%';
        container.style.display = 'none';
        document.getElementById('summary').style.display = 'block';
        
        document.getElementById('score-text').innerText = `${score} / ${questions.length}`;
        
        const flist = document.getElementById('failed-list');
        if(failedQuestions.length === 0) {
            document.getElementById('failed-title').innerText = "¡Excelente! No fallaste ninguna pregunta.";
        } else {
            document.getElementById('failed-title').innerText = `Preguntas para repasar (${failedQuestions.length}):`;
            failedQuestions.forEach(q => {
                flist.innerHTML += `
                    <div class="failed-item">
                        <h4>${q.text}</h4>
                        <div class="correct-answer-text">✅ Respuesta correcta: ${q.correct}</div>
                    </div>
                `;
            });
        }
    }
    
    window.exportMarkdown = function() {
        let md = "# Resultados de Estudio\\n\\n";
        md += `**Puntuación:** ${score} / ${questions.length}\\n\\n`;
        if(failedQuestions.length > 0) {
            md += "## Preguntas a Repasar\\n\\n";
            failedQuestions.forEach(q => {
                md += `**Pregunta:** ${q.text}\\n`;
                md += `**Correcta:** ${q.correct}\\n\\n`;
            });
        }
        
        const blob = new Blob([md], { type: 'text/markdown' });
        const a = document.createElement('a');
        a.href = URL.createObjectURL(blob);
        a.download = 'resultados_modulo.md';
        a.click();
    }
    
    // Init
    renderQuestions();

</script>
</body>
</html>
"""

html_out = html_template.replace("JSON_QUESTIONS", json.dumps(questions))

with open("d:/examen/modulo_estudio_interactivo.html", "w", encoding="utf-8") as f:
    f.write(html_out)

markdown_out = "# Módulo de Estudio - Evaluación de Videovigilancia y Megafonía\n\n"
markdown_out += "> **Instrucciones:** Responde las siguientes preguntas tal como aparecen en las imágenes originales. La IA ha extraído el contenido exacto. Despliega la pestaña 'Ver respuesta' para comprobar si acertaste y ver el feedback.\n\n"

for i, q in enumerate(questions):
    markdown_out += f"### Pregunta {i+1}\n"
    markdown_out += f"**{q['text']}**\n\n"
    
    for opt in q['options']:
        markdown_out += f"- [ ] {opt}\n"
        
    markdown_out += "\n<details>\n"
    markdown_out += "<summary>👉 <b>Ver respuesta y feedback</b></summary>\n\n"
    markdown_out += f"✅ **Respuesta Correcta:** {q['correct']}\n\n"
    markdown_out += f"> *Feedback:* El sistema registra esta opción como la acreditada para la evaluación. Se mantiene la estructura exacta de la imagen original.\n"
    markdown_out += "</details>\n\n---\n\n"

with open("d:/examen/modulo_estudio_interactivo.md", "w", encoding="utf-8") as f:
    f.write(markdown_out)

print("Generated modulo_estudio_interactivo.html and modulo_estudio_interactivo.md")
