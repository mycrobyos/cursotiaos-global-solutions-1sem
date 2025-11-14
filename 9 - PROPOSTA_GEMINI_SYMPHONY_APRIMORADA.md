# Proposta Gemini - Global Solutions 2025.2 (VERSÃO SIMPLIFICADA)
## Symphony: O Assistente de Integração e Carreira

**Escopo:** MVP em 5 dias | 5 pessoas  
**Foco:** Entrega funcional, não competição

---

## 💡 A Proposta: "Symphony" – O Assistente de Integração e Carreira

### Conceito Central
Uma plataforma inteligente que combina **três eixos temáticos**:
- **Bots como parceiros** (Eixo 3)
- **Recrutamento e inclusão ética** (Eixo 5) 
- **Soluções gamificadas** (Eixo 6)

O **"Symphony"** é projetado para tornar o **onboarding** e o **desenvolvimento contínuo** de funcionários mais humano e inclusivo. Ele atua como um **"parceiro de carreira" digital** desde o primeiro dia.

---

## 🎯 Como o "Symphony" Responde ao Desafio

A plataforma ataca os **três pilares** da pergunta central:

### 🤝 Mais Humano
- Reduz a **ansiedade e solidão** dos novos funcionários
- Em vez de um portal estático, um bot amigável (o **"Maestro"**) guia o usuário
- A IA foca em **conectar pessoas** (mentoria), automatizando a burocracia
- Libera o RH para **interações humanas de maior valor**

### 🌍 Mais Inclusivo
- Facilita a integração de pessoas com diferentes **backgrounds, estilos de aprendizado e necessidades** (ex: neurodiversidade)
- Módulo de mentoria usa **algoritmo ético** para quebrar "bolhas"
- Sugere conexões que normalmente não aconteceriam, **promovendo equidade**
- Interface acessível (WCAG 2.1 AA): leitores de tela, contraste alto, navegação por teclado

### 🌱 Mais Sustentável
- **Sustentabilidade humana e organizacional**
- Onboarding eficaz e inclusivo aumenta drasticamente a **retenção de talentos**
- Reduz **custos de recontratação**
- Garante **transferência eficiente de conhecimento**
- Torna o crescimento da empresa mais **sustentável**

---

## 🛠️ Detalhando o MVP (Requisitos Mínimos)

### 1. Funcionalidades Principais do MVP

O MVP terá **três módulos centrais** em uma aplicação web:

#### 🎵 O "Maestro" (Bot Parceiro - Eixo 3)
- **Chatbot de IA** que guia o novo funcionário
- **Não apenas reativo** (respondendo "onde encontro o manual X?")
- **Proativo** ("Notei que você ainda não configurou seus benefícios, quer ajuda?")
- Sistema de feedback com thumbs up/down para melhorar respostas
- Handoff para RH em casos que excedem a base de conhecimento

#### 🎮 Jornada Gamificada (Eixo 6)
Dashboard de onboarding que transforma tarefas burocráticas e treinamentos em **"trilha de missões"**

**Exemplos de "Missões":**
- **"Conheça seu time!"** → agendar um café virtual (10 pontos)
- **"Desbloqueie seu setup!"** → completar o checklist de TI (15 pontos)
- **"Mestre da Cultura"** → ler o guia de cultura e responder um quiz (20 pontos)
- **"Primeiro Mentor"** → conectar-se com um mentor sugerido (25 pontos)

**Sistema de Badges:**
- 🥉 Bronze (50 pts) - Novato Integrado
- 🥈 Prata (100 pts) - Colaborador Ativo
- 🥇 Ouro (150 pts) - Embaixador da Cultura

#### 🤝 Conector de Mentoria (Eixo 5)
- Sistema que sugere **mentores ou "buddies"** para o novo funcionário
- **Principal funcionalidade de IA/ML** do projeto
- Explicações transparentes para cada sugestão ("Carlos tem 85% de match com você")

---

### 2. Escopo de 5 Dias (Time de 5 pessoas)

**Entregáveis realistas:**

| Dia | Entregável | Responsável |
|-----|------------|-------------|
| **1** | Setup + Dataset sintético | Pessoa 1 (Dados) + Pessoa 2 (Backend) |
| **2** | Bot básico + API | Pessoa 2 (Backend) + Pessoa 3 (IA) |
| **3** | Recomendação ML + Frontend | Pessoa 3 (IA/ML) + Pessoa 4 (Frontend) |
| **4** | Gamificação + Dashboard | Pessoa 4 (Frontend) + Pessoa 5 (R/Análise) |
| **5** | Análise R + Vídeo + PDF | Todo o time |

