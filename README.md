# Rui Shao

Senior Site Reliability Engineer by day. I build production control systems for large-scale Kubernetes and cloud environments (AWS 10+ regions, 30+ clusters, 600+ nodes). Outside work: AI infrastructure, agentic workflows, and tools that extend what one person can operate alone.

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

**Deployment & Reliability** _(AWS 10+ regions | Kubernetes 30+ clusters | 600+ nodes)_

- Led end-to-end production Kubernetes upgrades (1.24→1.29) across 30+ multi-region clusters, covering control plane, worker nodes, and addon components (Calico, AWS CCM, cluster-autoscaler).
- Built an upgrade CLI (Python/Ansible/boto3) automating health checks, dry-run planning, and evidence collection — cutting per-cluster time from **18–21h to 3–4h** (~80% reduction), halving operator headcount, with **zero incidents** across the full rollout.

**Traffic & Multi-Region**

- Designed and built a distributed **auto traffic-switch system** from scratch (Master-Detector architecture), integrating 4 infrastructure backends (AWS ALB, API Gateway, Global Accelerator, Kubernetes) across 30 production clusters.
- Reduced incident traffic-switch response time from **5–15 min to seconds** by automating fault detection and switch execution, eliminating manual multi-console operations.

**Observability** _(40 tenants | ~1.2M active series | ~80K samples/sec)_

- Built production observability stack (vmagent → VictoriaMetrics cluster → vmalert → Alertmanager → Grafana + Loki) serving 30 clusters, 600 nodes, 40 tenants.
- Migrated from Prometheus Federation to VictoriaMetrics cluster; eliminated weekly OOM incidents (previously 2–3×/week), reduced global data lag from **45s to <5s**, and cut hot storage from **~930 GB to ~250 GB**.
- Designed 3-tier alerting (PAGER/HIGH/MEDIUM) with inhibition rules, per-tenant SLI recording rules, and latency decomposition (upstream vs. waiting latency via ingress access logs); enabling per-tenant fault isolation and SLA tracking across 40 clients.

**On-call & Incident Response**

- Served as primary on-call for production Kubernetes and AWS across 30+ clusters; resolved **20+ P1/P2 incidents** with avg MTTR of **~30 min**.
- Restored services through controlled mitigations (traffic splitting, cordon/drain, bounded scaling).

### Intel — Cloud Software Development Engineer (China) (2022/06–2025/02)

- Built Kubernetes platform tooling using operator-style controllers, IaC (GitOps/Ansible) cluster management.
- Developed Go-based gRPC service using OpenTelemetry SDK to transform structured messages into metrics and stream high-throughput time-series via Kafka into Prometheus and InfluxDB.

### Earlier internships

- **Tencent** (Software Development Engineer Intern, 2021/05–2021/09): Go gRPC microservices for live-streaming workloads (Kafka, MySQL, Redis).
- **ByteDance** (Software Development Engineer Intern, 2021/03–2021/05)
- **App Annie** (Web Backend Engineer Intern, 2020/11–2021/02)
- **Baidu** (Data Engineer Intern, 2020/01–2020/10)

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
