import pandas as pd

# Path to the large CSV file
file_path = '/3TB/Files/SAGE/All_SAGE_and_Gaia_and_VISTA/SAGE_Final.csv'  # Adjust the path if needed
output_file_sample = '1E4_SAGE_Final.csv'

# Define the chunk size
chunk_size = 100000  # Number of rows per chunk

# Initialize an empty list to store row indices
row_indices = []

# First, determine the total number of rows
for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    row_indices.extend(chunk.index.tolist())

# Randomly sample 100,000 row indices
sampled_indices = pd.Series(row_indices).sample(n=10000, random_state=42).tolist()

# Initialize an empty list to store sampled chunks
sampled_chunks = []

# Read the CSV file again, this time collecting the sampled rows
for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    sampled_chunk = chunk.loc[chunk.index.intersection(sampled_indices)]
    sampled_chunks.append(sampled_chunk)

# Concatenate all sampled chunks into a single DataFrame
sampled_df = pd.concat(sampled_chunks)

# Save the sampled rows to a new CSV file
sampled_df.to_csv(output_file_sample, index=False)

print(f"Random sample of 10,000 rows written to {output_file_sample}.")
