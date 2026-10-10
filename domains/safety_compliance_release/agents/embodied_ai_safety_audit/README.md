# Safety, Compliance & Policy Release: Embodied Ai Safety Audit

Part of the **Physical AI Enterprise Agents** platform for Gemini Enterprise.

---

## 1. Why This Agent Matters

### Business Problem
Integrates pre-deployment benchmark evaluations, ISO/OSHA robotic safety standards, and out-of-distribution (OOD) stress tests. Automatically generates safety audit summaries and verifies compliance before weights are flashed to edge hardware.

### Target Personas
Robotic Safety Officer, AI Compliance Lead, Embodied AI Release Manager, Edge Deployment Engineer

### Key Metrics Tracked
| Metric | Benchmark / Target | Business Impact |
| :--- | :--- | :--- |
| **Torque & Collision Safety Compliance** | `100% pass rate` | Verification that model checkpoints respect dynamic torque limits and collision stopping distances. |
| **Human-in-the-Loop Safety Benchmark Delta** | `>= 0% regression` | Verification of zero regression in human-proximity safety tests between model releases. |
| **Release Gate Audit Automation** | `< 5 mins` | Instant generation of automated deployment checklists and regulatory audit reports. |

---

## 2. What It Answers & Sub-Agent Routing

### Sub-Agent Architecture
- **`data_insights`**: Queries internal BigQuery tables (`scpr_easa_*`) using the BigQuery Conversational Analytics API (`ask_data_insights`, `forecast`, `analyze_contribution`, `detect_anomalies`) and generates visual data charts via `render_chart`.
- **`market_context`**: Leverages Google Search grounding for external robotics research (arXiv, CoRL, ICRA), IEEE RAS specifications, ISO 10218 / 15066 safety standards, and hardware datasheets.
- **`root_agent`**: Orchestrates routing between internal fleet telemetry/data lake metrics and external robotics intelligence.

---

## 3. Sample Q&A Showcase

### Example 1: Quantitative Diagnostics (Data Insights)
*Question:* "Does model checkpoint 'manipulation-v4.3' pass our maximum torque and dynamic collision safety limits?"
*Response:*
> Yes. Model checkpoint **'manipulation-v4.3' successfully passed all 120 dynamic safety validation runs**. Peak observed torque was **68.2 Nm (safety limit: 80.0 Nm)** and dynamic collision reaction time averaged **18.4 ms (threshold: < 25.0 ms)** under ISO 15066 safety limits.

### Example 2: Quantitative Diagnostics (Data Insights)
*Question:* "Summarize benchmark differences between checkpoint 'v4.2' and 'v4.3' across human-in-the-loop safety tests."
*Response:*
> Benchmark Comparison (`v4.2` vs `v4.3`): Human proximity slowdown distance improved from **0.42m to 0.58m** (+38% safety buffer), unexpected obstacle deceleration rate increased by **24%**, and false-positive collision emergency stops dropped from **4.2% to 0.8%**.

### Example 3: Quantitative Diagnostics (Data Insights)
*Question:* "Generate a deployment readiness report and safety checklist for pushing the new warehouse palletizing policy."
*Response:*
> Generated Deployment Gate Report for `warehouse-palletizing-v4.3`: 1) **ISO 10218-1 Compliance**: PASSED, 2) **OSHA 1910.212 Machine Guarding Delta**: COMPLIANT, 3) **Torque Saturation Envelope**: 100% within safe boundary, 4) **Human-in-the-loop Proximity Deceleration**: VERIFIED. Status: **APPROVED FOR EDGE FLASHING**.

### Example 4: Industry Grounding (Market Context)
*Question:* "What are the ISO 10218-1/2 and ISO/TS 15066 safety requirements for collaborative robot maximum speed and contact force?"
*Response:*
> ISO/TS 15066 specifies power and force limiting (PFL) thresholds, capping transient contact forces on the human chest/arm to 140 N and restricting collaborative workspace tool center point (TCP) transit speed to <= 250 mm/s during proximity detection.

### Example 5: Chart Visualization (`sample_chart.png`)
*Question:* "Render a chart comparing weekly performance metrics for embodied ai safety audit vs target threshold."
*Generated Visual Artifact:*
![Sample Chart](sample_chart.png)


---

## 4. Authorized BigQuery Tables

- `scpr_easa_model_safety_benchmarks` — Seeded via `data/model_safety_benchmarks.csv`
- `scpr_easa_iso_compliance_evals` — Seeded via `data/iso_compliance_evals.csv`
- `scpr_easa_deployment_gate_checklists` — Seeded via `data/deployment_gate_checklists.csv`

---

## 5. Example Questions

1. "Does model checkpoint 'manipulation-v4.3' pass our maximum torque and dynamic collision safety limits?"
2. "Summarize benchmark differences between checkpoint 'v4.2' and 'v4.3' across human-in-the-loop safety tests."
3. "Generate a deployment readiness report and safety checklist for pushing the new warehouse palletizing policy."
4. "What are the ISO 10218-1/2 and ISO/TS 15066 safety requirements for collaborative robot maximum speed and contact force?"
5. "Render a chart comparing weekly performance metrics for embodied ai safety audit vs target threshold."

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
uv run --frozen pytest domains/safety_compliance_release/agents/embodied_ai_safety_audit/tests/unit -v

# Run interactively with ADK CLI
adk run domains/safety_compliance_release/agents/embodied_ai_safety_audit
```
