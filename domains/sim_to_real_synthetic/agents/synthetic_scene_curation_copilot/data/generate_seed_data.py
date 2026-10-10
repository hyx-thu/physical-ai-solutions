"""Generate synthetic seed CSV data for synthetic_scene_curation_copilot."""
import csv
import json
from pathlib import Path

DATA_DIR = Path(__file__).parent

def generate_edge_case_real_trials():
    headers = ["trial_id", "task_name", "scenario_description", "training_data_hours", "failure_rate_pct", "needs_synthetic_augmentation_flag"]
    rows = [["TR-101", "kitchen_low_light", "Night-time kitchen counter manipulation under < 50 lux", 8.4, 28.5, 1], ["TR-102", "cloth_unfolding_wet", "Deformable wet dishcloth unfolding and hanging", 14.2, 22.0, 1], ["TR-103", "glassware_bin_picking", "Transparent stemware in dense jumbled bin", 16.8, 19.4, 1], ["TR-104", "plate_stacking_dry", "Dry standard ceramic plate stacking", 125.0, 3.2, 0], ["TR-105", "utensil_sorting_drawer", "Flatware sorting into compartmentalized drawer", 84.5, 5.1, 0]]
    with open(DATA_DIR / "edge_case_real_trials.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

def generate_sim_asset_library():
    headers = ["asset_id", "asset_name", "geometry_class", "mesh_fidelity", "material_type", "dimensions_cm", "source_format"]
    rows = [["AST-701", "mesh_stemware_tall_v2.usd", "Glassware_Stem", "Ultra_High_100k_Poly", "Refractive_Glass", "8.5x8.5x22.0", "OpenUSD"], ["AST-702", "mesh_carafe_fluted.usd", "Glassware_Carafe", "High_65k_Poly", "Refractive_Glass", "12.0x12.0x28.0", "OpenUSD"], ["AST-703", "mesh_cutlery_mirror_fork.usd", "Flatware_Fork", "High_45k_Poly", "Specular_Chrome", "2.5x1.5x20.0", "OpenUSD"], ["AST-704", "mesh_dishcloth_terry.usd", "Deformable_Fabric", "Cloth_FEM_Mesh", "Woven_Cotton", "30.0x30.0x0.4", "OpenUSD"], ["AST-705", "mesh_skillet_castiron.usd", "Cookware_Pan", "Medium_35k_Poly", "Textured_Iron", "28.0x45.0x6.0", "OpenUSD"]]
    with open(DATA_DIR / "sim_asset_library.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

def generate_domain_randomization_configs():
    headers = ["config_id", "scenario_name", "lighting_lux_min", "lighting_lux_max", "friction_coeff_min", "friction_coeff_max", "clutter_density_level", "target_sim_engine"]
    rows = [["CFG-201", "low_light_kitchen_v1", 12.0, 45.0, 0.32, 0.78, "HIGH", "IsaacLab_Omniverse"], ["CFG-202", "wet_cloth_friction_v2", 150.0, 400.0, 0.15, 0.45, "MEDIUM", "IsaacLab_Omniverse"], ["CFG-203", "glassware_specular_v1", 200.0, 800.0, 0.25, 0.6, "VERY_HIGH", "IsaacLab_Omniverse"], ["CFG-204", "general_tabletop_random", 100.0, 600.0, 0.3, 0.8, "LOW", "PyBullet_GPU"], ["CFG-205", "night_ambient_shadow_v3", 5.0, 25.0, 0.35, 0.75, "MEDIUM", "IsaacLab_Omniverse"]]
    with open(DATA_DIR / "domain_randomization_configs.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


def main():
    generate_edge_case_real_trials()
    generate_sim_asset_library()
    generate_domain_randomization_configs()
    print("synthetic_scene_curation_copilot seed data generated.")

if __name__ == "__main__":
    main()
