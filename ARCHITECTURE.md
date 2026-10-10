# Physical AI & Robotics Enterprise Agents Architecture

Comprehensive system topology, database registry, and multi-agent routing graph for **Physical AI Enterprise Agents** on Gemini Enterprise.

---

## 1. System Topology Overview

- **Total Domains:** 5
- **Total Deployed Agents:** 5
- **Total Knowledge Graph Nodes:** 46
- **Total Relational Edges:** 35
- **Primary BigQuery Dataset:** `physical_ai_ent_agents`

---

## 2. Multi-Agent Swarm Topology

```mermaid
graph TD
    User["Robotics Operations / Policy Engineer"] -->|Natural Language Prompt| GE["Gemini Enterprise Assistant"]
    GE -->|Routes to Agent| Root["Root Orchestrator LlmAgent<br/>(gemini-3.5-flash)"]
    
    Root -->|Lifecycle Callback| CB1["tools.callbacks.set_current_date"]
    
    Root -->|Internal Telemetry & Data Lake| DI["Data Insights Sub-Agent<br/>(BigQuery CA API)"]
    Root -->|External Robotics & Standards Intel| MC["Market Context Sub-Agent<br/>(Google Search Grounding)"]
    
    DI -->|Lifecycle Callback| CB2["tools.callbacks.set_bigquery_project"]
    DI -->|NL to SQL & Forecasting| BQCA["BigQuery CA Toolset<br/>(ask_data_insights, forecast, detect_anomalies)"]
    DI -->|Visualization Request| CG["Chart Generator<br/>(render_chart -> PNG)"]
    
    BQCA -->|Authorized Table Queries| BQ[("BigQuery Dataset<br/>physical_ai_ent_agents")]
    MC -->|Real-time Research Grounding| GS["Google Search Engine (IEEE / ISO / arXiv)"]
    
    DI -->|Quantitative Data Synthesis| Root
    MC -->|Academic & Standards Context| Root
    Root -->|Combined Grounded Response| GE
    GE -->|Interactive Presentation Deck| Canvas["Interactive 4-Slide Presentation Deck"]
```

---

## 3. Physical AI Domains & Agent Inventory

| Domain ID | Strategic Domain | Deployed Agent | BigQuery Table Prefix | Core Scope |
| :---: | :--- | :--- | :---: | :--- |
| `rdop` | **Robot Data Operations & Teleoperation** | `data_collection_annotation_ops` | `rdop_dcao_*` | Teleoperation hours, annotation stages, QA velocity |
| `pedi` | **Policy Evaluation & Failure Diagnostics** | `multimodal_eval_failure_diagnostics` | `pedi_mefd_*` | Multimodal rollout retrieval, grasp failure root causes, singularities |
| `s2rs` | **Sim-to-Real & Synthetic Data Pipeline** | `synthetic_scene_curation_copilot` | `s2rs_sscc_*` | Low-data regimes, 3D USD assets, domain randomization |
| `ftpm` | **Fleet Telemetry & Predictive Maintenance** | `fleet_diagnostics_hardware_maintenance` | `ftpm_fdhm_*` | Motor thermal spikes, harmonic backlash, force-torque SOPs |
| `scpr` | **Safety, Compliance & Policy Release** | `embodied_ai_safety_audit` | `scpr_easa_*` | Torque limit verification, ISO/TS 15066 safety gates, release readiness |

---

## 4. Graph Artifacts

- SQLite Graph Database: `graphify-out/graph.sqlite`
- JSON Graph Topology: `graphify-out/graph.json`