**Funcionalidades MVP (simplificadas):**
- ✅ Bot básico: FAQ com 10 documentos, respostas simples (pode usar API Gemini gratuita)
- ✅ Matching: 200 perfis sintéticos, recomendação por similaridade básica
- ✅ Gamificação: 4 missões principais, sistema de pontos simples
- ✅ Dashboard: 2 gráficos essenciais (dúvidas comuns, progresso de missões)
- ✅ Análise em R: EDA do dataset e 1 métrica de fairness
- ✅ Deploy: Frontend local + Backend local (ou Render gratuito se der tempo)

---

## 🧠 Aplicação de IA, ML e Outras Disciplinas

### Inteligência Artificial (IA) / Machine Learning (ML)

#### 🎵 Chatbot "Maestro" (RAG)
- **Arquitetura RAG** (Retrieval-Augmented Generation)
- IA usando APIs (Gemini/OpenAI) ou modelo open-source (Llama 3.2)
- Responde perguntas baseada em **base de conhecimento privada**
- Documentos da empresa, manuais, FAQs

**Fluxo técnico simplificado:**
1. Usuário faz pergunta → busca por palavra-chave nos documentos
2. Contexto + query → API Gemini (gratuita) gera resposta
3. Log básico da interação

**Controles básicos:**
- Login simples (sem RBAC complexo no MVP)
- Todos os documentos são públicos (FAQ da empresa)
- Logs simples em arquivo JSON

**Métricas (demonstração):**
- Contagem de perguntas por categoria
- Satisfação simulada (mock de 75%)

#### 🎯 Motor de Recomendação (Mentoria)
**Modelo de ML principal** usando filtragem baseada em conteúdo com embeddings

**Objetivo:** Dar "match" entre novos funcionários e mentores

**Features (Variáveis):**
- **Habilidades técnicas** (Python, Design, Marketing)
- **Habilidades interpessoais** (Liderança, Comunicação, Mentoria)
- **Interesses** (Voluntariado, Inovação, Sustentabilidade)
- **Metas de carreira** (Mudar de área, Liderar time, Especializar-se)
- **Preferências de comunicação** (reuniões curtas, assíncrono, semanal)

**Abordagem técnica simplificada:**
1. **Vetorização básica:** Usar TF-IDF ou contagem de skills comuns (sklearn)
2. **Similaridade:** Calcular overlap de habilidades e interesses
3. **Ranking:** Top-3 mentores por score simples (% de match)
4. **Explicabilidade:** "Carlos tem 3 skills em comum: Liderança, Python, Inovação"

**Métricas básicas:**
- Todos os perfis recebem pelo menos 2 sugestões
- Exibir % de matches interdepartamentais
- Fairness simples: contar distribuição de recomendações por departamento

#### ⚖️ Inclusão Ética (Eixo 5)
- Modelo treinado para priorizar **conexões interdepartamentais**
- Aumenta a **diversidade**
- Quebra silos e **preconceitos inconscientes**
- Auditoria de fairness: análise de Disparate Impact e TPR gap em R

---

### Stack Tecnológico (Versão Hackathon)

| Disciplina | Tecnologia | Aplicação |
|------------|------------|-----------||
| **Back-end** | Python (Flask ou FastAPI) | API REST simples |
| **Front-end** | React (ou HTML/CSS/JS simples) | Dashboard e interface |
| **Banco de Dados** | SQLite ou PostgreSQL local | Perfis, logs, progresso |
| **IA** | API Gemini (gratuita) | Respostas do bot |
| **ML** | scikit-learn (TF-IDF) | Matching por similaridade |
| **Cloud** | Render (opcional) ou local | Deploy se houver tempo |
| **Análise** | R + RMarkdown | EDA e gráficos |
| **Logs** | JSON ou CSV | Tracking simples |

---

### Segurança e Privacidade (MVP Simplificado)

**Controles básicos:**

1. **Autenticação simples:**
   - Login mock (sem senha real, apenas seleção de perfil)
   - 2 tipos de usuário: colaborador e RH

2. **Proteção de Dados:**
   - Dataset 100% sintético (nomes gerados por Faker)
   - API keys em arquivo .env (não commitar)
   - Dados locais (sem exposição pública)

3. **Documentação de Segurança:**
   - Descrever no PDF que em produção seria necessário:
     - Autenticação real (OAuth)
     - HTTPS
     - RBAC granular
     - Criptografia de dados sensíveis
   - Para a POC: foco em demonstrar funcionalidade, não segurança enterprise

---

## 📊 Coleta, Tratamento e Análise de Dados

### Coleta e Tratamento (Dados Simulados)

