"""Generate synthetic seed CSV data for fleet_diagnostics_hardware_maintenance."""
import csv
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent

def generate_joint_telemetry_streams():
    headers = ["telemetry_id", "timestamp", "unit_id", "robot_model", "joint_index", "motor_temp_celsius", "harmonic_backlash_arcmin", "anomaly_flag"]
    rows = [["TEL-4001", "2026-08-24 14:10:00", "UNIT-082", "Unitree_R1", 3, 78.4, 2.8, 1], ["TEL-4002", "2026-08-24 14:10:00", "UNIT-082", "Unitree_R1", 4, 62.1, 4.8, 1], ["TEL-4003", "2026-08-24 14:10:00", "UNIT-083", "Unitree_R1", 3, 58.2, 1.9, 0], ["TEL-4004", "2026-08-24 14:15:00", "UNIT-104", "KUKA_LBR_iiwa", 2, 49.5, 1.2, 0], ["TEL-4005", "2026-08-24 14:20:00", "UNIT-082", "Unitree_R1", 3, 79.1, 2.9, 1]]
    with open(DATA_DIR / "joint_telemetry_streams.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

def generate_actuator_maintenance_history():
    headers = ["record_id", "unit_id", "maintenance_date", "actuator_id", "replaced_part", "technician_id", "error_code", "notes"]
    rows = [["MNT-201", "UNIT-082", "2026-06-14", "ACT-J4-88", "Harmonic_Drive_Gearhead", "TECH-512", "ERR_ACTUATOR_OVERCURRENT_401", "Replaced worn gearhead due to tooth micro-pitting"], ["MNT-202", "UNIT-082", "2026-07-22", "SEN-FT-02", "None (Recalibration)", "TECH-309", "ERR_FT_DRIFT_WARNING", "Static gravity tare and zero-point recalibration complete"], ["MNT-203", "UNIT-083", "2026-05-18", "ACT-J1-12", "Encoder_Disk_Assembly", "TECH-512", "ERR_ENCODER_SYNC_LOST", "Replaced optical encoder disk after vibration test"], ["MNT-204", "UNIT-095", "2026-07-30", "ACT-J2-33", "Stator_Winding", "TECH-104", "ERR_MOTOR_TEMP_MAX", "High thermal resistance replaced stator"], ["MNT-205", "UNIT-082", "2026-08-25", "ACT-J3-45", "Pending Inspection", "TECH-309", "ERR_THERMAL_SPIKE_WARN", "Work order WO-2026-981 issued for Joint 3 stator check"]]
    with open(DATA_DIR / "actuator_maintenance_history.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

def generate_force_torque_calibration_logs():
    headers = ["id", "timestamp", "entity_id", "region", "metric_value", "status_flag"]
    rows = [["REC-001", "2026-08-20 10:00:00", "ENT-101", "Lab-North", 125.5, "ACTIVE"], ["REC-002", "2026-08-21 11:30:00", "ENT-102", "Lab-South", 88.2, "COMPLETED"], ["REC-003", "2026-08-22 14:15:00", "ENT-103", "Sim-Cluster", 210.0, "OPTIMAL"], ["REC-004", "2026-08-23 09:45:00", "ENT-104", "Fleet-Bay", 94.75, "ACTIVE"], ["REC-005", "2026-08-24 16:20:00", "ENT-105", "Test-Cell", 165.3, "VERIFIED"]]
    with open(DATA_DIR / "force_torque_calibration_logs.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


def main():
    generate_joint_telemetry_streams()
    generate_actuator_maintenance_history()
    generate_force_torque_calibration_logs()
    print("fleet_diagnostics_hardware_maintenance seed data generated.")

if __name__ == "__main__":
    main()
