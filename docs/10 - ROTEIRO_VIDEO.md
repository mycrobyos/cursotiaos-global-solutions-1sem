# 🎥 Roteiro de Vídeo - HumanIza MVP
## Duração: 5-7 minutos

---

## 📋 PREPARAÇÃO ANTES DE GRAVAR

### Checklist Técnico:
- [ ] Backend rodando (`python3 app.py` na pasta backend)
- [ ] Frontend aberto no navegador (index.html)
- [ ] Testar chat com 1 pergunta antes
- [ ] Testar matching com exemplo antes
- [ ] Limpar histórico do chat (recarregar página)
- [ ] Fechar abas desnecessárias do navegador
- [ ] Aumentar zoom do navegador para 125-150% (melhor visualização)
- [ ] Ter VSCode aberto com os arquivos principais
- [ ] Ter terminal visível com backend rodando

---

## 🎬 ROTEIRO DETALHADO

### ABERTURA (30 segundos)

**[TELA: Você falando ou apresentação]**

> "Olá! Sou [seu nome] e vou apresentar o **HumanIza**, nossa solução para o desafio Global Solutions 2025 sobre o Futuro do Trabalho."

> "O HumanIza é uma plataforma inteligente que torna o onboarding mais humano, inclusivo e sustentável, combinando três eixos: chatbot com IA, recomendação de mentores e gamificação."

**[MOSTRAR: Tela inicial do HumanIza]**

---

### PARTE 1: O PROBLEMA (30 segundos)

**[TELA: Você falando ou slides simples]**

> "Estudos mostram que 70% dos novos funcionários se sentem perdidos na primeira semana. O onboarding tradicional é impessoal, baseado em PDFs e e-mails, e não promove conexões humanas."

> "Nossa solução ataca esse problema com tecnologia que conecta pessoas, não apenas automatiza processos."

---

### PARTE 2: DEMO DO CHAT - "IZA" (1m 30s)

**[TELA: Navegador com Symphony aberto]**

> "Vou demonstrar as três funcionalidades principais. Primeira: o chat com a Iza, nossa assistente de IA."

**[FAZER]:**
1. Clicar na aba "Chat com Iza"
2. Digitar: **"quais são os benefícios?"**
3. Enviar e mostrar resposta da IA
4. Digitar: **"qual o horário de trabalho?"**
5. Enviar e mostrar resposta

**[NARRAR enquanto digita]:**
> "A Iza usa a API Gemini do Google para responder perguntas sobre a empresa. Ela tem acesso a uma base de conhecimento com FAQs, políticas e cultura organizacional."

> "Veja como a resposta é natural e contextualizada. Isso reduz a carga do RH e dá autonomia ao colaborador."

**[MOSTRAR CÓDIGO - 20 segundos]:**
- Abrir VSCode em `backend/app.py`
- Mostrar função `@app.route('/chat')`

> "No código, integramos a API Gemini com uma base de FAQs. Se a pergunta estiver nos FAQs, responde direto. Caso contrário, usa a IA generativa."

---

### PARTE 3: DEMO DO MATCHING DE MENTORES (2 minutos)

**[TELA: Navegador]**

> "Segunda funcionalidade: recomendação inteligente de mentores usando Machine Learning."

**[FAZER]:**
1. Clicar na aba "Encontre seu Mentor"
2. No campo Habilidades, digitar: **"Python, Liderança, Comunicação"**
3. No campo Interesses, digitar: **"Inovação, Tecnologia"**
4. Clicar em "Buscar Mentores"
5. Aguardar aparecer os 3 resultados

**[NARRAR enquanto aguarda]:**
> "O sistema está analisando 200 perfis de funcionários usando TF-IDF, uma técnica de Machine Learning para vetorização de texto."

**[QUANDO APARECER OS RESULTADOS]:**
> "Veja: temos 3 recomendações com porcentagem de match. Cada sugestão mostra o departamento, cargo, habilidades em comum e uma explicação do porquê do match."

**[APONTAR PARA TELA]:**
> "Aqui diz '3 skills em comum: Liderança, Python, Inovação'. Isso é transparência algorítmica - o colaborador entende porque aquela pessoa foi sugerida."

**[MOSTRAR CÓDIGO - 30 segundos]:**
- Abrir VSCode em `backend/app.py`
- Mostrar função `@app.route('/recommend')`
- Apontar para linha `TfidfVectorizer` e `cosine_similarity`

> "Tecnicamente, usamos TF-IDF do scikit-learn para vetorizar as habilidades e calcular similaridade de cosseno. É content-based filtering, um algoritmo clássico de recomendação."

---

### PARTE 4: DEMO DA GAMIFICAÇÃO (1 minuto)

**[TELA: Navegador]**

> "Terceira funcionalidade: gamificação do onboarding com trilha de missões."

**[FAZER]:**
1. Clicar na aba "Missões"
2. Ler uma missão em voz alta: **"Conheça seu time - agendar café virtual - 10 pontos"**
3. Marcar 2-3 missões
4. Mostrar barra de progresso aumentando
5. Ler a mensagem de badge que aparece

**[NARRAR]:**
> "Transformamos tarefas burocráticas em um jogo. Cada missão concluída dá pontos e badges."

> "Veja: marquei 3 missões e já ganhei o badge Bronze. Isso aumenta o engajamento e deixa claro o que precisa ser feito na primeira semana."

---

### PARTE 5: DADOS E ANÁLISE (1 minuto)

**[TELA: VSCode ou terminal]**

> "Por trás disso tudo, temos um dataset sintético de 200 perfis de funcionários."

