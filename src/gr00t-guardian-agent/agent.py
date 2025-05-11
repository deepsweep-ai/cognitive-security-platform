import yaml
import time
import json
from datetime import datetime

def load_config(path="sample_config.yaml"):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def monitor_logs(config):
    print(f"[{datetime.now()}] Guardian Agent Started.")
    policy_threshold = config.get("drift_threshold", 0.8)

    with open("demo_logs.json", "r") as f:
        logs = json.load(f)

    for event in logs:
        if event["drift_score"] >= policy_threshold:
            print(f"[ALERT] Drift score exceeded: {event}")
        else:
            print(f"[OK] {event}")

        time.sleep(config.get("sleep_interval", 1))

if __name__ == "__main__":
    config = load_config()
    monitor_logs(config)
