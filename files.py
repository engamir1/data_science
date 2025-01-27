def read_large_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()  # Yield one line at a time


# Simulate processing a large file
for line in read_large_file("data.txt"):
    print(f"Processing: {line}")
