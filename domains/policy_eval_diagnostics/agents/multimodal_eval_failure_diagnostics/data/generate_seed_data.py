"""Generate synthetic seed CSV data for multimodal_eval_failure_diagnostics."""
import csv
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent

def generate_eval_rollout_metrics():
    headers = ["eval_id", "timestamp", "task_name", "environment_type", "policy_checkpoint", "success_flag", "execution_time_sec", "singularity_flag"]
    rows = [["EVAL-501", "2026-08-18 10:12:00", "dishwashing_loading", "Kitchen_Island_01", "vla-manip-v4.3", 1, 42.5, 0], ["EVAL-502", "2026-08-19 14:28:00", "dishwashing_loading", "Kitchen_DeepSink_02", "vla-manip-v4.3", 0, 78.2, 1], ["EVAL-503", "2026-08-20 16:45:00", "glass_sorting", "Kitchen_Dining_03", "vla-manip-v4.3", 1, 35.1, 0], ["EVAL-504", "2026-08-21 11:20:00", "pot_scrubbing", "Kitchen_Island_01", "vla-manip-v4.3", 1, 58.0, 0], ["EVAL-505", "2026-08-22 09:05:00", "dishwashing_loading", "Kitchen_DeepSink_02", "vla-manip-v4.3", 0, 64.8, 1]]
    with open(DATA_DIR / "eval_rollout_metrics.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

def generate_failure_root_causes():
    headers = ["failure_id", "eval_id", "task_name", "object_type", "surface_property", "failure_category", "root_cause_summary", "segment_start_sec", "segment_end_sec"]
    rows = [["FAIL-101", "EVAL-502", "dishwashing_loading", "wine_glass", "transparent_specular", "Perception_Depth_Dropout", "Depth sensor ray dropout causing gripper offset", 22.4, 28.1], ["FAIL-102", "EVAL-505", "dishwashing_loading", "stainless_pan", "reflective_smooth", "Grasp_Slip", "Low tactile friction threshold during high acceleration", 31.0, 36.5], ["FAIL-103", "EVAL-502", "dishwashing_loading", "large_tray", "matte_plastic", "Kinematic_Singularity", "Wrist pitch Joint 5 saturated near limit at bottom of sink", 45.2, 52.0], ["FAIL-104", "EVAL-512", "glass_sorting", "crystal_tumbler", "transparent_specular", "Perception_Depth_Dropout", "RGB-D pointcloud noise caused premature finger closure", 18.2, 23.0], ["FAIL-105", "EVAL-519", "cup_stacking", "ceramic_mug", "glazed_porcelain", "Grasp_Slip", "Dynamic torque compensation lag during rotational tilt", 14.8, 19.5]]
    with open(DATA_DIR / "failure_root_causes.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

def generate_joint_singularity_events():
    headers = ["id", "timestamp", "entity_id", "region", "metric_value", "status_flag"]
    rows = [["REC-001", "2026-08-20 10:00:00", "ENT-101", "Lab-North", 125.5, "ACTIVE"], ["REC-002", "2026-08-21 11:30:00", "ENT-102", "Lab-South", 88.2, "COMPLETED"], ["REC-003", "2026-08-22 14:15:00", "ENT-103", "Sim-Cluster", 210.0, "OPTIMAL"], ["REC-004", "2026-08-23 09:45:00", "ENT-104", "Fleet-Bay", 94.75, "ACTIVE"], ["REC-005", "2026-08-24 16:20:00", "ENT-105", "Test-Cell", 165.3, "VERIFIED"]]
    with open(DATA_DIR / "joint_singularity_events.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


def main():
    generate_eval_rollout_metrics()
    generate_failure_root_causes()
    generate_joint_singularity_events()
    print("multimodal_eval_failure_diagnostics seed data generated.")

if __name__ == "__main__":
    main()
