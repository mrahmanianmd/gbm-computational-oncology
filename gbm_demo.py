project = "GBM Computational Oncology"

datasets = [
    "TCGA-GBM",
    "GEO",
    "cBioPortal",
    "Public single-cell RNA-seq datasets"
]

print(project)
print("\nDatasets:")

for dataset in datasets:
    print(f"- {dataset}")

print("\nGoal: identify biologically relevant and experimentally testable GBM findings.")
