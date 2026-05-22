import random
import time

# Global tracking state
TOTAL_PROCESSED = 0
TOTAL_ERRORS = 0
LATENCY_HISTORY = []


def run_entire_pipeline(payloads):
    global TOTAL_PROCESSED, TOTAL_ERRORS, LATENCY_HISTORY

    print("--- PIPELINE STARTING ---")

    for item in payloads:
        start_time = time.perf_counter_ns()

        # 1. Validate payload structure inline
        if not isinstance(item, dict) or "text" not in item or "user_id" not in item:
            print(f"[ERROR] Invalid payload format: {item}")
            TOTAL_ERRORS += 1
            continue

        if len(item["text"].strip()) == 0:
            print(f"[ERROR] Empty text from user {item['user_id']}")
            TOTAL_ERRORS += 1
            continue

        # 2. Mock generating text embeddings
        print(f"[INFO] Generating embeddings for user {item['user_id']}...")
        # Simulate slight network jitter
        time.sleep(random.choice([0.01, 0.02, 0.05]))

        # Fake a 3-dimensional embedding vector based on word count
        words = item["text"].split()
        mock_vector = [float(len(words)), float(len(item["text"])), 0.891]

        # 3. Calculate sentiment score from the vectors
        # If the first vector value is high, we consider it positive sentiment
        vector_sum = sum(mock_vector)
        if vector_sum > 15.0:
            sentiment = "Positive"
        else:
            sentiment = "Neutral/Negative"

        print(
            f"[SUCCESS] User {item['user_id']} sentiment: {sentiment} (Vector: {mock_vector})"
        )

        # 4. Update metrics
        TOTAL_PROCESSED += 1
        end_time = time.perf_counter_ns()
        duration_ms = (end_time - start_time) / 1_000_000
        LATENCY_HISTORY.append(duration_ms)

    # 5. Calculate and print summary report
    print("\n--- FINAL METRICS REPORT ---")
    print(f"Total Successful Rows: {TOTAL_PROCESSED}")
    print(f"Total Failed Rows: {TOTAL_ERRORS}")

    if LATENCY_HISTORY:
        sorted_latencies = sorted(LATENCY_HISTORY)
        mid_index = len(sorted_latencies) // 2
        p50_latency = sorted_latencies[mid_index]
        print(f"p50 Pipeline Latency: {p50_latency:.4f} ms")
    else:
        print("p50 Pipeline Latency: 0.0000 ms")

    print("--- PIPELINE FINISHED ---")


# --- SANDBOX TEST DATA ---
if __name__ == "__main__":
    raw_incoming_data = [
        {
            "user_id": "usr_101",
            "text": "This new machine learning framework is absolutely incredible!",
        },
        {"user_id": "usr_102", "text": ""},  # Should error (empty)
        {"invalid_key": "corrupted"},  # Should error (bad schema)
        {"user_id": "usr_103", "text": "Short text."},
        {
            "user_id": "usr_104",
            "text": "Designing machine learning systems requires strict data contracts and latency metrics.",
        },
    ]

    run_entire_pipeline(raw_incoming_data)
