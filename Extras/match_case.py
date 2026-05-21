def process_payload(payload: dict[str, str | list[float]]) -> str:
    match payload:
        case {"status": "error", "message": str(msg)}:
            return f"System failure: {msg}"
        case {"status": "success", "embeddings": [float(), *rest]}:
            return f"Processing array starting with first element, plus {len(rest)} more vectors"
        case _:
            raise ValueError("Data contract broken!")


print(process_payload({"status": "error", "message": "p90 latency exceeded 50ms"}))
print(process_payload({"status": "success", "embeddings": [2.0, 5.0]}))