**[MOSTRAR]:**
1. Abrir `data/profiles.csv` no VSCode
2. Rolar algumas linhas mostrando: nome, departamento, habilidades, interesses

**[NARRAR]:**
> "Geramos esses dados com a biblioteca Faker do Python. Temos 4 departamentos, 3 níveis de senioridade, e 12 habilidades diferentes distribuídas aleatoriamente."

**[OPCIONAL - se tiver feito a análise R]:**
- Abrir o arquivo HTML gerado pelo RMarkdown
- Mostrar 1-2 gráficos (distribuição por departamento, fairness)

> "Fizemos uma análise exploratória em R para garantir que os dados são balanceados e não têm viés. O Disparate Impact ficou em 0.95, dentro da meta ética de 0.8 a 1.25."

---

### PARTE 6: INTEGRAÇÃO DAS DISCIPLINAS (1 minuto)

**[TELA: Você falando ou mostrar arquivos]**

> "Este projeto integra 7 disciplinas do curso:"

**[LISTAR enquanto mostra arquivos/código]:**

1. **Python:** Backend Flask, geração de dados
   - Mostrar `app.py` e `generate_profiles.py`

2. **Machine Learning:** Sistema de recomendação com TF-IDF
   - Apontar função `recommend()`

3. **Inteligência Artificial:** Integração com Gemini API
   - Mostrar chamada `model.generate_content()`

4. **Banco de Dados:** Armazenamento em CSV com modelagem relacional
   - Mostrar `profiles.csv` aberto

5. **Cybersecurity:** Dataset sintético, variáveis de ambiente para API keys
   - Mostrar `.env.example` e mencionar boas práticas

6. **Linguagem R:** Análise exploratória e fairness
   - Se tiver: mostrar arquivo RMarkdown ou gráfico

7. **Formação Social:** Foco em inclusão e ética algorítmica
   - Mencionar explicabilidade das recomendações e fairness

---

### PARTE 7: IMPACTO E RESULTADOS (45 segundos)

**[TELA: Você falando ou dashboard simulado]**

> "Com o HumanIza, estimamos:"
> - Aumento de 30% na conclusão de tarefas de onboarding na primeira semana
> - Redução de 50% nas dúvidas enviadas ao RH
> - Mais de 80% dos novos colaboradores recebem pelo menos 2 sugestões de mentores
> - Promoção de conexões interdepartamentais, quebrando silos

> "Isso torna o trabalho mais humano (conexões reais), mais inclusivo (algoritmo ético) e mais sustentável (retenção de talentos)."

---

### FECHAMENTO (30 segundos)

**[TELA: Você falando]**

> "O HumanIza é uma prova de conceito funcional que mostra como a tecnologia pode humanizar o trabalho, não apenas automatizá-lo."

> "Todo o código está no GitHub [mostrar README], com instruções de instalação e documentação completa."

> "Obrigado! Estou à disposição para dúvidas."

**[TELA FINAL: Mostrar aplicação rodando ou logo do HumanIza]**

---

## 🎯 DICAS DE GRAVAÇÃO

### Técnicas:
- **Fale devagar e claro** - pessoas vão assistir em velocidade normal
- **Pause 2 segundos** antes de cada funcionalidade nova
- **Aponte com o cursor** para elementos importantes na tela
- **Ensaie 1-2 vezes** antes da gravação final
- **Grave em partes** se necessário e edite depois

### Evite:
- ❌ Dizer "hum", "tipo", "né" demais
- ❌ Ficar muito tempo em silêncio
- ❌ Passar rápido demais pelos gráficos/código
- ❌ Texto pequeno na tela (aumente zoom)

### Ferramentas de Gravação:
- **macOS:** QuickTime Player (Arquivo → Nova Gravação de Tela)
- **Gratuito:** OBS Studio
- **Pago:** Loom, Camtasia

### Edição (opcional):
- Cortar partes com erro
- Adicionar título inicial com nome do projeto
- Adicionar música de fundo baixa (opcional)
- Exportar em 1080p

---

## 📤 CHECKLIST PÓS-GRAVAÇÃO

- [ ] Vídeo tem no máximo 7 minutos
- [ ] Áudio está claro (sem ruído de fundo)
- [ ] Todas as 3 funcionalidades foram demonstradas
- [ ] Mostrou pelo menos 1 trecho de código
- [ ] Mencionou integração das disciplinas
- [ ] Upload no YouTube como "não listado"
- [ ] Link do vídeo adicionado no PDF (SEM mascarar)

---

## 🎬 EXEMPLO DE FALAS PRONTAS

### Para o Chat:
> "Vou fazer uma pergunta simples: 'quais são os benefícios?'. A Iza acessa a base de conhecimento e retorna uma resposta natural, citando vale-refeição, plano de saúde e gympass. Simples e eficaz."

### Para o Matching:
> "Agora vou buscar mentores com minhas habilidades: Python, Liderança e Comunicação. Interesses: Inovação e Tecnologia. Clico em buscar... e em 2 segundos temos 3 sugestões com 85%, 72% e 68% de match. Cada uma explica o porquê: 'skills em comum: Liderança, Python, Inovação'."

### Para as Missões:
> "Aqui temos 4 missões de onboarding. Vou marcar 'Conheça seu time' e 'Desbloqueie seu setup'. Veja a barra de progresso subindo... e ganhamos o badge Bronze! Falta pouco para o Prata."

### Para o Código:
> "No código, a função de recomendação usa TfidfVectorizer do scikit-learn. Ela transforma texto em vetores numéricos e calcula similaridade de cosseno. É uma técnica eficiente e escalável para sistemas de recomendação."

---

**BOA GRAVAÇÃO! 🎥🎵**
