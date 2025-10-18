# backend/ai/portfolio_agent.py
import os
import json
import random 
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI 

load_dotenv()

THEME_DATA = [
    {
        "Name": "Star Wars (Jedi/Sith Galactic Republic)",
        "Vibe": "Epic space opera, Light vs. Dark, futuristic technology, moral struggle.",
        "Icon": "🌌⚔️",
        "Colors": "Yellow, Red, Blue, Deep Space Black, Silver",
        "Vocab": "Missions, Databanks, Holocron, Force-sensitive, Commander, Protocol Droid, Lightsaber Skills"
    },
    {
        "Name": "World of Warcraft (WoW) - Horde vs Alliance",
        "Vibe": "High fantasy MMORPG, massive battles, epic quests, tribal conflict.",
        "Icon": "🛡️🔥",
        "Colors": "Deep Red, Gold, Royal Blue, Forest Green, Bronze",
        "Vocab": "Quest Log, Talent Tree, Artifacts, Raid Leader, Skill Mastery, Gold Earned, Experience Points (XP)"
    },
    {
        "Name": "Spider-Man (Web-Slinger Vigilantism)",
        "Vibe": "Street-level superhero, friendly neighborhood, science background, responsibility.",
        "Icon": "🕷️🕸️",
        "Colors": "Bright Red, Deep Blue, Web White, NYC Gray",
        "Vocab": "Web Fluid Formulas, Daily Bugle Headlines, Responsibility, Power Set, Villains Defeated, Spidey-Sense"
    },
    {
        "Name": "Blink-182 (Pop-Punk/Millennial Rebellion)",
        "Vibe": "High-energy pop-punk, anti-establishment, youthful angst, catchy hooks.",
        "Icon": "🎸🖕",
        "Colors": "Neon Pink, Black, Sky Blue, Skateboard White",
        "Vocab": "Tour Dates, Setlist, Album Drops, Punk Rock Ethos, World Tour, Backstage Pass, Fan Base"
    },
{
        "Name": "The Matrix (Cyberpunk Dystopia/Red Pill)",
        "Vibe": "Simulated reality, fight for freedom, deep philosophy, futuristic action.",
        "Icon": "💊💻",
        "Colors": "Matrix Green (Binary Code), Black, Dark Gray, Apocalypse Red",
        "Vocab": "Red Pill/Blue Pill, The One, Binary Code, The Oracle, Agents, Recharges, Awakening"
    },
    {
        "Name": "Death Note (Supernatural Crime Thriller)",
        "Vibe": "Moral dilemma, justice vs. crime, mental chess game between geniuses, absolute power.",
        "Icon": "🍎📓",
        "Colors": "Black, Blood Red, Chalk White, Dark Gray, Cream (Old Paper)",
        "Vocab": "Shinigami, Kira, L, Name Written, Shinigami Eyes, Death Note, Rules"
    },
    {
        "Name": "Metallica (Legendary Thrash Metal)",
        "Vibe": "Heavy metal, speed, dark and social themes, iconic riffs.",
        "Icon": "⚡️🤘",
        "Colors": "Classic Black, Fire Red, Chrome Silver, Dirty White",
        "Vocab": "Master of Puppets, Album Drop, World Tour, Final Setlist, Powerful Riffs, Sold-Out Concert, Mosh Pit"
    },
    {
        "Name": "Pantera (Aggressive Groove Metal)",
        "Vibe": "Pure aggression, Southern attitude, heavy groove metal, boundless intensity.",
        "Icon": "🔥🎸",
        "Colors": "Black, Off-White, Metallic Blue, Camouflage, Dirty Gold",
        "Vocab": "Cowboys from Hell, Power Groove, Dimebag Darrell, Studio Recording, Smash It, Metal Ritual"
    },
    {
        "Name": "Transformers (Giant Robot War)",
        "Vibe": "Science fiction, alien robots, battle between good and evil, transforming vehicles.",
        "Icon": "🤖🚛",
        "Colors": "Fire Red (Optimus), Electric Blue, Bright Yellow (Bumblebee), Metallic Gray, Decepticon Purple",
        "Vocab": "Autobots/Decepticons, Transformation, Energon, Cybertron Mission, Vehicle Mode, Matrix of Leadership"
    },
    {
        "Name": "Iron Man (Technology and Eccentricity)",
        "Vibe": "Tech superhero, artificial intelligence, high-tech armor, millionaire playboy.",
        "Icon": "🚀💰",
        "Colors": "Sports Car Red, Gold, Reactor Blue, Industrial White",
        "Vocab": "Mark Armor, JARVIS/FRIDAY, Arc Reactor, Stark Industries, Flight Tests, Rescue Mission, Genius Scientist"
    },
    {
        "Name": "Vikings (Norse Invasion Epic)",
        "Vibe": "Norse myths, brutal exploration, honor in battle, early medieval era.",
        "Icon": "🛶🪓",
        "Colors": "Leather Brown, Deep Navy Blue, Snow White, Blood Red, Steel Gray",
        "Vocab": "Ragnarok, Battle Axe, War Shield, Settlement, Raid, Valhalla, Jarl, Saga"
    }

]

