dockerfile_lines = [
       "FROM python:latest",
       "WORKDIR /app",
       "COPY . .",
       "FROM node:LATEST",
   ]
for i ,line in enumerate(dockerfile_lines, start=1):
    if "latest" in line.lower():
        print(f"ERROR (line {i}): {line} — :latest used")

