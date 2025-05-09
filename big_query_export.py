from google.cloud import bigquery
import pandas as pd

# Path to your service account JSON
SERVICE_ACCOUNT_FILE = '/Users/johnhousley/Downloads/kuiu-klaviyodata-to-lawyer-1651249f5a7f.json'

# Initialize BigQuery client
client = bigquery.Client.from_service_account_json(SERVICE_ACCOUNT_FILE)

# Your full table ID or query
project = "kuiu-klaviyodata-to-lawyer"
dataset = "KUIU_klaviyoData_to_Lawyer"
table = "alternate_generic_klaviyo_input_RESERVOIR_copy"

# Option A: export full table
table_id = f"{project}.{dataset}.{table}"
query = f"SELECT * FROM `{table_id}`"

# Option B: custom query (optional override)
# query = """
#     SELECT name, age FROM `your-project-id.dataset.table`
#     WHERE age > 30
# """

# Run the query
print("Running query...")
df = client.query(query).to_dataframe()

# Save to CSV
output_file = "bigquery_export.csv"
df.to_csv(output_file, index=False)
print(f"Data saved to {output_file}")
