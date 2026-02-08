# Rui Shao

Production infrastructure engineer. Kubernetes, distributed systems, observability. US/EU market focus.

## Positioning

I build and operate systems that stay up. AI infra, observability, high-throughput data pipelines. Less hype, more runbooks.

## Core domains

- Production infrastructure (Kubernetes, Docker, Helm)
- AI infrastructure (task lifecycle, scheduling, model deployment)
- Observability (Prometheus, Grafana, Loki, InfluxDB)
- Distributed systems (gRPC, Kafka, Redis, MySQL)

## Signature experience

- Built AI task lifecycle management platform with Kubernetes Operator — workflow scheduling, deployment, versioning for training and inference
- Optimized large-scale offline data image pull (kube-fledged, containerd) — reduced cold start by 60%
- Developed high-traffic gRPC metrics service — async streaming, object pooling, Goroutine reuse; latency 200ms→50ms, memory -40%
- Deployed Prometheus Kubernetes Operator for 100+ metrics; scaled Loki with Promtail sharding; Kafka 100k msg/sec

## Engineering philosophy

- Reliability is a practiced discipline, not a feature
- Cost visibility precedes cost optimization
- Deployments are a primary failure mode; design for rollback first
- External dependencies are single points of failure; treat them like your own infra

## Current focus

- AI infrastructure: cost-aware routing, evaluation pipelines, agent orchestration
- Safe deployment patterns
- Observability layering (when to use logs vs metrics vs traces)

## Repos

- [production-infra-casebook](https://github.com/ryan42xyz/production-infra-casebook) — case studies and postmortems
- [architecture-notes](https://github.com/ryan42xyz/architecture-notes) — design notes and patterns
- [ai-infra-lab](https://github.com/ryan42xyz/ai-infra-lab) — AI infra experiments and directions
