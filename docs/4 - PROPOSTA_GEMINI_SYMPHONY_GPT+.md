# Proposta Gemini - Global Solutions 2025.2
## Symphony: O Assistente de Integração e Carreira

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

#### 🎮 Jornada Gamificada (Eixo 6)
Dashboard de onboarding que transforma tarefas burocráticas e treinamentos em **"trilha de missões"**

**Exemplos de "Missões":**
- **"Conheça seu time!"** → agendar um café virtual
- **"Desbloqueie seu setup!"** → completar o checklist de TI
- **"Mestre da Cultura"** → ler o guia de cultura e responder um quiz

#### 🤝 Conector de Mentoria (Eixo 5)
- Sistema que sugere **mentores ou "buddies"** para o novo funcionário
- **Principal funcionalidade de IA/ML** do projeto

---

### 2. Escopo de 1 Semana (Hackathon)
- Bot RAG mínimo: ingestão de 10–20 documentos (FAQ/cultura), busca semântica e resposta, com logs de intenções.
- Matching de mentoria: dataset sintético (~500 perfis), recomendação content-based com embeddings e explicações dos matches.
- Jornada gamificada: trilha com 6–8 missões e registro de progresso.
- Dashboard MVP: 3 gráficos (dúvidas comuns, taxa de missões semana 1, carga de mentoria por departamento).
- Segurança básica: RBAC simples (colaborador/RH), segregação de coleções por departamento no RAG, anonimização do dataset sintético.
- Deploy simples: Frontend em Vercel; Backend em Render/Cloud Run; Postgres gerenciado com extensão de vetores (pgvector).

## 🧠 Aplicação de IA, ML e Outras Disciplinas

### Inteligência Artificial (IA) / Machine Learning (ML)

#### 🎵 Chatbot "Maestro"
- **Arquitetura RAG** (Retrieval-Augmented Generation)
- IA usando modelo open-source (Llama 3, Mistral) ou APIs (Gemini)
- Responde perguntas baseada em **base de conhecimento privada**
- Documentos da empresa, manuais, FAQs
 - Controles: coleções separadas por departamento e checagem de permissão (RBAC) antes da recuperação; logs de consultas para auditoria.
 - Métrica MVP: taxa de resolução em 1 interação e satisfação (thumbs) por resposta.

#### 🎯 Motor de Recomendação (Mentoria)
**Modelo de ML principal** usando filtragem baseada em conteúdo ou híbrida

**Objetivo:** Dar "match" entre novos funcionários e mentores

**Features (Variáveis):**
- **Habilidades técnicas** (Python, Design)
- **Habilidades interpessoais** (Liderança, Comunicação)
- **Interesses** (Voluntariado, Inovação)
- **Metas de carreira**
- **Preferências de comunicação** (reuniões curtas, assíncrono)
 
**Abordagem técnica (MVP):**
- Vetorização de perfis com embeddings (ex.: `sentence-transformers/all-MiniLM-L6-v2` ou bge-m3) e cálculo de similaridade.
- Regras de diversidade (boost interdepartamental) e filtros por disponibilidade.
- Métricas: Precision@3, cobertura de perfis recomendados, Disparate Impact simples entre grupos simulados.

#### ⚖️ Inclusão Ética (Eixo 5)
- Modelo treinado para priorizar **conexões interdepartamentais**
- Aumenta a **diversidade**
- Quebra silos e **preconceitos inconscientes**

### Stack Tecnológico Sugerido

| Disciplina | Tecnologia | Aplicação |
|------------|------------|-----------|
| **Back-end** | Python (FastAPI/Django) ou Node.js (Express) | API REST para ML, usuários e conteúdo |
| **Front-end** | React, Vue ou Angular | Dashboard e interface do chatbot |
| **Banco de Dados** | PostgreSQL (+pgvector) | Perfis, habilidades, logs, progresso, embeddings |
| **DevOps** | Vercel (FE) + Render/Cloud Run (BE) | Deploy simples; logs/monitoramento básicos |

### Segurança e Privacidade (MVP)
- Autenticação: login simples; perfis de acesso (colaborador, RH) com RBAC na API.
- RAG: autorização por coleção/departamento antes da recuperação; nenhum dado sensível real no índice.
- Criptografia: TLS em trânsito; dados sintéticos/anonimizados em repouso.
- Auditoria: logs de chat e de recomendações com IDs anônimos; retenção curta para a POC.

---

## 📊 Coleta, Tratamento e Análise de Dados

### Coleta e Tratamento (Dados Simulados)

#### O que fazer:
Criar um **dataset sintético** (~500 "funcionários")

#### Estrutura do Dataset:
```
Colunas: ID, Nome, Departamento, Cargo, 
Habilidades_Tecnicas (lista), 
Habilidades_Sociais (lista), 
Interesses (lista), 
Metas_Carreira (texto curto), 
Anos_de_Empresa
```

#### Tratamento:
- **One-Hot Encoding** ou **TF-IDF** nas colunas de listas e texto
- Transformação em **vetores numéricos** para o modelo ML
 - Fairness inicial: criação de grupos simulados e checagem de `Disparate Impact` e `TPR gap`.
 - EDA em R (RMarkdown) para documentar distribuição de habilidades e viés potencial.

