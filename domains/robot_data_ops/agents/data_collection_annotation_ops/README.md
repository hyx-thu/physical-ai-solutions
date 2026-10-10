# Robot Data Operations & Teleoperation: Data Collection Annotation Ops

Part of the **Physical AI Enterprise Agents** platform for Gemini Enterprise.

---

## 1. Why This Agent Matters

### Business Problem
Connects Gemini Enterprise to robot data lakes (Cloud Storage, BigQuery) and labeling pipeline trackers. Enables operations leads and data engineers to monitor collection volume, teleoperation hours, annotation stages, and QA verification velocity via natural language.

### Target Personas
Teleoperation Operations Lead, Robot Data Engineer, Annotation QA Manager, Fleet Data Architect

### Key Metrics Tracked
| Metric | Benchmark / Target | Business Impact |
| :--- | :--- | :--- |
| **Teleoperation Collection Hours** | `>= 450 hrs/wk` | Total validated teleoperation demonstration hours captured across robot rigs. |
| **Annotation QA Verification Rate** | `>= 96.5%` | Percentage of multi-modal trajectory clips verified and labeled against monthly targets. |
| **Collection Site Quota Adherence** | `>= 94.0%` | Regional teleoperation sites meeting multi-object manipulation quotas. |

---

## 2. What It Answers & Sub-Agent Routing

### Sub-Agent Architecture
- **`data_insights`**: Queries internal BigQuery tables (`rdop_dcao_*`) using the BigQuery Conversational Analytics API (`ask_data_insights`, `forecast`, `analyze_contribution`, `detect_anomalies`) and generates visual data charts via `render_chart`.
- **`market_context`**: Leverages Google Search grounding for external robotics research (arXiv, CoRL, ICRA), IEEE RAS specifications, ISO 10218 / 15066 safety standards, and hardware datasheets.
- **`root_agent`**: Orchestrates routing between internal fleet telemetry/data lake metrics and external robotics intelligence.

---

## 3. Sample Q&A Showcase

### Example 1: Quantitative Diagnostics (Data Insights)
*Question:* "How many total hours and video clips were collected this week across all household robot setups?"
*Response:*
> Across all household robot setups (Kitchen Rigs A1-A4 and Living Room Cell B2), a total of **482.5 teleoperation hours** and **14,280 validated video clips** were ingested into Cloud Storage and BigQuery this week. Collection volume is currently pacing **+7.2% ahead of weekly target**.

### Example 2: Quantitative Diagnostics (Data Insights)
*Question:* "What percentage of the 'cloth folding' dataset has been QA-verified versus our monthly target?"
*Response:*
> The 'cloth folding' manipulation dataset currently stands at **92.4% QA-verified** (18,480 of 20,000 required trajectory clips), against our monthly milestone target of 90.0%. Stage-3 keypoint annotation throughput is averaging 1,240 frames/hour.

### Example 3: Quantitative Diagnostics (Data Insights)
*Question:* "Which collection sites are falling behind on multi-object manipulation quotas?"
*Response:*
> Collection Site **Bay-Area Lab 3** is currently at **78.5% quota adherence** for multi-object table clearing tasks due to camera recalibration downtime, whereas **Austin Robotics Hub** and **Zurich Facility** are operating at 98.2% and 95.6% respectively.

### Example 4: Industry Grounding (Market Context)
*Question:* "What are the latest Open X-Embodiment and robotics data collection benchmarks for imitation learning?"
*Response:*
> According to IEEE RAS and Open X-Embodiment 2026 dataset standards, dual-arm teleoperation pipelines require a minimum of 50 demonstrations per object geometry to achieve >= 90% zero-shot generalization in policy fine-tuning.

### Example 5: Chart Visualization (`sample_chart.png`)
*Question:* "Render a chart comparing weekly performance metrics for data collection annotation ops vs target threshold."
*Generated Visual Artifact:*
![Sample Chart](sample_chart.png)


---

## 4. Authorized BigQuery Tables

- `rdop_dcao_teleop_session_logs` — Seeded via `data/teleop_session_logs.csv`
- `rdop_dcao_annotation_task_pipeline` — Seeded via `data/annotation_task_pipeline.csv`
- `rdop_dcao_qa_verification_velocity` — Seeded via `data/qa_verification_velocity.csv`

---

## 5. Example Questions

1. "How many total hours and video clips were collected this week across all household robot setups?"
2. "What percentage of the 'cloth folding' dataset has been QA-verified versus our monthly target?"
3. "Which collection sites are falling behind on multi-object manipulation quotas?"
4. "What are the latest Open X-Embodiment and robotics data collection benchmarks for imitation learning?"
5. "Render a chart comparing weekly performance metrics for data collection annotation ops vs target threshold."

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
uv run --frozen pytest domains/robot_data_ops/agents/data_collection_annotation_ops/tests/unit -v

# Run interactively with ADK CLI
adk run domains/robot_data_ops/agents/data_collection_annotation_ops
```
