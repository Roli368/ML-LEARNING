import kagglehub

# Download latest version
path = kagglehub.dataset_download("sdolezel/black-friday")

print("Path to dataset files:", path)