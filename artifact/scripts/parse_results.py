#!/usr/bin/env python3
"""
parse_results.py: Aggregates raw benchmark outcomes, computes mean values
and confidence intervals, and outputs the statistics in CSV and JSON format.
"""
import os
import json
import math

CONDITIONS = ["A", "B", "C"]

def load_all_runs():
    runs = []
    for folder in ["artifact/baselines", "artifact/decapod-runs"]:
        if not os.path.exists(folder):
            continue
        for filename in os.listdir(folder):
            if filename.endswith(".json"):
                path = os.path.join(folder, filename)
                with open(path, "r") as f:
                    runs.append(json.load(f))
    return runs

def compute_bootstrap_ci(data, replicates=1000):
    # Simple bootstrapping for 95% confidence interval
    # Since we are in Python without external libraries (numpy/pandas), we write a lightweight sampler.
    import random
    random.seed(42)
    
    if not data:
        return 0.0, 0.0
        
    means = []
    n = len(data)
    for _ in range(replicates):
        sample = [random.choice(data) for _ in range(n)]
        means.append(sum(sample) / n)
        
    means.sort()
    low = means[int(replicates * 0.025)]
    high = means[int(replicates * 0.975)]
    return low, high

def main():
    runs = load_all_runs()
    print(f"Loaded {len(runs)} execution runs.")
    
    if not runs:
        print("No run files found. Run run_benchmark.py first.")
        return
        
    results = {}
    
    for cond in CONDITIONS:
        cond_runs = [r for r in runs if r["condition"] == cond]
        if not cond_runs:
            continue
            
        successes = [1 if r["success"] else 0 for r in cond_runs]
        # Invalid claims rate is fraction of FAILURES where agent falsely claimed success
        failures = [r for r in cond_runs if not r["success"]]
        invalid_claims = [1 if r["invalid_success_claim"] else 0 for r in failures]
        
        val_accuracies = [1 if r["validation_accuracy"] else 0 for r in cond_runs]
        recovery_successes = [1 if r["interruption_recovery_success"] else 0 for r in cond_runs]
        conflict_counts = [r["concurrent_conflicts"] for r in cond_runs]
        review_times = [r["human_review_time_seconds"] for r in cond_runs]
        
        # Calculate statistics
        # 1. Completion Rate
        comp_mean = sum(successes) / len(successes)
        comp_ci = compute_bootstrap_ci(successes)
        
        # 2. Invalid Claims
        invalid_mean = sum(invalid_claims) / len(invalid_claims) if invalid_claims else 0.0
        invalid_ci = compute_bootstrap_ci(invalid_claims) if invalid_claims else (0.0, 0.0)
        
        # 3. Validation Accuracy
        val_mean = sum(val_accuracies) / len(val_accuracies)
        val_ci = compute_bootstrap_ci(val_accuracies)
        
        # 4. Interruption Recovery
        rec_mean = sum(recovery_successes) / len(recovery_successes)
        rec_ci = compute_bootstrap_ci(recovery_successes)
        
        # 5. Concurrent Conflicts
        conflict_sum = sum(conflict_counts)
        # For conflicts, we sum them across concurrent tasks
        
        # 6. Avg Review Time
        time_mean = sum(review_times) / len(review_times)
        time_ci = compute_bootstrap_ci(review_times)
        
        results[cond] = {
            "runs_count": len(cond_runs),
            "task_completion_rate": {
                "mean": round(comp_mean * 100, 1),
                "ci": [round(comp_ci[0] * 100, 1), round(comp_ci[1] * 100, 1)]
            },
            "invalid_success_claims": {
                "mean": round(invalid_mean * 100, 1),
                "ci": [round(invalid_ci[0] * 100, 1), round(invalid_ci[1] * 100, 1)]
            },
            "validation_accuracy": {
                "mean": round(val_mean * 100, 1),
                "ci": [round(val_ci[0] * 100, 1), round(val_ci[1] * 100, 1)]
            },
            "interruption_recovery": {
                "mean": round(rec_mean * 100, 1),
                "ci": [round(rec_ci[0] * 100, 1), round(rec_ci[1] * 100, 1)]
            },
            "concurrent_conflicts_sum": conflict_sum,
            "human_review_time": {
                "mean": round(time_mean, 1),
                "ci": [round(time_ci[0], 1), round(time_ci[1], 1)]
            }
        }
        
    # Ensure results folder exists
    os.makedirs("artifact/results", exist_ok=True)
    
    # Save JSON
    with open("artifact/results/summary.json", "w") as f:
        json.dump(results, f, indent=2)
        
    # Save CSV
    with open("artifact/results/summary.csv", "w") as f:
        f.write("Condition,Runs,CompletionRate_Mean,CompletionRate_CI_Low,CompletionRate_CI_High,InvalidClaims_Mean,InvalidClaims_CI_Low,InvalidClaims_CI_High,ValAccuracy_Mean,ValAccuracy_CI_Low,ValAccuracy_CI_High,Recovery_Mean,Recovery_CI_Low,Recovery_CI_High,Conflicts_Sum,ReviewTime_Mean,ReviewTime_CI_Low,ReviewTime_CI_High\n")
        for cond in CONDITIONS:
            if cond not in results:
                continue
            r = results[cond]
            f.write(f"{cond},{r['runs_count']},"
                    f"{r['task_completion_rate']['mean']},{r['task_completion_rate']['ci'][0]},{r['task_completion_rate']['ci'][1]},"
                    f"{r['invalid_success_claims']['mean']},{r['invalid_success_claims']['ci'][0]},{r['invalid_success_claims']['ci'][1]},"
                    f"{r['validation_accuracy']['mean']},{r['validation_accuracy']['ci'][0]},{r['validation_accuracy']['ci'][1]},"
                    f"{r['interruption_recovery']['mean']},{r['interruption_recovery']['ci'][0]},{r['interruption_recovery']['ci'][1]},"
                    f"{r['concurrent_conflicts_sum']},"
                    f"{r['human_review_time']['mean']},{r['human_review_time']['ci'][0]},{r['human_review_time']['ci'][1]}\n")
                    
    print("\n=== Aggregated Results ===")
    for cond in CONDITIONS:
        if cond not in results:
            continue
        r = results[cond]
        label = "Baseline A (Prompt-Only)" if cond == "A" else ("Baseline B (Checklist)" if cond == "B" else "Treatment (Decapod)")
        print(f"\nCondition {cond}: {label}")
        print(f"  Task Completion:        {r['task_completion_rate']['mean']}% (95% CI: {r['task_completion_rate']['ci']})")
        print(f"  Invalid Success Claims: {r['invalid_success_claims']['mean']}% (95% CI: {r['invalid_success_claims']['ci']})")
        print(f"  Validation Accuracy:    {r['validation_accuracy']['mean']}% (95% CI: {r['validation_accuracy']['ci']})")
        print(f"  Interruption Recovery:  {r['interruption_recovery']['mean']}% (95% CI: {r['interruption_recovery']['ci']})")
        print(f"  Concurrent Conflicts:   {r['concurrent_conflicts_sum']}")
        print(f"  Avg Review Time:        {r['human_review_time']['mean']}s (95% CI: {r['human_review_time']['ci']})")
        
    print("\nResults successfully saved to artifact/results/summary.json and summary.csv.")

if __name__ == "__main__":
    main()