### Análise de Dados (Resultados)

Dashboard que responde:

- 🤔 **"Quais as dúvidas mais comuns dos novos contratados?"** (Análise dos logs do chatbot)
- 📈 **"Quais departamentos estão sobrecarregados com pedidos de mentoria?"**
- ✅ **"Qual a taxa de conclusão das 'missões' na primeira semana?"**

### KPIs do MVP
- Tempo de onboarding (estimado pela conclusão de missões) — objetivo: +30% conclusão semana 1.
- Precision@3 do matching — objetivo: ≥0.6 em validação offline.
- Cobertura de perfis recomendados — objetivo: ≥80% dos novatos com pelo menos 2 sugestões válidas.
- Dúvidas comuns resolvidas em 1 interação — objetivo: ≥60%.
- Satisfação com respostas (thumbs up) — objetivo: ≥70%.
- Fairness (Disparate Impact 0.8–1.25) entre grupos simulados.

---

## 🎬 Demonstração Prática em Vídeo

### Roteiro Sugerido (5-7 minutos):

#### 1. O Problema (30s)
> *"O onboarding tradicional é impessoal, ineficiente e muitas vezes excludente."*

#### 2. A Solução (1 min)
> *"Apresentando o 'Symphony', o parceiro de carreira IA que..."*

#### 3. Demo 1: A Jornada (1.5 min)
- Mostrar novo usuário **"Ana"** fazendo login
- Ela vê sua **trilha gamificada**
- Interage com o bot **"Maestro"** para tirar dúvida simples

#### 4. Demo 2: A Conexão (1.5 min)
- **"Ana"** chega à missão **"Encontre seu Mentor"**
- Ela preenche **perfil de interesses**
- O **"Symphony"** processa (mostrar IA "pensando")
- Sugere **3 mentores** com explicações:
  > *"O 'Carlos' tem as habilidades de Liderança que você quer desenvolver e também se interessa por sustentabilidade"*

#### 5. O Impacto (1 min)
- Mostrar **dashboard de análise** (visão do RH)
- > *"Com o Symphony, reduzimos o tempo de onboarding em 30% e aumentamos a sensação de pertencimento, criando um trabalho mais humano, inclusivo e sustentável."*
 - Exibir KPIs: Precision@3, taxa de missões, DI de fairness e satisfação do bot.

---

## ✅ Vantagens da Proposta "Symphony"

### 🎯 **Diferenciais Competitivos:**
- ✅ Combina **3 eixos temáticos** de forma coesa
- ✅ Foca em **problema real e mensurável** (onboarding)
- ✅ **Funcionalidade inédita** (IA ética para mentoria)
- ✅ **Impacto humano claro** (retenção, bem-estar, inclusão)

### 🚀 **Viabilidade Técnica:**
- ✅ **MVP factível** para o prazo da GS
- ✅ Usa **tecnologias acessíveis** (APIs, frameworks conhecidos)
- ✅ **Dados simulados** são suficientes para demonstração
- ✅ **Demonstração visual** clara e envolvente

### 🏆 **Potencial para Pódio:**
- ✅ **Solução desafiadora** mas coesa
- ✅ **Atende todos os requisitos** técnicos
- ✅ **Aborda diretamente** a pergunta central
- ✅ **Narrativa forte** sobre humanização do trabalho

---

## Cobertura das Disciplinas (versão hackathon)
- AICSS: design do agente (Maestro), governança de prompts e limites de escopo; handoff humano para casos fora de base.
- Cybersecurity: RBAC, segregação de coleções do RAG, anonimização do dataset, checklist OWASP básico.
- Machine Learning: recomendação content-based com embeddings, validação offline e métricas (Precision@k, cobertura).
- Redes Neurais: uso de embeddings pré-treinados para matching; opcional classificador de intenção.
- Linguagem R: EDA e fairness (DI/TPR gap) em RMarkdown com dataset sintético.
- Python: FastAPI para API, serviço de RAG e recomendação, scripts de processamento e métricas.
- Computação em Nuvem: deploy FE/BE gerenciado (Vercel/Render), Postgres gerenciado com pgvector.
- Banco de Dados: schema mínimo com `users`, `profiles`, `missions`, `mentor_matches`, `chat_logs`, `events` + embeddings.
- Formação Social: diretrizes de inclusão (linguagem clara, acessibilidade WCAG básica), suporte a estilos de interação e consentimento.

## Cronograma (1 semana)
- Dia 1: dataset sintético, schema Postgres, setup FE/BE.
- Dia 2: RAG (ingestão + busca) e interface do chat.
- Dia 3: embeddings e recomendação; métricas offline.
- Dia 4: trilha gamificada e eventos; dashboard inicial.
- Dia 5: RBAC, segregação RAG, logs e KPIs.
- Dia 6: EDA/fairness em R; estabilização e prints.
- Dia 7: gravação do vídeo (roteiro GS) e revisão do PDF.

**Data da Proposta:** 12 de novembro de 2025  
**Fonte:** Gemini  
**Contexto:** Global Solutions 2025.2 - O Futuro do Trabalho