#### O que fazer:
Criar um **dataset sintético** (~500 "funcionários")

#### Estrutura do Dataset (simplificada):
```python
Colunas: 
- id: int
- nome: str (gerado por Faker)
- departamento: str (TI, RH, Vendas, Marketing)
- cargo: str (Júnior, Pleno, Sênior)
- habilidades: str (ex: "Python, Liderança, Comunicação")
- interesses: str (ex: "Sustentabilidade, Inovação")
- disponivel_mentoria: bool
```

**Quantidade:** 200 perfis (suficiente para demonstração)

#### Tratamento:
- **Vetorização:** TF-IDF das habilidades e interesses (sklearn)
- **Normalização:** Lowercase, remoção de pontuação
- **Armazenamento:** SQLite ou CSV (simples)
- **Fairness:** Contar distribuição por departamento e cargo

### Análise de Dados (Resultados)

**Dashboard Simplificado:**

1. **Gráfico 1: Dúvidas mais comuns**
   - Barra simples com top 5 categorias de perguntas

2. **Gráfico 2: Progresso de missões**
   - % de conclusão das 4 missões principais

**Análise em R:**
- EDA: distribuição de perfis por departamento e cargo
- Gráfico: distribuição de habilidades mais comuns
- Métrica fairness: % de matches interdepartamentais
- Relatório RMarkdown simples (2-3 páginas)

---

### Métricas do MVP (demonstração)

| Métrica | Como demonstrar |
|---------|----------------|
| Uso do bot | Contar perguntas por categoria |
| Matching funcional | 100% dos perfis recebem 3 sugestões |
| Gamificação | Simular 70% de conclusão de missões |
| Fairness básica | % de matches interdepartamentais |
| Dashboard | 2 gráficos funcionais em R |

---

## 🎬 Demonstração Prática em Vídeo

### Roteiro Sugerido (5 minutos):

#### 1. O Problema (30s)
> *"70% dos novos funcionários sentem-se perdidos na primeira semana. O onboarding tradicional é impessoal, ineficiente e muitas vezes excludente. Isso impacta retenção e bem-estar."*

#### 2. A Solução (1 min)
> *"Apresentando o 'Symphony', o parceiro de carreira IA que combina bot inteligente, mentoria ética e gamificação. Ele guia, conecta e engaja desde o primeiro dia."*

#### 3. Demo 1: A Jornada (1.5 min)
- Mostrar novo usuário **"Ana"** fazendo login
- Ela vê sua **trilha gamificada** com 6 missões
- Interage com o bot **"Maestro"** para tirar dúvida simples ("Onde encontro o manual de benefícios?")
- Bot responde com contexto relevante e sugere próxima missão
- Ana dá thumbs up na resposta

#### 4. Demo 2: A Conexão (1.5 min)
- **"Ana"** chega à missão **"Encontre seu Mentor"**
- Ela preenche **perfil de interesses** (3 habilidades que quer desenvolver + 2 interesses pessoais)
- O **"Symphony"** processa (mostrar "IA analisando 500 perfis...")
- Sugere **3 mentores** com explicações detalhadas:
  > *"Carlos Silva - 85% de match*  
  > *Habilidades comuns: Liderança, Comunicação*  
  > *Interesses comuns: Sustentabilidade*  
  > *Bonus: Conexão interdepartamental (Produto ↔ TI) +10%"*
- Ana seleciona um mentor e agenda primeiro encontro

#### 5. Demo 3: Dashboard (1 min)
- Alternar para **visão do RH**
- Mostrar dashboard analítico:
  - Gráfico de dúvidas mais comuns (top 5)
  - Taxa de conclusão de missões: 72% na semana 1
  - Carga de mentoria por departamento (balanceamento)
  - **Destaque de Fairness:** "Disparate Impact = 0.95 (dentro da meta ética)"

#### 6. Integração Técnica (45s)
> *"Symphony integra as disciplinas do curso: bot com IA (Cybersecurity para dados), recomendação ML (Machine Learning), análise em R (Linguagem R), API Python (Python), Banco de Dados (SQLite/Postgres), deploy (Cloud opcional) e princípios de inclusão (Formação Social)."*

#### 7. O Impacto (30s)
> *"Com o Symphony, aumentamos a conclusão de onboarding em 30%, promovemos conexões interdepartamentais (+40%) e garantimos fairness ética. Criamos um trabalho mais humano, inclusivo e sustentável."*

**Total: ~5 minutos**

---

## ✅ Vantagens da Proposta "Symphony"

