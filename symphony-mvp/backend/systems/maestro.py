import numpy as np
import google.generativeai as genai
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


DOCUMENTOS_FAQ = [
    { "pergunta": "O que é o Symphony?", "resposta": "O Symphony é o seu parceiro digital de carreira..." },
    { "pergunta": "Quem é o Maestro?", "resposta": "Eu sou o Maestro..." },
    { "pergunta": "Como funcionam as missões de onboarding?", "resposta": "Suas missões funcionam assim..." },
    { "pergunta": "Os pontos e badges valem alguma coisa?", "resposta": "Sim, badges representam progresso." },
    { "pergunta": "Como encontro um mentor?", "resposta": "Use o conector de mentoria." },
    { "pergunta": "Como o Symphony escolhe meus mentores?", "resposta": "Usa IA ética para matches." },
    { "pergunta": "Onde estão documentos importantes?", "resposta": "Na intranet." },
    { "pergunta": "Como peço meu notebook?", "resposta": "Pelo HelpDesk Central." },
    { "pergunta": "O bot não sabe a resposta. E agora?", "resposta": "Ele encaminha para RH." },
    { "pergunta": "Como conhecer meu time?", "resposta": "Agende um café virtual." }
]


class BuscadorFAQ:
    def __init__(self, documentos, limiar=0.3):
        self.docs = documentos
        self.limiar = limiar
        self.perguntas = [d["pergunta"] for d in documentos]
        self.respostas = [d["resposta"] for d in documentos]
        self.vectorizer = TfidfVectorizer()
        self.matrix = self.vectorizer.fit_transform(self.perguntas)

    def buscar_contexto(self, query):
        vec = self.vectorizer.transform([query])
        sims = cosine_similarity(vec, self.matrix)
        idx = np.argmax(sims)

        if sims[0, idx] > self.limiar:
            return self.respostas[idx]

        return None


class GeradorRespostas:
    def __init__(self):
        try:
            self.model = genai.GenerativeModel("models/gemini-2.0-flash")
        except:
            self.model = None

    def gerar_resposta_rag(self, pergunta, contexto):
        if not self.model:
            return "Erro: modelo não inicializado."

        ctx = contexto if contexto else "Nenhum contexto disponível."
        prompt = f"Pergunta: {pergunta}\nContexto: {ctx}\nResponda baseado no contexto."

        try:
            resp = self.model.generate_content(prompt)
            return resp.text
        except:
            return "Erro ao gerar resposta."


class MaestroBot:
    def __init__(self):
        self.buscador = BuscadorFAQ(DOCUMENTOS_FAQ)
        self.gerador = GeradorRespostas()

    def responder(self, pergunta):
        ctx = self.buscador.buscar_contexto(pergunta)
        return self.gerador.gerar_resposta_rag(pergunta, ctx)


MAESTRO = MaestroBot()
