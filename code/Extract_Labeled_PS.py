import pandas as pd

# Path to the large CSV file
file_path = '/3TB/Files/SAGE/All_SAGE_and_Gaia_and_VISTA/SAGE_Final.csv'  # Adjust the path if needed
output_file_labeled = 'Labeled_SAGE_Final.csv'

# Define the chunk size
chunk_size = 100000  # Number of rows per chunk

# Initialize an empty list to hold the filtered chunks
filtered_chunks = []

# Read and filter the CSV file in chunks
for chunk in pd.read_csv(file_path, chunksize=chunk_size):
    # Filter rows where 'Jones_Spec_Label' is not NaN
    filtered_chunk = chunk.dropna(subset=['Jones_Spec_Label'])
    filtered_chunks.append(filtered_chunk)

# Concatenate all filtered chunks into a single DataFrame
result_df = pd.concat(filtered_chunks)

# Save the filtered rows to a new CSV file
result_df.to_csv(output_file_labeled, index=False)

print(f"Filtered rows with 'Jones_Spec_Label' written to {output_file_labeled}.")
