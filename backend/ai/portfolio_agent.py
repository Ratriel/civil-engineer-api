# backend/ai/portfolio_agent.py
import os
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

load_dotenv()

def generate_portfolio_html(style: str = "dark") -> str:
    """
    Genera HTML con TailwindCSS basado en el perfil de Ariel.
    El parámetro 'style' puede ser: 'dark', 'light', 'hacker', etc.
    Devuelve el HTML como string.
    """
    # Cargar perfil
    profile_path = os.path.join(os.path.dirname(__file__), "profile.json")
    with open(profile_path, "r", encoding="utf-8") as f:
        profile = json.load(f)

    # Configurar modelo
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

    # Prompt de generación
    prompt = PromptTemplate.from_template("""
Eres un experto diseñador frontend con experiencia en TailwindCSS.

Genera un documento HTML completo (doctype, head, body) que muestre el siguiente perfil profesional:
{profile}

Requisitos:
- Usa TailwindCSS desde CDN.
- Tema visual: {style} (oscuro, moderno, tipo hacker).
- Secciones: "About Me", "Skills", "Projects" y "Contact".
- Debe tener animaciones suaves entre secciones (por ejemplo, fade-in, slide, hover effects).
- Incluye solo el código HTML final, sin explicaciones ni comentarios.
- Debe ser válido y renderizable directamente en un navegador.
""")

    # Ejecutar modelo
    final_prompt = prompt.format(profile=json.dumps(profile), style=style)
    response = llm.invoke(final_prompt)

    return response.content
