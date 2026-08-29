"""
data/generate_logs.py

Generates a simulated network/authentication log dataset for Project 6
(Threat Intelligence Dashboard).

Why simulated data?
    Real network logs are hard to obtain, messy, and often contain
    sensitive information. For this project we simulate realistic log
    events so students can focus on parsing, feature engineering, and
    anomaly detection rather than data-cleaning a huge real-world
    dataset (see Project Overview, sections 3.1 and 12).

What this script produces:
    data/network_logs.csv with columns:
        timestamp, source_ip, destination_ip, event_type, action,
        port, status, username

    The dataset mixes:
        - ~90% NORMAL behavior (regular logins, browsing, occasional
          single failed password, normal request pacing).
        - ~10% SUSPICIOUS behavior, generated as short "bursts" per
          attacker IP so downstream feature engineering (failed logins
          in a time window, requests per minute, unique ports) has
          real signal to detect. Patterns included:
            1. Brute-force login attempts (many failed logins, same
               source IP, short time window).
            2. Port scanning (many different destination ports hit
               in quick succession from one source IP).
            3. Unusual off-hours high-frequency activity (many
               requests late at night from one source IP).

Usage:
    python data/generate_logs.py
    (creates/overwrites data/network_logs.csv)

Note: This is intentionally a standalone script with no project
imports, so it can be run before any other backend code exists.
"""

import csv
import random
from datetime import datetime, timedelta

random.seed(42)  # reproducible dataset across runs/students

OUTPUT_PATH = "data/network_logs.csv"

EVENT_TYPES = ["login", "http_request", "file_access", "api_call"]
ACTIONS = {
    "login": ["login_success", "login_failed"],
    "http_request": ["GET", "POST"],
    "file_access": ["read", "write"],
    "api_call": ["GET", "POST", "DELETE"],
}
COMMON_PORTS = [80, 443, 22, 3306, 8080]
USERNAMES = ["alice", "bob", "carla", "diego", "erin", "frank", "guest"]

FIELDNAMES = [
    "timestamp",
    "source_ip",
    "destination_ip",
    "event_type",
    "action",
    "port",
    "status",
    "username",
]


def random_internal_ip():
    """A small pool of 'normal user' IPs, reused across many events
    so feature engineering can compute per-IP behavior over time."""
    return f"10.0.0.{random.randint(2, 40)}"


def random_external_ip():
    """A small pool of 'attacker' IPs used only in suspicious bursts."""
    return f"203.0.113.{random.randint(1, 254)}"


def random_destination_ip():
    return f"192.168.1.{random.randint(1, 20)}"


def make_row(timestamp, source_ip, destination_ip, event_type, action, port, status, username):
    return {
        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "source_ip": source_ip,
        "destination_ip": destination_ip,
        "event_type": event_type,
        "action": action,
        "port": port,
        "status": status,
        "username": username,
    }


def generate_normal_events(n, start_time):
    """
    Generates n normal events spread across a wide time window.
    Occasional single failed logins are included on purpose (real
    users mistype passwords sometimes) so the rule-based baseline and
    the model both have to distinguish "one mistake" from "an attack".
    """
    rows = []
    current_time = start_time
    for _ in range(n):
        # Normal traffic spreads out over time (a few seconds to a
        # few minutes between events).
        current_time += timedelta(seconds=random.randint(5, 300))

        event_type = random.choices(
            EVENT_TYPES, weights=[0.3, 0.4, 0.15, 0.15]
        )[0]
        action = random.choice(ACTIONS[event_type])

        # Normal login failures happen sometimes, but rarely.
        if event_type == "login":
            status = "success" if action == "login_success" else "failed"
            # Real users occasionally fail once, so allow this but
            # keep it infrequent.
            if action == "login_failed" and random.random() > 0.15:
                action = "login_success"
                status = "success"
        else:
            status = "success" if random.random() > 0.05 else "error"

        rows.append(
            make_row(
                timestamp=current_time,
                source_ip=random_internal_ip(),
                destination_ip=random_destination_ip(),
                event_type=event_type,
                action=action,
                port=random.choice(COMMON_PORTS),
                status=status,
                username=random.choice(USERNAMES),
            )
        )
    return rows, current_time


