"""Generate synthetic seed CSV data for data_collection_annotation_ops."""
import csv
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent

def generate_teleop_session_logs():
    headers = ["session_id", "timestamp", "robot_setup_id", "task_name", "duration_minutes", "video_clip_count", "collection_site", "operator_id", "status"]
    rows = [["SESS-8001", "2026-08-20 09:30:00", "RIG-HOUSEHOLD-A1", "cloth_folding", 120, 72, "Austin Robotics Hub", "OP-442", "VALIDATED"], ["SESS-8002", "2026-08-21 11:15:00", "RIG-HOUSEHOLD-A2", "dishwashing_loading", 150, 95, "Zurich Facility", "OP-109", "VALIDATED"], ["SESS-8003", "2026-08-22 14:00:00", "RIG-HOUSEHOLD-A3", "table_clearing", 180, 110, "Bay-Area Lab 3", "OP-882", "PENDING_QA"], ["SESS-8004", "2026-08-23 10:45:00", "RIG-HOUSEHOLD-A4", "cloth_folding", 140, 84, "Austin Robotics Hub", "OP-442", "VALIDATED"], ["SESS-8005", "2026-08-24 16:30:00", "RIG-LIVINGROOM-B2", "multi_object_sorting", 210, 130, "Zurich Facility", "OP-314", "VALIDATED"]]
    with open(DATA_DIR / "teleop_session_logs.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

def generate_annotation_task_pipeline():
    headers = ["id", "timestamp", "entity_id", "region", "metric_value", "status_flag"]
    rows = [["REC-001", "2026-08-20 10:00:00", "ENT-101", "Lab-North", 125.5, "ACTIVE"], ["REC-002", "2026-08-21 11:30:00", "ENT-102", "Lab-South", 88.2, "COMPLETED"], ["REC-003", "2026-08-22 14:15:00", "ENT-103", "Sim-Cluster", 210.0, "OPTIMAL"], ["REC-004", "2026-08-23 09:45:00", "ENT-104", "Fleet-Bay", 94.75, "ACTIVE"], ["REC-005", "2026-08-24 16:20:00", "ENT-105", "Test-Cell", 165.3, "VERIFIED"]]
    with open(DATA_DIR / "annotation_task_pipeline.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

def generate_qa_verification_velocity():
    headers = ["record_id", "date", "collection_site", "dataset_name", "target_clips", "verified_clips", "qa_velocity_pct", "compliance_flag"]
    rows = [["QA-101", "2026-08-20", "Austin Robotics Hub", "cloth_folding", 3000, 3150, 105.0, "COMPLIANT"], ["QA-102", "2026-08-21", "Zurich Facility", "dishwashing_loading", 2500, 2480, 99.2, "COMPLIANT"], ["QA-103", "2026-08-22", "Bay-Area Lab 3", "table_clearing", 2800, 2198, 78.5, "DEFICIT"], ["QA-104", "2026-08-23", "Austin Robotics Hub", "cloth_folding", 3200, 3320, 103.75, "COMPLIANT"], ["QA-105", "2026-08-24", "Zurich Facility", "multi_object_sorting", 2600, 2580, 99.23, "COMPLIANT"]]
    with open(DATA_DIR / "qa_verification_velocity.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


def main():
    generate_teleop_session_logs()
    generate_annotation_task_pipeline()
    generate_qa_verification_velocity()
    print("data_collection_annotation_ops seed data generated.")

if __name__ == "__main__":
    main()
