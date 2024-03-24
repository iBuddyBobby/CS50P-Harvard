file_types ={
"gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "zip": "application/zip",
    "txt": "text/plain",
    
}

file = input("File name: ")
x = file.strip().lower().split(".")[-1]
print(file_types.get(x, "application/octet-stream"))
