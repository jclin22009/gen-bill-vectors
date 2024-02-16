import json
from tqdm import tqdm

# Read data from JSON
parsed_data = []
first_50 = []
# Bill fields: 'billId', 'title', 'introducedDate', 'billText', 'crsSummary', 'briefSummary', 'verboseSummary'
with open("data.jsons", "r") as file:
    for line in tqdm(file, desc="Reading bills"):
        json_object = json.loads(line)
        parsed_data.append(json_object)
    health_bills = [
        bill
        for bill in parsed_data
        if "health" in bill["title"].lower() and len(bill["billText"].split()) <= 500
    ]
    first_50 = health_bills[:50]

# Write data to JSON file
with open("output/health_bills.md", "w") as file:
    for bill in first_50:
        bill_info = (
            "## "
            + bill["billId"]
            + "\n_"
            + bill["title"]
            + "_\n"
            + bill["briefSummary"]
            + "\n\n\n"
        )
        file.write(bill_info)
