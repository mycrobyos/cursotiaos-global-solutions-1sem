# Avaliação da Proposta "Symphony" — Global Solutions 2025.2

**Data:** 13 de novembro de 2025

---

## Resumo
- Forte conceito: bot "Maestro" (RAG), mentoria com recomendação ética e jornada gamificada.
- Alinha-se à pergunta central: humano, inclusivo e sustentável, com foco em onboarding e retenção.
- Necessita explicitar a cobertura de todas as disciplinas, segurança/privacidade, métricas de IA e documentação técnica.

## Pontuação por Critério (0–5)
- Aplicabilidade e clareza: 4.5 — problema real, solução coesa e mensurável.
- Uso criativo de IA/dados: 4.0 — RAG + recomendação; faltam métricas e fairness mais detalhadas.
- Integração técnica (todas as disciplinas): 2.5 — Python/DB/Cloud presentes; Cyber, R, Redes Neurais e Formação Social não explícitos.
- Planejamento e documentação: 3.5 — MVP e roteiro definidos; faltam arquitetura, esquema de dados e backlog.
- Comunicação visual/apresentação: 4.0 — roteiro de demo sólido.
- Colaboração/interdisciplinar: 3.0 — papéis e governança não descritos.

## Cobertura das Disciplinas (sugestões de fortalecimento)
- AICSS: desenho de agentes, governança de prompts, limites de escopo, handoffs humanos.
- Cybersecurity: SSO/OIDC, RBAC por perfil (RH/gestor/colaborador), criptografia em repouso e trânsito, gestão de segredos, logs/auditoria, DPIA e privacy-by-design; threat model (STRIDE) e mitigação OWASP Top 10; políticas de acesso à base do RAG.
- Machine Learning: detalhar features e abordagem (content-based/híbrida), métricas (Precision@k, MAP, nDCG), cold start, validação offline e A/B simulado.
- Redes Neurais: usar embeddings (ex.: bge-m3, sentence-transformers) e/ou modelo siames para matching; opcional: classificador neural de intenção para o bot.
- Linguagem R: EDA do dataset sintético e fairness (disparate impact, TPR gap) em R; relatório RMarkdown; opcional: mini dashboard Shiny para RH.
- Python: backend FastAPI, pipeline RAG (ingestão + busca), serviço de recomendação, testes unitários e scripts de treino.
- Computação em Nuvem: deploy em Cloud Run/Render/Vercel; DB gerenciado (Cloud SQL/Postgres); storage de documentos; observabilidade (logs/metrics); IaC mínimo (Terraform) opcional.
- Banco de Dados: schema com `users`, `profiles`, `skills`, `missions`, `mentor_matches`, `chat_logs`, `events`; vetor com `pgvector` ou índice dedicado (Pinecone/Weaviate); políticas de retenção.
- Formação Social: diretrizes de inclusão (WCAG, linguagem acessível), suporte à neurodiversidade (modos de interação), consentimento e transparência; plano de avaliação de bem-estar/pertencimento.

## Riscos e Lacunas
- Fairness/ética sem critérios operacionais; risco de vieses no matching.
- Segurança e privacidade ausentes para documentos internos e logs do bot.
- KPIs e evidências não definidos.
- Cobertura de R e Redes Neurais não demonstrada.
- Arquitetura e plano de deploy não documentados.

## Recomendações Práticas (alto impacto)
- Arquitetura: adicionar diagrama simples com fluxos do Bot (RAG), Recomendação e Dashboard; listar endpoints principais e schema mínimo do Postgres (+pgvector).
- Métricas: definir 6 KPIs para o vídeo e PDF — tempo de onboarding, taxa de missões (semana 1), Precision@3 no matching, cobertura de perfis, satisfação do bot (thumbs), fairness (Disparate Impact entre grupos).
- Fairness e governança: incluir constraints de diversidade (interdepartamental), auditoria de matches e painel de distribuição; política de consentimento e opt-out.
- Segurança: RBAC + segregação de coleções do RAG por departamento; mascaramento/anonimização no dataset; checklist OWASP para front/back.
- R: notebook de EDA/fairness e RMarkdown no repositório.
- Redes Neurais: adotar embeddings open-source e relatar resultados vs. baseline TF-IDF.
- Vídeo: mostrar logs do bot, painel de métricas e explicações dos matches; evidenciar decisões éticas e de segurança.

## MVP Enxuto (factível)
- Bot RAG: ingestão de 10–20 documentos, busca semântica + resposta; logs com intenções.
- Matching: dataset sintético de ~500 perfis; content-based com embeddings; reportar Precision@3 e fairness simples.
- Dashboard: trilha de missões + 3 gráficos (dúvidas comuns, taxa de missões, carga de mentoria).
- Infra: FastAPI + Postgres(+pgvector) + React; deploy em Vercel/Render com RBAC básico.

## Checklist de Entrega (PDF/Repo/Vídeo)
- PDF: link do YouTube não listado sem mascarar; link do GitHub privado; nomes; seções mínimas; diagramas; métricas e screenshots.
- Repositório: `backend/`, `frontend/`, `ml/`, `r/`, `docs/` (diagrama e threat model); `README` com comandos de execução.
- Vídeo (≤7 min): abertura “QUERO CONCORRER”, integração entre disciplinas, 3 módulos em ação, métricas/fairness e segurança, conclusão.

## Próximos Passos (sugeridos)
- Criar esqueleto de pastas + README.
- Adicionar diagrama de arquitetura e threat model.
- Gerar dataset sintético e notebooks (Python e R).
- Protótipos do RAG e do matching.
- Dashboard básico com KPIs.