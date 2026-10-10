# Fleet Telemetry & Predictive Maintenance: Fleet Diagnostics Hardware Maintenance

Part of the **Physical AI Enterprise Agents** platform for Gemini Enterprise.

---

## 1. Why This Agent Matters

### Business Problem
Grounds Gemini Enterprise on high-frequency joint telemetry, error logs, and hardware repair SOPs. Enables field technicians and hardware engineers to troubleshoot anomalies, anticipate component fatigue, and obtain step-by-step repair guidance.

### Target Personas
Robotics Hardware Engineer, Field Maintenance Technician, Fleet Reliability Manager, Actuator Systems Specialist

### Key Metrics Tracked
| Metric | Benchmark / Target | Business Impact |
| :--- | :--- | :--- |
| **Thermal & Backlash Anomaly Detection** | `> 99.0% recall` | Real-time flagging of motor temperature spikes and harmonic drive backlash within 48 hours. |
| **Sensor Recalibration Efficiency** | `< 20 mins` | Reduction in field calibration time for 6-axis wrist force-torque sensors. |
| **Fleet Hardware Availability** | `>= 98.5% uptime` | Overall operational availability across active robot fleet units. |

---

## 2. What It Answers & Sub-Agent Routing

### Sub-Agent Architecture
- **`data_insights`**: Queries internal BigQuery tables (`ftpm_fdhm_*`) using the BigQuery Conversational Analytics API (`ask_data_insights`, `forecast`, `analyze_contribution`, `detect_anomalies`) and generates visual data charts via `render_chart`.
- **`market_context`**: Leverages Google Search grounding for external robotics research (arXiv, CoRL, ICRA), IEEE RAS specifications, ISO 10218 / 15066 safety standards, and hardware datasheets.
- **`root_agent`**: Orchestrates routing between internal fleet telemetry/data lake metrics and external robotics intelligence.

---

## 3. Sample Q&A Showcase

### Example 1: Quantitative Diagnostics (Data Insights)
*Question:* "Are any robot units showing abnormal motor temperature spikes or joint backlash over the last 48 hours?"
*Response:*
> Fleet telemetry flags **Unit #082 (Unitree R1)** exhibiting **Joint 3 motor temperature spikes to 78.4 deg C** (warning threshold: 72.0 deg C) and **Joint 4 harmonic backlash of 4.8 arcmin** (tolerance: < 3.0 arcmin). Preventive maintenance dispatch is recommended.

### Example 2: Quantitative Diagnostics (Data Insights)
*Question:* "What is the step-by-step recalibration procedure for the wrist force-torque sensor on Robot Model X?"
*Response:*
> Procedure for 6-Axis F/T Sensor Model X: 1) Command arm to zero-gravity tare pose `(J1=0, J2=-45, J3=90, J4=0, J5=45, J6=0)`, 2) Execute static gravity compensation tare via `/dev/ft_sensor0:tare`, 3) Apply 10N calibration reference weight in +/- Z axis, 4) Verify drift tolerance < 0.05N across 60 seconds.

### Example 3: Quantitative Diagnostics (Data Insights)
*Question:* "Summarize the maintenance history, error codes, and replaced actuators for Unit #082."
*Response:*
> Unit #082 Maintenance Profile: Total runtime: 1,842 hours. Replaced parts: Joint 4 harmonic drive actuator (replaced on 2026-06-14, error `ERR_ACTUATOR_OVERCURRENT_401`), F/T sensor recalibrated (2026-07-22). Current pending work order: `WO-2026-981` for Joint 3 stator thermal sensor inspection.

### Example 4: Industry Grounding (Market Context)
*Question:* "What are the manufacturer motor temperature limits and harmonic drive maintenance cycles for Unitree and KUKA robotics actuators?"
*Response:*
> Unitree and harmonic drive OEM specifications rate continuous brushless motor operation up to 75.0 deg C (thermal trip at 85.0 deg C) and mandate harmonic drive grease re-lubrication every 2,500 operating hours to prevent backlash degradation.

### Example 5: Chart Visualization (`sample_chart.png`)
*Question:* "Render a chart comparing weekly performance metrics for fleet diagnostics hardware maintenance vs target threshold."
*Generated Visual Artifact:*
![Sample Chart](sample_chart.png)


---

## 4. Authorized BigQuery Tables

- `ftpm_fdhm_joint_telemetry_streams` — Seeded via `data/joint_telemetry_streams.csv`
- `ftpm_fdhm_actuator_maintenance_history` — Seeded via `data/actuator_maintenance_history.csv`
- `ftpm_fdhm_force_torque_calibration_logs` — Seeded via `data/force_torque_calibration_logs.csv`

---

## 5. Example Questions

1. "Are any robot units showing abnormal motor temperature spikes or joint backlash over the last 48 hours?"
2. "What is the step-by-step recalibration procedure for the wrist force-torque sensor on Robot Model X?"
3. "Summarize the maintenance history, error codes, and replaced actuators for Unit #082."
4. "What are the manufacturer motor temperature limits and harmonic drive maintenance cycles for Unitree and KUKA robotics actuators?"
5. "Render a chart comparing weekly performance metrics for fleet diagnostics hardware maintenance vs target threshold."

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
uv run --frozen pytest domains/fleet_telemetry_maintenance/agents/fleet_diagnostics_hardware_maintenance/tests/unit -v

# Run interactively with ADK CLI
adk run domains/fleet_telemetry_maintenance/agents/fleet_diagnostics_hardware_maintenance
```