def generate_bruteforce_burst(start_time):
    """
    Simulates a brute-force login attack: one external IP, many
    failed logins against one username, all within a short window.
    """
    attacker_ip = random_external_ip()
    target_ip = random_destination_ip()
    target_user = random.choice(USERNAMES)
    rows = []
    current_time = start_time

    attempt_count = random.randint(15, 40)
    for i in range(attempt_count):
        current_time += timedelta(seconds=random.randint(1, 4))  # rapid attempts
        # Last attempt occasionally succeeds (attacker guesses right)
        is_last = i == attempt_count - 1
        action = "login_success" if (is_last and random.random() > 0.5) else "login_failed"
        status = "success" if action == "login_success" else "failed"

        rows.append(
            make_row(
                timestamp=current_time,
                source_ip=attacker_ip,
                destination_ip=target_ip,
                event_type="login",
                action=action,
                port=22,
                status=status,
                username=target_user,
            )
        )
    return rows, current_time


def generate_port_scan_burst(start_time):
    """
    Simulates port scanning: one external IP hitting many different
    ports on one destination in rapid succession.
    """
    attacker_ip = random_external_ip()
    target_ip = random_destination_ip()
    rows = []
    current_time = start_time

    scan_ports = random.sample(range(1, 65535), k=random.randint(20, 50))
    for port in scan_ports:
        current_time += timedelta(milliseconds=random.randint(50, 500))
        rows.append(
            make_row(
                timestamp=current_time,
                source_ip=attacker_ip,
                destination_ip=target_ip,
                event_type="api_call",
                action="GET",
                port=port,
                status="error",  # most scanned ports refuse/timeout
                username="unknown",
            )
        )
    return rows, current_time


def generate_offhours_flood_burst(start_time):
    """
    Simulates unusual high-frequency activity from one IP late at
    night (e.g. 2-4 AM), which is unusual even if each individual
    request looks technically valid.
    """
    attacker_ip = random_external_ip()
    target_ip = random_destination_ip()
    rows = []

    # Force the burst into off-hours regardless of start_time's clock.
    offhours_time = start_time.replace(hour=random.randint(2, 4), minute=0, second=0)
    current_time = offhours_time

    request_count = random.randint(30, 60)
    for _ in range(request_count):
        current_time += timedelta(seconds=random.uniform(0.5, 3))
        rows.append(
            make_row(
                timestamp=current_time,
                source_ip=attacker_ip,
                destination_ip=target_ip,
                event_type="http_request",
                action=random.choice(["GET", "POST"]),
                port=443,
                status="success",
                username="unknown",
            )
        )
    return rows, current_time


def generate_dataset(total_normal=2500, num_bruteforce=6, num_portscan=5, num_offhours=5):
    """
    Builds the full dataset by interleaving normal traffic with
    suspicious bursts, then sorting everything by timestamp so the
    final CSV reads like a real chronological log file.
    """
    start_time = datetime(2026, 1, 1, 8, 0, 0)
    all_rows = []

    # Split normal traffic into chunks so suspicious bursts can be
    # inserted between them at different points in time.
    num_chunks = num_bruteforce + num_portscan + num_offhours + 1
    normal_per_chunk = total_normal // num_chunks

    current_time = start_time
    normal_rows, current_time = generate_normal_events(normal_per_chunk, current_time)
    all_rows.extend(normal_rows)

    burst_generators = (
        [generate_bruteforce_burst] * num_bruteforce
        + [generate_port_scan_burst] * num_portscan
        + [generate_offhours_flood_burst] * num_offhours
    )
    random.shuffle(burst_generators)

    for burst_fn in burst_generators:
        burst_rows, current_time = burst_fn(current_time)
        all_rows.extend(burst_rows)

        normal_rows, current_time = generate_normal_events(normal_per_chunk, current_time)
        all_rows.extend(normal_rows)

    # Sort chronologically (off-hours bursts jump the clock backwards
    # relative to current_time, so sorting is required for a clean
    # log file).
    all_rows.sort(key=lambda r: r["timestamp"])
    return all_rows


def main():
    rows = generate_dataset()

    with open(OUTPUT_PATH, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Generated {len(rows)} log events -> {OUTPUT_PATH}")
    print("Note: labels are NOT included on purpose — Isolation Forest")
    print("is unsupervised. Use the burst-generation logic above only")
    print("as a reference when manually inspecting/evaluating results.")


if __name__ == "__main__":
    main()