### 🎯 **Pontos Fortes:**
- ✅ Combina **3 eixos temáticos** de forma coesa
- ✅ Foca em **problema real** (onboarding ineficaz)
- ✅ **Impacto humano claro** (conexão, bem-estar, inclusão)
- ✅ **Funcionalidade prática** (bot + matching + gamificação)

### 🚀 **Viabilidade Técnica:**
- ✅ **MVP executável em 5 dias** com 5 pessoas
- ✅ Usa **tecnologias simples** (APIs gratuitas, bibliotecas conhecidas)
- ✅ **Dados sintéticos** fáceis de gerar
- ✅ **Demonstração visual** direta
- ✅ **Sem dependências complexas**

---

## 📋 Cobertura das Disciplinas (7 disciplinas)

### Cybersecurity
- **Contribuição:** Proteção básica de dados e boas práticas
- **Conceitos aplicados:** Dados sintéticos, variáveis de ambiente, documentação de segurança
- **Entregável:** Dataset anonimizado, API keys em .env, seção de segurança no PDF

### Machine Learning
- **Contribuição:** Sistema de recomendação de mentores
- **Conceitos aplicados:** TF-IDF, similaridade de cosseno, content-based filtering
- **Entregável:** Script de matching que retorna top-3 mentores por perfil

### Linguagem R
- **Contribuição:** Análise exploratória de dados
- **Conceitos aplicados:** EDA, visualização (ggplot2), estatística descritiva
- **Entregável:** RMarkdown com gráficos de distribuição e métrica de fairness

### Python
- **Contribuição:** Backend e processamento de dados
- **Conceitos aplicados:** Flask/FastAPI, geração de dados (Faker), APIs REST
- **Entregável:** API funcional, script de geração do dataset, integração com Gemini

### Computação em Nuvem
- **Contribuição:** Deploy da aplicação (se houver tempo) ou documentação de deploy
- **Conceitos aplicados:** PaaS (Render/Vercel), variáveis de ambiente
- **Entregável:** App deployado OU instruções detalhadas de deploy no README

### Banco de Dados
- **Contribuição:** Armazenamento de perfis e logs
- **Conceitos aplicados:** Modelagem relacional, SQL, índices
- **Entregável:** Schema SQL com tabelas `profiles`, `missions`, `logs`

### Formação Social
- **Contribuição:** Foco em inclusão e impacto humano
- **Conceitos aplicados:** Diversidade, acessibilidade, ética em IA
- **Entregável:** Seção no PDF sobre inclusão, linguagem clara na interface, análise de impacto

---

## 📅 Cronograma Detalhado (5 dias, 5 pessoas)

### Distribuição de Papéis:
- **Pessoa 1 (Dados/DB):** Dataset sintético, schema, logs
- **Pessoa 2 (Backend/Python):** API, integração Gemini, matching
- **Pessoa 3 (ML/IA):** Algoritmo de recomendação, bot
- **Pessoa 4 (Frontend):** Interface, gamificação, dashboard
- **Pessoa 5 (R/Análise):** EDA, gráficos, relatório

| Dia | Pessoa 1 (Dados/DB) | Pessoa 2 (Backend) | Pessoa 3 (ML/IA) | Pessoa 4 (Frontend) | Pessoa 5 (R) |
|-----|---------------------|-------------------|------------------|--------------------|--------------|
| **1** | Gerar 200 perfis sintéticos (Faker) | Setup Flask/FastAPI, estrutura de pastas | Pesquisar API Gemini e TF-IDF | Setup React ou HTML/CSS | Setup R, instalar pacotes |
| **2** | Schema SQLite, inserir dados | Endpoint `/chat` com Gemini API | Implementar busca em docs (10 FAQs) | Interface do chat | Começar EDA do dataset |
| **3** | Criar tabela de logs | Endpoint `/recommend` | Algoritmo TF-IDF para matching | Tela de recomendações | Gráficos de distribuição |
| **4** | Popular missões no DB | Integrar tudo na API | Testar matching, ajustar | Gamificação (4 missões + pontos) | Análise de fairness |
| **5** | Exportar dados para PDF | Testar API, gravar demo | Revisar bot e matching | Dashboard com 2 gráficos | Finalizar RMarkdown |

### Tarefas Coletivas (Dia 5 tarde):
- **Vídeo:** Todos participam da gravação (divisão de falas)
- **PDF:** Cada pessoa documenta sua parte
- **Revisão:** Todos testam a aplicação

---

## 📦 Estrutura de Entrega

### Repositório GitHub (Privado)

