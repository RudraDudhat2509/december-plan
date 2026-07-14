import json


def calculate_average_latency(traces):
    total_latency = 0
    count = 0
    for trace in traces:
        total_latency += extract_latency(trace)
        count += 1
    return total_latency / count


def extract_latency(trace):
    spans = trace["spans"]
    return sum(span["duration_ms"] for span in spans)


with open("trace_data.json") as f:
    traces = json.load(f)

print(calculate_average_latency(traces))
