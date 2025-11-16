# 🎵 Symphony MVP - Guia de Execução Rápida

## 🚀 Setup em 5 Minutos

### 1. Gerar Dataset Sintético

```bash
cd data
pip install faker
python generate_profiles.py
```

Isso criará `profiles.csv` com 200 perfis.

### 2. Configurar Backend

```bash
cd ../backend
pip install -r requirements.txt
```

**Configurar API Gemini (opcional mas recomendado):**
1. Acesse: https://makersuite.google.com/app/apikey
2. Crie uma API key gratuita
3. Copie `.env.example` para `.env`:
   ```bash
   cp .env.example .env
   ```
4. Edite `.env` e cole sua chave:
   ```
   GEMINI_API_KEY=SUA_CHAVE_AQUI
   ```

**Iniciar servidor:**
```bash
python app.py
```

O backend estará rodando em `http://localhost:5000`

### 3. Abrir Frontend

Em outra janela do terminal:

```bash
cd ../frontend
# Abrir com servidor HTTP simples
python -m http.server 8000
```

Ou simplesmente abra `index.html` direto no navegador.

Acesse: `http://localhost:8000`

---

## 📸 Como Demonstrar

### 1. Chat com o Maestro
- Pergunte: "quais são os benefícios?"
- Pergunte: "qual o horário de trabalho?"
- Veja respostas inteligentes (se configurou Gemini) ou FAQs

### 2. Encontrar Mentor
- Preencha: "Python, Liderança, Comunicação"
- Interesses: "Inovação, Tecnologia"
- Clique "Buscar Mentores"
- Veja top 3 recomendações com % de match

### 3. Missões Gamificadas
- Marque as 4 missões
- Veja progresso e badges

---

## 🎥 Para o Vídeo

1. Mostre a tela inicial
2. Demo do chat (2-3 perguntas)
3. Demo do matching (preencher e ver resultados)
4. Demo das missões (marcar e ver progresso)
5. Mostre o código do TF-IDF no backend
6. Mostre o CSV de perfis
7. Se tiver R: mostre os gráficos

---

## 🐛 Troubleshooting

**Backend não inicia:**
- Certifique-se de instalar: `pip install -r requirements.txt`
- Verifique se profiles.csv existe em `../data/`

**Chat não responde:**
- Se não configurou Gemini: use as perguntas dos FAQs (benefícios, horário, férias, cultura, treinamento)
- Verifique console do navegador (F12)

**Matching não funciona:**
- Certifique-se de que o backend está rodando
- Abra http://localhost:5000/health para verificar

**CORS error:**
- Certifique-se de que flask-cors está instalado
- Ou abra o HTML direto (sem servidor)

---

## 📊 Estrutura do Projeto

```
symphony-mvp/
├── data/
│   ├── generate_profiles.py  ← Gera 200 perfis
│   └── profiles.csv          ← Dataset gerado
├── backend/
│   ├── app.py               ← Flask API
│   ├── requirements.txt     ← Dependências Python
│   └── .env                 ← API keys (não commitar!)
└── frontend/
    ├── index.html           ← Interface principal
    ├── style.css            ← Estilos
    └── app.js               ← Lógica do frontend
```

---

## 🎯 Próximos Passos (se tiver tempo)

1. **Análise R:** Criar `r_analysis/eda.Rmd` com gráficos
2. **Deploy:** Subir backend no Render (gratuito)
3. **Dashboard RH:** Adicionar tab com estatísticas
4. **Melhorar matching:** Adicionar peso por departamento

---

## ✅ Checklist para Entrega

- [ ] Dataset gerado (200 perfis)
- [ ] Backend rodando localmente
- [ ] Frontend funcionando (chat + matching + missões)
- [ ] Screenshots de cada funcionalidade
- [ ] Vídeo de 5 min demonstrando
- [ ] PDF com código comentado

---

## 🔑 API Endpoints

- `POST /chat` - Chatbot (body: `{question: "..."}`)
- `POST /recommend` - Matching (body: `{skills: "...", interests: "..."}`)
- `GET /profiles` - Ver todos os perfis
- `GET /health` - Status do servidor

---

**Dúvidas?** Teste cada parte separadamente e verifique os logs no terminal!
