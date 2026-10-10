# Policy Evaluation & Failure Diagnostics: Multimodal Eval Failure Diagnostics

Part of the **Physical AI Enterprise Agents** platform for Gemini Enterprise.

---

## 1. Why This Agent Matters

### Business Problem
Leverages Gemini Enterprise's multimodal retrieval capabilities across evaluation rollout videos, metric tables, and run logs. Helps policy engineers query task success rates, diagnose edge-case failures, and retrieve exact rollout segments showing policy errors.

### Target Personas
Embodied AI Policy Engineer, Robotics Evaluation Lead, Reinforcement Learning Scientist, Autonomy Diagnostics Specialist

### Key Metrics Tracked
| Metric | Benchmark / Target | Business Impact |
| :--- | :--- | :--- |
| **Task Success Rate (Kitchen/Dishwashing)** | `>= 88.0%` | Autonomous task completion rate across diverse kitchen environments over 30 days. |
| **Grasping Failure Rate (Reflective/Clear)** | `< 4.2%` | Reduction in grasp failures on transparent, specular, or low-texture objects. |
| **Kinematic Singularity MTTR** | `< 15 mins` | Mean time to detect and isolate arm joint singularities and slip errors during rollouts. |

---

## 2. What It Answers & Sub-Agent Routing

### Sub-Agent Architecture
- **`data_insights`**: Queries internal BigQuery tables (`pedi_mefd_*`) using the BigQuery Conversational Analytics API (`ask_data_insights`, `forecast`, `analyze_contribution`, `detect_anomalies`) and generates visual data charts via `render_chart`.
- **`market_context`**: Leverages Google Search grounding for external robotics research (arXiv, CoRL, ICRA), IEEE RAS specifications, ISO 10218 / 15066 safety standards, and hardware datasheets.
- **`root_agent`**: Orchestrates routing between internal fleet telemetry/data lake metrics and external robotics intelligence.

---

## 3. Sample Q&A Showcase

### Example 1: Quantitative Diagnostics (Data Insights)
*Question:* "What is the overall success rate for dishwashing tasks in kitchen environments over the last 30 days?"
*Response:*
> Over the last 30 days across 1,450 physical evaluation rollouts in test kitchen setups, the overall task success rate for **dishwashing and plate loading reached 89.4%**, surpassing the 88.0% baseline threshold (+4.6% vs previous checkpoint).

### Example 2: Quantitative Diagnostics (Data Insights)
*Question:* "What are the top 3 root causes for grasping failures on transparent or reflective objects?"
*Response:*
> Analysis of 184 grasp failures on transparent glassware and polished stainless cutlery reveals: 1) **Depth map specular dropout** (48.4% of failures), 2) **Friction coefficient underestimation on wet glass** (28.3%), and 3) **Finger pad slip during dynamic handover** (15.2%).

### Example 3: Quantitative Diagnostics (Data Insights)
*Question:* "Find and summarize all evaluation runs where the robot arm experienced kinematic singularities or slip errors."
*Response:*
> Identified **14 rollout runs** in the last 14 days with kinematic boundary anomalies: 9 occurred during deep-sink reach maneuvers where Joint 5 reached its +/- 175 deg angular limit, causing trajectory stalling, and 5 involved object micro-slip (> 12mm) during rapid trajectory acceleration.

### Example 4: Industry Grounding (Market Context)
*Question:* "What are current SOTA failure recovery techniques for VLA models on specular objects in CoRL and ICRA literature?"
*Response:*
> Recent CoRL and ICRA 2026 research indicates tactile-visual multimodal fusion (combining high-frequency GelSight tactile sensing with RGB-D) reduces specular grasp failure rates from 18.2% to under 3.5% on transparent glass.

### Example 5: Chart Visualization (`sample_chart.png`)
*Question:* "Render a chart comparing weekly performance metrics for multimodal eval failure diagnostics vs target threshold."
*Generated Visual Artifact:*
![Sample Chart](sample_chart.png)


---

## 4. Authorized BigQuery Tables

- `pedi_mefd_eval_rollout_metrics` — Seeded via `data/eval_rollout_metrics.csv`
- `pedi_mefd_failure_root_causes` — Seeded via `data/failure_root_causes.csv`
- `pedi_mefd_joint_singularity_events` — Seeded via `data/joint_singularity_events.csv`

---

## 5. Example Questions

1. "What is the overall success rate for dishwashing tasks in kitchen environments over the last 30 days?"
2. "What are the top 3 root causes for grasping failures on transparent or reflective objects?"
3. "Find and summarize all evaluation runs where the robot arm experienced kinematic singularities or slip errors."
4. "What are current SOTA failure recovery techniques for VLA models on specular objects in CoRL and ICRA literature?"
5. "Render a chart comparing weekly performance metrics for multimodal eval failure diagnostics vs target threshold."

---

## 6. Tools & Architecture

- **`ask_data_insights`**: BigQuery Conversational Analytics natural language to SQL.
- **`render_chart`**: BigQuery SQL to Matplotlib PNG visual rendering.
- **`google_search`**: Google Search robotics research and industry standards grounding.
- **LLM Inference**: `gemini-3.5-flash` with `GOOGLE_CLOUD_LOCATION=global`.
- **Runtime Engine**: Vertex AI Agent Engine (`us-central1`).

---

## 7. Run Locally

```bash
# Run unit tests
uv run --frozen pytest domains/policy_eval_diagnostics/agents/multimodal_eval_failure_diagnostics/tests/unit -v

# Run interactively with ADK CLI
adk run domains/policy_eval_diagnostics/agents/multimodal_eval_failure_diagnostics
```
