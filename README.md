# Rui Shao

Senior Site Reliability Engineer by day. I build production control systems for large-scale Kubernetes and cloud environments (AWS 6 regions, 30+ clusters, 600+ nodes). Outside work: AI infrastructure, agentic workflows, and tools that extend what one person can operate alone.

Blog: [ryan42xyz.github.io](https://ryan42xyz.github.io/) · GitHub: [@ryan42xyz](https://github.com/ryan42xyz) · Email: [sr1054461216@gmail.com](mailto:sr1054461216@gmail.com)

## Core positioning

I treat production as a controllable system: make change safer, isolate failure, shorten recovery, and keep efficiency sustainable under SLO guardrails.

## What I focus on

- Safer change: progressive rollouts, pause/rollback gates, compatibility preflights (CRDs/webhooks/add-ons).
- Traffic control across clusters/regions: weighted routing for canary, cutover, failover, and staged failback.
- Observability that's actionable during incidents: service-impact signals (latency/error/saturation, SLO burn), incident views that join metrics/logs/changes/deps.
- Cost work with reliability guardrails: Reserved/On-Demand/Spot by workload criticality + interruption tolerance; lifecycle/tiered storage; topology-aware placement.
- On-call recovery: symptom-first triage (`refused` vs `timeout`, waiting vs upstream latency, app vs node pressure), smallest-safe mitigation, codified runbooks.

## Experience highlights

### Datavisor — Senior Site Reliability Engineer (Japan) (2025/10–Present); Site Reliability Engineer (China) (2025/03–2025/10)

**AI Agent Engineering**

- Built an autonomous SRE triage agent as a Claude Code skill, used in daily on-call to auto-investigate production alerts via structured debug trees and MCP tool calls (VictoriaMetrics, Grafana, Loki).
- Designed 3-layer code-level safety system — query validation, cluster-tier enforcement, scope tracking — ensuring all agent operations are read-only; unknown environments default to the most restrictive policy.
- Engineered a 132-file knowledge base (6-cluster routing, 7 executable debug trees, 35 incident cases) with JSONL observability tracing for every tool call and safety decision.

**Infrastructure & Reliability** _(AWS 6 regions | K8s 30+ clusters | 600+ nodes)_

- Led production Kubernetes upgrades (1.24→1.29) across 30+ clusters; built automation tool cutting per-cluster time from **18–21h to 3–4h** with **zero incidents**.
- Designed distributed auto traffic-switch system across 4 AWS/K8s backends, reducing failover from manual **5–15 min to seconds**.

**Observability & On-call** _(40 tenants | ~1.2M active series)_

- Built full-stack monitoring (VictoriaMetrics + Grafana + Loki) serving 30 clusters and 40 tenants; migrated from Prometheus Federation, eliminating weekly OOM and reducing data lag from **45s to <5s**.
- Designed 3-tier alerting with per-tenant SLI rules, enabling tenant-level fault isolation and SLA tracking.
- Primary on-call for 30+ production clusters; resolved **20+ P1/P2 incidents** with avg MTTR **~30 min**.

### Intel — Cloud Software Development Engineer (China) (2022/06–2025/02)

Developed Go microservices and Kubernetes operators for platform tooling; owned production monitoring infrastructure and collaborated with product teams to design end-to-end observability (OpenTelemetry → Kafka → Prometheus/InfluxDB).

### Earlier internships

- **Tencent** (Software Development Engineer Intern, 2021/05–2021/09): Go gRPC microservices for live-streaming workloads (Kafka, MySQL, Redis).
- **ByteDance** (Software Development Engineer Intern, 2021/03–2021/05)
- **App Annie** (Web Backend Engineer Intern, 2020/11–2021/02)
- **Baidu** (Data Engineer Intern, 2020/01–2020/10)

## Projects

- **[ryan42xyz/agents](https://github.com/ryan42xyz/agents)** — SRE Triage Agent (Anthropic SDK reimplementation with full agent loop, safety gates, eval framework)
- **[ryan42xyz/context-infrastructure](https://github.com/ryan42xyz/context-infrastructure)** — Personal AI-native context system, memory architecture, and agentic workflow infrastructure
- **[ryan42xyz/chatgpt_flow](https://github.com/ryan42xyz/chatgpt_flow)** — Browser extension to extract and organize ChatGPT conversation data

## Skills

- **Languages**: Python, Go, Java, Shell, SQL
- **Infra & data**: AWS, GCP, Kubernetes, Docker, MySQL, Yugabyte, ClickHouse, Redis, Kafka, Elasticsearch
- **Observability & platform**: Prometheus, VictoriaMetrics, InfluxDB, Grafana, Loki, gRPC, Helm, Git, Jenkins
- **Human languages**: Chinese, English

## Education

- **Master** — University of Science & Technology Beijing, Computer Science and Technology (2019/09–2022/06)
- **Bachelor** — Wenhua College, Electronic Information Engineering (2014/09–2018/06)

## Side interests

Outside of production work, I spend a lot of time at the intersection of AI and infrastructure:

- Building agentic workflows and multi-agent systems — not just using LLMs but wiring them into real operational loops
- AI-native tooling: context systems, memory architectures, orchestration patterns (heavy Claude Code / OpenCode user and contributor)
- Writing about SRE mental models, AI collaboration, and what it actually takes to operate production systems at scale
