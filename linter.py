satir = "FROM python:3.13"

if "latest" in satir.lower():
    print("ERROR:version is not stable")
else:
    print("OK:version is stable")