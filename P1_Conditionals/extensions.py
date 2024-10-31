def file_extensions(ext):
    match ext:
        case "gif" | "png":
            return f"image/{ext}"
        case "jpeg" | "jpg":
            return f"image/jpeg"
        case "pdf" | "zip":
            return f"application/{ext}"
        case "txt":
            return f"text/plain"
        case _:
            return "application/octet-stream"

ext = input("File Name: ").lower().strip().split(".")[-1]
print(file_extensions(ext))