def generate_portfolio_html(theme_data: dict) -> str:
    """
    Generates HTML portfolio, saves it to the local directory, and returns the HTML content.
    """
    # Load profile
    BASE_DIR = os.path.dirname(__file__) # Esto resuelve la ruta local sin usar settings
    profile_path = os.path.join(BASE_DIR, "profile.json")

    with open(profile_path, "r", encoding="utf-8") as f:
        profile = json.load(f)
        
    # Configure model
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.95) 

    # 🚀 PROMPT TEMPLATE MEJORADO: RECIBE METADATA Y LA USA 🚀

    prompt = PromptTemplate.from_template("""
    You are a **Digital Storyteller** and expert frontend designer. Your mission is to generate a CV that is an **exciting digital adventure** based entirely on the provided theme metadata.

    Generate a **COMPLETE, EXTENSIVE HTML document** (doctype, head, body) showcasing the following professional profile:
    {profile}.

    **CORE OBJECTIVE:** The CV must be **EXTREMELY DETAILED**, **informally brilliant**, and immediately capture the reader's attention! **ABSOLUTELY ENSURE YOU INCLUDE ALL SECTIONS AND EVERY SINGLE PIECE OF EXPERIENCE DATA FROM THE PROFILE**.

    **THEME METADATA (CRITICAL!):**
    Use the following thematic data to guide your design and narrative:
    {theme_metadata}

    **KEY CREATIVE REQUIREMENTS (Maximum Freedom):**

    1.  **Theme and Tone:** The theme is **{theme_name}**. The **Vibe** is {theme_vibe}.
    2.  **Structural Dynamicism:** **EACH TIME THIS IS RENDERED**, the CV must have a **radically different section structure**. Use unconventional, inventive titles using the provided **Vocab** (e.g., replace 'Experience' with 'Quest Log' or 'Tour Dates').
    3.  **TailwindCSS Design:** Use TailwindCSS from CDN. Base the color palette on the provided **Colors** ({theme_colors}) for a **visually aggressive, memorable, and non-traditional** design. **MANDATORY DESIGN RULES:**
        * **AVOID WHITE BACKGROUNDS** (`bg-white` or similar light shades). The overall design must favor **DARK, VIBRANT, or DEEP colors** as backgrounds to enhance the thematic mood.
        * Ensure **MAXIMUM COLOR CONTRAST** between text and background for high readability (e.g., use light text on dark backgrounds, or dark text on light, non-white colors).
    4.  **Impact Storytelling:** Frame **ALL** experience and project details as thematic narratives (e.g., 'Mission Reports' or 'Artifact Forging'). **BE EXTENSIVE IN YOUR NARRATIVE**. Detail the **REAL IMPACT using METRICS** for every single job and project listed in the profile. **DO NOT OMIT ANY DATA POINT**.

    **FORMATTING INSTRUCTIONS:**
    -   Include only the final HTML code. **DO NOT** include any explanations or comments.
    -   Ensure the HTML is valid and directly renderable.
    """)

    final_prompt = prompt.format(
        profile=json.dumps(profile), 
        theme_metadata=json.dumps(theme_data),
        theme_name=theme_data['Name'],
        theme_vibe=theme_data['Vibe'],
        theme_icon=theme_data['Icon'],
        theme_colors=theme_data['Colors'],

    )
    response = llm.invoke(final_prompt)
    html_content = response.content

        # --- NUEVA LÓGICA DE GUARDADO ---
    
    # 1. Crear el nombre del archivo basado en el nombre del tema
    file_slug = 1
    filename = f"cv{file_slug}.html"
    file_path = os.path.join(BASE_DIR, filename)

    # 2. Guardar el contenido HTML en el mismo directorio
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_content)
    except Exception as e:
        print(e)

        # Considera cómo quieres manejar el error si la escritura falla

    # 3. Devuelve el contenido HTML (comportamiento original)
    return html_content

