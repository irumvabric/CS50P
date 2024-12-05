fileName = input("File name: ").strip().lower()

extentions = fileName

if fileName.endswith(".gif"):
    print("image/gif")
elif fileName.endswith(".jpg") or fileName.endswith(".jpeg"):
    print("image/jpeg")
elif fileName.endswith(".png"):
    print("image/png")
elif fileName.endswith(".pdf"):
    print("application/pdf")
elif fileName.endswith(".zip"):
    print("application/zip")
elif fileName.endswith(".txt"):
    print("application/txt")
else:
    print("application/octet-stream")


