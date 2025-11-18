import csv
import os
import unicodedata
from flask import jsonify

# ============================================================
# LOAD PROFILES
# ============================================================

PROFILES = []
PROFILES_PATH = os.path.join(os.path.dirname(__file__), "..", '..', 'data', 'profiles.csv')
print("DEBUG - Caminho do CSV:", PROFILES_PATH)

def load_profiles():
    global PROFILES
    if os.path.exists(PROFILES_PATH):
        try:
            with open(PROFILES_PATH, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                PROFILES = list(reader)
                print(f"✅ Perfis carregados: {len(PROFILES)}")
        except Exception as e:
            print("❌ Erro ao carregar profiles:", e)
    else:
        print(f"⚠️ Arquivo {PROFILES_PATH} não encontrado")

load_profiles()

# ============================================================
# FAQS
# ============================================================

FAQS = {
    "benefícios": "Os benefícios incluem: vale-refeição, plano de saúde, vale-transporte e gympass.",
    "horário": "O horário padrão é das 9h às 18h, com 1h de almoço. Home office 2x por semana.",
    "férias": "Você tem direito a 30 dias de férias após 12 meses.",
    "cultura": "Nossa cultura valoriza inovação, colaboração e diversidade.",
    "treinamento": "Oferecemos cursos, workshop e orçamento anual de R$1.000."
}

# ============================================================
# UTILITÁRIOS
# ============================================================

def normalize_text(text):
    """Remove acentos, converte para minúsculas e remove espaços extras"""
    text = text.strip().lower()
    text = ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')
    return text

# ============================================================
# CHAT
# ============================================================

def chat_logic(request, GEMINI_MODEL):
    if request.method == 'OPTIONS':
        return '', 204

    data = request.json or {}
    question = data.get('question', '').strip().lower()

    # FAQ direto
    for key, answer in FAQS.items():
        if key in question:
            return jsonify({'answer': answer, 'source': 'faq'})

    # Modelo Gemini
    if GEMINI_MODEL:
        try:
            prompt = f"Responda como assistente da empresa. Pergunta: {question}"
            response = GEMINI_MODEL.generate_content(prompt)
            return jsonify({'answer': response.text, 'source': 'gemini'})

        except Exception as e:
            print("❌ ERRO GEMINI:", e)
            return jsonify({'answer': "Erro ao acessar modelo.", 'source': 'error'})

    # Caso não tenha modelo
    return jsonify({'answer': "Gemini não configurado.", 'source': 'mock'})

# ============================================================
# RECOMMENDER DE MENTORES
# ============================================================

def recommend_logic(request):
    if request.method == 'OPTIONS':
        return '', 204

    try:
        data = request.json or {}
        print("DEBUG - Dados recebidos:", data)

        # Separar por vírgula ou espaço, remover vazios e normalizar
        user_skills = set()
        for s in data.get('skills', '').replace(',', ' ').split():
            s = normalize_text(s)
            if s: user_skills.add(s)

        user_interests = set()
        for i in data.get('interests', '').replace(',', ' ').split():
            i = normalize_text(i)
            if i: user_interests.add(i)

        print("DEBUG - Skills do usuário:", user_skills)
        print("DEBUG - Interesses do usuário:", user_interests)

        if not PROFILES:
            print("⚠️ PROFILES vazio")
            return jsonify({'error': 'Perfis não carregados'}), 500

        mentors = [p for p in PROFILES if p.get('disponivel_mentoria') == 'True']
        print(f"DEBUG - Mentores disponíveis: {len(mentors)}")

        recommendations = []

        for mentor in mentors:
            # Normalizar skills/interesses do mentor
            mentor_skills = set(normalize_text(s) for s in mentor.get('habilidades', '').replace(',', ' ').split())
            mentor_interests = set(normalize_text(s) for s in mentor.get('interesses', '').replace(',', ' ').split())

            common_skills = user_skills & mentor_skills
            common_interests = user_interests & mentor_interests

            score = len(common_skills) * 10 + len(common_interests) * 5

            if score > 0:
                recommendations.append({
                    'id': mentor.get('id'),
                    'nome': mentor.get('nome'),
                    'departamento': mentor.get('departamento'),
                    'cargo': mentor.get('cargo'),
                    'score': score,
                    'habilidades': mentor.get('habilidades'),
                    'interesses': mentor.get('interesses'),
                    'explicacao': f"Skills em comum: {', '.join(common_skills) if common_skills else 'Perfil complementar'}; "
                                  f"Interesses em comum: {', '.join(common_interests) if common_interests else 'Nenhum'}"
                })

        recommendations.sort(key=lambda x: x['score'], reverse=True)
        print("DEBUG - Recommendations:", recommendations)

        if not recommendations:
            return jsonify({'recommendations': [], 'message': 'Nenhum mentor encontrado. Tente outras habilidades ou interesses.'})

        return jsonify({'recommendations': recommendations[:3]})

    except Exception as e:
        print("❌ ERRO recommend_logic:", e)
        return jsonify({'error': 'Erro interno ao processar recomendação', 'details': str(e)}), 500


# ============================================================
# PROFILES ENDPOINT
# ============================================================

def get_profiles_logic():
    return jsonify({
        'profiles': PROFILES,
        'total': len(PROFILES)
    })
