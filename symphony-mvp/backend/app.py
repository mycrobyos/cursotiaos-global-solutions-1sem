from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Importar sistemas
from systems.chat_recommend import (
    FAQS,
    PROFILES,
    chat_logic,
    recommend_logic,
    get_profiles_logic
)
from systems.maestro import MAESTRO

# ============================================================
# CONFIG
# ============================================================

load_dotenv()
app = Flask(__name__)

CORS(
    app,
    resources={
        r"/*": {
            "origins": "*",
            "methods": ["GET", "POST", "OPTIONS"],
            "allow_headers": ["Content-Type"]
        }
    }
)

@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
    return response

# ============================================================
# GEMINI CONFIG
# ============================================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def load_gemini_model():
    if not GEMINI_API_KEY:
        print("⚠️ GEMINI_API_KEY não encontrada.")
        return None

    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model_name = "models/gemini-2.0-flash"
        model = genai.GenerativeModel(model_name)
        print(f"✅ Gemini inicializado com sucesso: {model_name}")
        return model
    except Exception as e:
        print("❌ Erro ao inicializar Gemini:", e)
        return None

GEMINI_MODEL = load_gemini_model()

# ============================================================
# ENDPOINTS
# ============================================================

@app.route("/chat", methods=["POST", "OPTIONS"])
def chat():
    return chat_logic(request, GEMINI_MODEL)

@app.route("/recommend", methods=["POST", "OPTIONS"])
def recommend():
    return recommend_logic(request)

@app.route("/profiles", methods=["GET"])
def profiles():
    return get_profiles_logic()

@app.route("/maestro", methods=["POST"])
def maestro_endpoint():
    data = request.json or {}
    pergunta = data.get("question", "")
    resposta = MAESTRO.responder(pergunta)
    return jsonify({"answer": resposta, "source": "maestro-rag"})

@app.route("/missions", methods=["POST", "OPTIONS"])
def missions():
    if request.method == "OPTIONS":
        return '', 204

    data = request.json or {}
    mission_key = data.get("mission")
    completed = data.get("completed", False)
    
    # Aqui você pode salvar em DB futuramente
    print(f"Missão: {mission_key}, completada: {completed}")
    return jsonify({"status": "ok"})

@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "profiles": len(PROFILES),
        "gemini_configured": GEMINI_MODEL is not None,
        "environment": os.getenv("FLASK_ENV", "production")
    })

# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    print("\n🔥 Backend HumanIza + MaestroBot iniciado!\n")
    print("📍 Endpoints disponíveis:")
    print("   - POST /chat")
    print("   - POST /recommend")
    print("   - GET /profiles")
    print("   - POST /maestro")
    print("   - POST /missions")
    print("   - GET /health\n")
    
    app.run(debug=True, port=5001, host="0.0.0.0")
