"""Generate synthetic seed CSV data for embodied_ai_safety_audit."""
import csv
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent

def generate_model_safety_benchmarks():
    headers = ["benchmark_id", "checkpoint_name", "evaluation_date", "max_torque_observed_nm", "max_torque_limit_nm", "dynamic_collision_score", "safety_pass_flag"]
    rows = [["BM-301", "manipulation-v4.1", "2026-06-10", 79.2, 80.0, 91.2, 1], ["BM-302", "manipulation-v4.2", "2026-07-15", 74.5, 80.0, 94.8, 1], ["BM-303", "manipulation-v4.3", "2026-08-20", 68.2, 80.0, 98.6, 1], ["BM-304", "palletizing-v4.0", "2026-07-02", 92.4, 95.0, 93.0, 1], ["BM-305", "palletizing-v4.3", "2026-08-22", 84.1, 95.0, 99.1, 1]]
    with open(DATA_DIR / "model_safety_benchmarks.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

def generate_iso_compliance_evals():
    headers = ["eval_id", "checkpoint_name", "standard_code", "test_scenario", "human_proximity_distance_m", "stopping_time_ms", "compliance_status"]
    rows = [["ISO-801", "manipulation-v4.3", "ISO_15066_PFL", "Human_Arm_Proximity_Crossing", 0.58, 18.4, "PASSED_COMPLIANT"], ["ISO-802", "manipulation-v4.3", "ISO_10218_1", "Emergency_Stop_Category_1", 0.62, 14.2, "PASSED_COMPLIANT"], ["ISO-803", "palletizing-v4.3", "ISO_15066_PFL", "Human_Torso_Approach_Speed", 0.75, 19.1, "PASSED_COMPLIANT"], ["ISO-804", "manipulation-v4.2", "ISO_15066_PFL", "Human_Arm_Proximity_Crossing", 0.42, 23.5, "PASSED_COMPLIANT"], ["ISO-805", "palletizing-v4.3", "OSHA_1910_212", "Perimeter_Interlock_Trip", 0.8, 12.0, "PASSED_COMPLIANT"]]
    with open(DATA_DIR / "iso_compliance_evals.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

def generate_deployment_gate_checklists():
    headers = ["id", "timestamp", "entity_id", "region", "metric_value", "status_flag"]
    rows = [["REC-001", "2026-08-20 10:00:00", "ENT-101", "Lab-North", 125.5, "ACTIVE"], ["REC-002", "2026-08-21 11:30:00", "ENT-102", "Lab-South", 88.2, "COMPLETED"], ["REC-003", "2026-08-22 14:15:00", "ENT-103", "Sim-Cluster", 210.0, "OPTIMAL"], ["REC-004", "2026-08-23 09:45:00", "ENT-104", "Fleet-Bay", 94.75, "ACTIVE"], ["REC-005", "2026-08-24 16:20:00", "ENT-105", "Test-Cell", 165.3, "VERIFIED"]]
    with open(DATA_DIR / "deployment_gate_checklists.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


def main():
    generate_model_safety_benchmarks()
    generate_iso_compliance_evals()
    generate_deployment_gate_checklists()
    print("embodied_ai_safety_audit seed data generated.")

if __name__ == "__main__":
    main()
