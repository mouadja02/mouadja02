<!-- ============================ HERO ============================ -->
<div align="center">

![Mouad Jaouhari — Data & AI Engineer](./header.svg)

<br/>

[![Portfolio](https://img.shields.io/badge/Portfolio-0c0a09?style=for-the-badge&logo=About.me&logoColor=00f0ff)](https://mouadja02.github.io)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/j-mouad)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mouadpro02@gmail.com)
[![Profile Views](https://komarev.com/ghpvc/?username=mouadja02&color=a855f7&style=for-the-badge&label=VISITORS)](https://github.com/mouadja02)

</div>

---

<!-- ============================ AGENT MANIFEST ============================ -->

### `~/ whoami` &nbsp;·&nbsp; the manifest, as an agent would read it

```yaml
# mouad.agent.yaml — system manifest
identity:
  name:    Mouad Jaouhari          # alias: MJ
  role:    Data & AI Engineer
  company: ATOS
  motto:   "From signals to systems — now with a mind of their own."

mission: >
  Turn raw, messy data into autonomous systems that
  retrieve, reason, and act — not just dashboards that report.

operating_loop: [ plan, retrieve, act, observe, reflect ]

stack:
  data:    [ Snowflake, Spark, Airflow, Kafka, dbt, Iceberg ]
  agentic: [ LangGraph, LangChain, RAG, CAG ]
  memory:  [ Qdrant, Pinecone ]
  tooling: [ Claude Code, OpenAI Codex, Cursor ]
  cloud:   [ AWS, GCP, Cloudflare ]

currently_building: [ dacli, dag-doctor, CAG-Lab ]
status: "open to agentic-AI & data-platform collaborations"
```

---

<!-- ============================ AGENT ORCHESTRATION GRAPH ============================ -->
<div align="center">

![Agent Orchestration Graph](./skills-constellation.svg)

</div>

---

<!-- ============================ HOW I BUILD AGENTS ============================ -->

### How I think about agents — the reasoning loop

I don't build chatbots; I build systems that **plan, pull their own context, take actions, and self-correct**. Every agent I ship runs some version of this loop:

```mermaid
%%{init: {'theme':'dark','themeVariables':{'primaryColor':'#0d1117','primaryTextColor':'#e7e5e4','primaryBorderColor':'#00f0ff','lineColor':'#a855f7','fontFamily':'monospace','fontSize':'15px'}}}%%
flowchart LR
    U([ prompt ]) --> P[plan]
    P --> R["retrieve<br/>Qdrant · Pinecone"]
    R --> A["act<br/>tools · APIs · SQL"]
    A --> O[observe]
    O --> D{goal met?}
    D -->|no| Rf[reflect] --> P
    D -->|yes| Out([ answer / action ])
```

---

<!-- ============================ DATA -> INTELLIGENCE PIPELINE ============================ -->
<div align="center">

![Data to Intelligence Pipeline](./data-pipeline-flow.svg)

</div>

---

<!-- ============================ TECHNICAL ARSENAL ============================ -->
<div align="center">

## Technical Arsenal

**Agentic AI · LLM Engineering**

![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-2E1065?style=for-the-badge&logoColor=white)
![RAG](https://img.shields.io/badge/RAG_+_CAG-7c3aed?style=for-the-badge&logoColor=white)
![Qdrant](https://img.shields.io/badge/Qdrant-DC244C?style=for-the-badge&logo=qdrant&logoColor=white)
![Pinecone](https://img.shields.io/badge/Pinecone-000000?style=for-the-badge&logo=pinecone&logoColor=white)
![Claude](https://img.shields.io/badge/Claude_Code-D97757?style=for-the-badge&logo=anthropic&logoColor=white)
![OpenAI Codex](https://img.shields.io/badge/OpenAI_Codex-412991?style=for-the-badge&logo=openai&logoColor=white)
![Cursor](https://img.shields.io/badge/Cursor-0c0a09?style=for-the-badge&logo=cursor&logoColor=00f0ff)
![Hugging Face](https://img.shields.io/badge/Hugging_Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)
![n8n](https://img.shields.io/badge/n8n-EA4B71?style=for-the-badge&logo=n8n&logoColor=white)

**Data Engineering**

![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white)
![Apache Spark](https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apache-spark&logoColor=white)
![Airflow](https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=apache-airflow&logoColor=white)
![Kafka](https://img.shields.io/badge/Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white)
![Iceberg](https://img.shields.io/badge/Apache_Iceberg-1C9BD6?style=for-the-badge&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

**Languages · ML**

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![C](https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black)
![CUDA](https://img.shields.io/badge/NVIDIA_CUDA-76B900?style=for-the-badge&logo=nvidia&logoColor=white)

**Cloud · DevOps**

![GCP](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)
![AWS](https://img.shields.io/badge/Amazon_AWS-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=cloudflare&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)

</div>

---

<!-- ============================ CAPABILITY MATRIX ============================ -->
<div align="center">

![Capability Matrix](./skill-bars.svg)

</div>

---

<!-- ============================ FEATURED BUILDS ============================ -->
<div align="center">

## Featured Builds — where Data meets Agents

<table align="center">
<tr>
<td width="50%" valign="top" align="left">

#### [dacli](https://github.com/mouadja02/dacli)
An intelligent CLI agent that builds production-grade data warehouses from scratch on your chosen data platform.

![Agentic](https://img.shields.io/badge/Agentic-a855f7?style=flat-square) ![LangGraph](https://img.shields.io/badge/LangGraph-1c1917?style=flat-square) ![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=flat-square&logo=snowflake&logoColor=white)
</td>
<td width="50%" valign="top" align="left">

#### [dag-doctor](https://github.com/mouadja02/dag-doctor)
An AI assistant that explains failed Airflow DAGs, pinpoints the root cause, and suggests safe fixes.

![AI Ops](https://img.shields.io/badge/AI_Ops-a855f7?style=flat-square) ![Airflow](https://img.shields.io/badge/Airflow-017CEE?style=flat-square&logo=apacheairflow&logoColor=white) ![LLM](https://img.shields.io/badge/LLM-1c1917?style=flat-square)
</td>
</tr>
<tr>
<td width="50%" valign="top" align="left">

#### [CAG-Lab](https://github.com/mouadja02/CAG-Lab)
Benchmarking Cache-Augmented Generation (CAG) against RAG for real-world knowledge systems.

![Research](https://img.shields.io/badge/Research-a855f7?style=flat-square) ![RAG vs CAG](https://img.shields.io/badge/RAG_vs_CAG-1c1917?style=flat-square) ![Vector DB](https://img.shields.io/badge/Vector_DB-1c1917?style=flat-square)
</td>
<td width="50%" valign="top" align="left">

#### [skills](https://github.com/mouadja02/skills)
A curated collection of 149 agent skills for Claude Code & Cursor — engineering craft, AI agents, prompt engineering, and more.

![149 skills](https://img.shields.io/badge/149_skills-a855f7?style=flat-square) ![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=flat-square&logo=anthropic&logoColor=white) ![Cursor](https://img.shields.io/badge/Cursor-1c1917?style=flat-square&logo=cursor&logoColor=00f0ff)
</td>
</tr>
<tr>
<td width="50%" valign="top" align="left">

#### [bitcoin-technical-indicators-dataset](https://github.com/mouadja02/bitcoin-technical-indicators-dataset)
Bitcoin hourly OHLCV with 70+ technical indicators — a daily-updated dataset for ML & trading analysis.

![Dataset](https://img.shields.io/badge/Dataset-00f0ff?style=flat-square) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![ML](https://img.shields.io/badge/ML-1c1917?style=flat-square)
</td>
<td width="50%" valign="top" align="left">

#### [end2end-datawarehouse-project](https://github.com/mouadja02/end2end-datawarehouse-project)
End-to-end data platform with real-time streaming and cloud processing — Kafka, Spark, AWS Glue, Snowflake, Iceberg.

![Streaming](https://img.shields.io/badge/Streaming-00f0ff?style=flat-square) ![Kafka](https://img.shields.io/badge/Kafka-231F20?style=flat-square&logo=apachekafka&logoColor=white) ![Spark](https://img.shields.io/badge/Spark-E25A1C?style=flat-square&logo=apachespark&logoColor=white)
</td>
</tr>
</table>

<sub>also brewing &nbsp;·&nbsp; <code>murmur</code> (local-LLM prompt overlay) &nbsp;·&nbsp; <code>mnemex</code> (LLM memory vault) &nbsp;·&nbsp; <code>neural-network-cuda</code> (NN from scratch → CUDA)</sub>

</div>

---

<!-- ============================ STATS ============================ -->
<div align="center">

## By the Numbers

<img height="175" src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=mouadja02&theme=github_dark" />
<img height="175" src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=mouadja02&theme=github_dark" />

<br/>

<img src="https://streak-stats.demolab.com?user=mouadja02&hide_border=true&background=0a0a0f&stroke=1c1917&ring=00f0ff&fire=a855f7&currStreakLabel=00f0ff&sideLabels=a8a29e&dates=52525b&currStreakNum=fafaf9&sideNums=fafaf9&dayLabels=a8a29e" />

<br/>

![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=mouadja02&bg_color=0a0a0f&color=00f0ff&line=a855f7&point=ffffff&area=true&area_color=a855f7&hide_border=true)

</div>

---

<div align="center">

### Let's build systems that think.

<i>From raw signals → reasoning systems.</i>

[![Portfolio](https://img.shields.io/badge/Portfolio-0c0a09?style=for-the-badge&logo=About.me&logoColor=00f0ff)](https://mouadja02.github.io)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/j-mouad)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mouadpro02@gmail.com)

</div>
