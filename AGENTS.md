# Physical AI Enterprise Agents

Google ADK agents for Gemini Enterprise, organized by Physical AI and Robotics domain (Robot Data Operations & Teleoperation,
Policy Evaluation & Failure Diagnostics, Sim-to-Real & Synthetic Data Pipeline, Fleet Telemetry & Predictive Maintenance,
Safety, Compliance & Policy Release). Agents are defined declaratively via ADK's YAML Agent Config and answer
operational and technical questions by querying BigQuery through the Conversational Analytics API
(`ask_data_insights`), supplemented by Google Search grounding for external robotics research, IEEE RAS standards, and ISO/OSHA specifications.

**`CLAUDE.md`, `GEMINI.md`, and `AGENTS.md` must be kept 100% byte-identical** at all times via `cp CLAUDE.md GEMINI.md && cp CLAUDE.md AGENTS.md && cmp CLAUDE.md GEMINI.md && cmp CLAUDE.md AGENTS.md`. Always update all three in sync whenever project state, conventions, or instructions change.

## Current State

The scaffolding infrastructure (template, shared instruction fragments, generator script) is
domain-agnostic. 5 flagship enterprise agents are fully built, tested, and registered across 5 Physical AI & Robotics domains:
- **Robot Data Operations & Teleoperation (1 agent)** (`domains/robot_data_ops/agents/`)
- **Policy Evaluation & Failure Diagnostics (1 agent)** (`domains/policy_eval_diagnostics/agents/`)
- **Sim-to-Real & Synthetic Data Pipeline (1 agent)** (`domains/sim_to_real_synthetic/agents/`)
- **Fleet Telemetry & Predictive Maintenance (1 agent)** (`domains/fleet_telemetry_maintenance/agents/`)
- **Safety, Compliance & Policy Release (1 agent)** (`domains/safety_compliance_release/agents/`)

## Architecture & Conventions

1. **BigQuery Dataset**: `physical_ai_ent_agents`
2. **Table Naming Convention**: `<domain_id>_<agent_id>_<logical_table_stem>`
3. **Model**: `gemini-3.5-flash` with `GOOGLE_CLOUD_LOCATION=global`
4. **Callbacks**:
   - `set_current_date` populates `{temp:current_date}`
   - `set_bigquery_project` populates `{temp:bq_project_id}`
5. **Tooling**:
   - Natural Language to SQL: BigQuery Conversational Analytics API (`ask_data_insights`, `forecast`, `analyze_contribution`, `detect_anomalies`)
   - Charts: Matplotlib via `render_chart`
   - Market & Research Grounding: `google_search`
