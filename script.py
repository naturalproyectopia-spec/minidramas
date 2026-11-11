import os
import json
from google import genai

def generar_guion_minidrama():
    # Inicializa el cliente de Gemini usando el secret de GitHub
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    
    premisa = os.environ.get("PREMISA_DRAMA", "Un café que te permite viajar 5 segundos al pasado.")
    
    prompt = f"""
    Eres un director experto en contenido viral vertical (TikTok/Reels). 
    Crea un minidrama exacto de 20 segundos basado en esta premisa: "{premisa}".
    
    Devuelve la respuesta estrictamente en un formato JSON válido con esta estructura:
    {{
      "titulo": "Título atractivo",
      "hook": "Texto visual o acción de los segundos 0 a 3",
      "desarrollo": "Acción principal y giro dramático de los segundos 3 a 15",
      "climax_final": "Cierre o cliffhanger de los segundos 15 a 20",
      "prompt_visual_ia": "Un prompt detallado en inglés para generar el estilo cinematográfico vertical (9:16) sin diálogos hablados, atmósfera de tensión."
    }}
    """
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    
    guion_texto = response.text
    print("--- GUION GENERADO POR GEMINI ---")
    print(guion_texto)
    
    with open("guion.json", "w", encoding="utf-8") as f:
        f.write(guion_texto)

if __name__ == "__main__":
    generar_guion_minidrama()
