import csv
import os
import numpy as np
from flask import jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ============================================================
# LOAD PROFILES
# ============================================================

PROFILES = []
PROFILES_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'profiles.csv')

def load_profiles():
    global PROFILES
    if os.path.exists(PROFILES_PATH):
        try:
            with open(PROFILES_PATH, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                PROFILES = list(reader)
                print(f"Perfis carregados: {len(PROFILES)}")
        except Exception as e:
            print("Erro ao carregar profiles:", e)

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
            print("ERRO GEMINI:", e)
            return jsonify({'answer': "Erro ao acessar modelo.", 'source': 'error'})

    # Caso não tenha modelo
    return jsonify({'answer': "Gemini não configurado.", 'source': 'mock'})


# ============================================================
# RECOMMENDER
# ============================================================

def recommend_logic(request):
    if request.method == 'OPTIONS':
        return '', 204

    data = request.json or {}
    user_skills = data.get('skills', '').lower()
    user_interests = data.get('interests', '').lower()

    if not PROFILES:
        return jsonify({'error': 'Perfis não carregados'}), 500

    user_text = f"{user_skills} {user_interests}"

    mentors = [p for p in PROFILES if p.get('disponivel_mentoria') == 'True']

    mentor_texts = [
        f"{m.get('habilidades', '')} {m.get('interesses', '')}".lower()
        for m in mentors
    ]

    vectorizer = TfidfVectorizer()
    all_texts = [user_text] + mentor_texts
    tfidf_matrix = vectorizer.fit_transform(all_texts)

    similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])[0]
    top_indices = np.argsort(similarities)[-3:][::-1]

    recommendations = []

    for idx in top_indices:
        mentor = mentors[idx]
        score = float(similarities[idx])

        user_sk = {s.strip() for s in user_skills.split(',')}
        mentor_sk = {s.strip() for s in mentor.get('habilidades', '').lower().split(',')}
        common = user_sk & mentor_sk

        recommendations.append({
            'id': mentor.get('id'),
            'nome': mentor.get('nome'),
            'departamento': mentor.get('departamento'),
            'cargo': mentor.get('cargo'),
            'score': int(score * 100),
            'habilidades': mentor.get('habilidades', ''),
            'interesses': mentor.get('interesses', ''),
            'explicacao': f"Skills em comum: {', '.join(common) if common else 'Perfil complementar'}"
        })

    return jsonify({'recommendations': recommendations})


# ============================================================
# PROFILES ENDPOINT
# ============================================================

def get_profiles_logic():
    return jsonify({
        'profiles': PROFILES,
        'total': len(PROFILES)
    })
