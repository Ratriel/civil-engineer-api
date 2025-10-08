# backend/ai/agent.py
import os
from openai import OpenAI
from dotenv import load_dotenv
from ai.data_store import load_data


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def civil_engineering_agent(question: str):
    # Carga los datos sísmicos
    data = load_data()

    # Prepara el contexto textual (resumen simple por ahora)
    context = (
        "Estos son los registros sísmicos y geológicos recientes:\n"
        f"- Automáticos: {len(data.get('recent_automatic', []))} registros\n"
        f"- Sentidos: {len(data.get('recent_felt', []))} registros\n"
        f"- Históricos: {len(data.get('historical', []))} registros\n"
    )

    # Construye el prompt
    prompt = f"""
Eres un ingeniero civil experto en sismología y construcción antisísmica.

Tienes acceso a datos de sismos en Costa Rica y Estados Unidos.
Usa la siguiente información para contextualizar tu respuesta:

{context}

Pregunta: {question}

Responde con un enfoque técnico pero claro.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
