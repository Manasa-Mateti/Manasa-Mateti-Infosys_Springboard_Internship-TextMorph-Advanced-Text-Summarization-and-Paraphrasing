import nbformat

# Load the notebook
with open('MileStone1.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# Remove widget state metadata if present
if 'widgets' in nb['metadata']:
    del nb['metadata']['widgets']

# Check if any cell metadata contains widget information and remove
for cell in nb['cells']:
    if 'metadata' in cell and 'widgets' in cell['metadata']:
        del cell['metadata']['widgets']

# Save the cleaned notebook
cleaned_notebook_path = 'MileStone1.ipynb'
with open(cleaned_notebook_path, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

cleaned_notebook_path