```
symphony-gs2025/
├── README.md                    # Setup e instruções de uso
├── backend/
│   ├── app.py                  # Flask/FastAPI app principal
│   ├── chat.py                 # Endpoint do bot (Gemini)
│   ├── recommend.py            # Endpoint de matching (TF-IDF)
│   ├── database.py             # Conexão SQLite
│   ├── requirements.txt        # Dependências Python
│   └── .env.example            # Template de API keys
├── frontend/
│   ├── index.html              # Página principal
│   ├── chat.html               # Interface do chat
│   ├── missions.html           # Trilha gamificada
│   ├── dashboard.html          # Dashboard RH
│   └── style.css               # Estilos
├── data/
│   ├── generate_profiles.py    # Gera 200 perfis (Faker)
│   ├── profiles.csv            # Dataset sintético
│   ├── documents/              # 10 FAQs em .txt
│   └── schema.sql              # Schema do banco
├── r_analysis/
│   ├── eda.Rmd                 # Análise exploratória
│   ├── eda.html                # Output do RMarkdown
│   └── plots/                  # Gráficos salvos
└── docs/
    ├── arquitetura.png         # Diagrama simples
    └── screenshots/            # Prints da demo
```

### PDF de Entrega

**Estrutura mínima:**

1. **Capa:**
   - Nome do projeto: **Symphony**
   - Nome completo dos integrantes + RMs
   - Link do vídeo (YouTube não listado, **SEM MASCARAR**)
   - Link do GitHub privado (com tutor adicionado)

2. **Introdução (1-2 páginas):**
   - Contexto do problema (onboarding ineficaz)
   - Objetivos do projeto
   - Como atende aos 3 pilares (humano, inclusivo, sustentável)

3. **Desenvolvimento (5-8 páginas):**
   - Arquitetura da solução (diagrama)
   - Descrição dos 3 módulos (Maestro, Mentoria, Gamificação)
   - Stack tecnológico e justificativas
   - Integração das 9 disciplinas (seção por seção)
   - Segurança e privacidade
   - Dataset sintético e processamento

4. **Resultados Esperados (2-3 páginas):**
   - KPIs e métricas alcançadas
   - Screenshots da aplicação
   - Gráficos do dashboard
   - Análise de fairness (R)

5. **Conclusões (1 página):**
   - Impacto humano e técnico
   - Lições aprendidas
   - Próximos passos (pós-hackathon)

6. **Anexos:**
   - Código comentado dos módulos principais
   - Exemplos de prompts do RAG
   - Query SQL do schema

---

## 🎯 Checklist Final (Antes da Entrega)

### Código
- [ ] Repositório privado no GitHub
- [ ] Tutor adicionado como colaborador
- [ ] README com instruções claras
- [ ] .env.example com GEMINI_API_KEY
- [ ] Código comentado em português

### Aplicação (Local OK)
- [ ] Bot respondendo 10 perguntas básicas
- [ ] Matching retornando 3 sugestões
- [ ] 4 missões visíveis e clicáveis
- [ ] 2 gráficos funcionais
- [ ] Dataset de 200 perfis carregado

### Documentação
- [ ] PDF com todas as seções (intro, desenvolvimento, resultados, conclusão)
- [ ] Screenshots de cada funcionalidade
- [ ] Código principal comentado anexado
- [ ] Link do vídeo **SEM MASCARAR**
- [ ] Link do GitHub privado

### Vídeo
- [ ] Máximo 5-7 minutos
- [ ] Demo dos 3 módulos (chat, matching, gamificação)
- [ ] Mostrar dashboard com gráficos
- [ ] Explicar integração das disciplinas
- [ ] Upload no YouTube (não listado)

### R Analysis
- [ ] RMarkdown compilado (HTML ou PDF)
- [ ] Pelo menos 2 gráficos (distribuição + fairness)
- [ ] Texto explicativo em português

---

## 💡 Pontos de Atenção para Execução

1. **Priorizar funcionalidade sobre perfeição:** MVP funcional é melhor que código perfeito incompleto
2. **Comunicação diária:** Daily rápida (15 min) para alinhar progresso
3. **Dados mock são OK:** Dataset sintético é suficiente para POC
4. **Deploy local é válido:** Se não der tempo de subir na nuvem, rodar local com prints
5. **Documentar enquanto faz:** Não deixar PDF e vídeo para última hora
6. **Testar integrado:** No dia 4, fazer primeira integração completa
7. **Backup de decisões:** Se algo não funcionar, ter plano B simples

---

**Data da Proposta Simplificada:** 13 de novembro de 2025  
**Fonte Original:** Gemini  
**Adaptação:** GitHub Copilot  
**Contexto:** Global Solutions 2025.2 - O Futuro do Trabalho  
**Escopo:** 5 dias | 5 pessoas | Entrega funcional
