base_image="python"
version="3.13"
workdir="/app"

dockerfile=f"FROM {base_image}:{version}\nWORKDIR {workdir}\nCOPY . ."
print(dockerfile)