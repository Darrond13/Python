#Implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
#.gif, .jpg, .jpeg, .png, .pdf, .txt, .zip
#Otherwise output application/octet-stream  
def main():
    user = input("File name: ").strip().lower()
    splice = "." + user.split(".")[1]

    media_types = {
        ".gif" : "image/gif",
        ".jpg" : "image/jpeg",
        ".jpeg" : "image/jpeg",
        ".png" : "image/png",
        ".pdf" : "application/pdf",
        ".txt" : "text/plain",
        ".zip" : "application/zip",
    }
    if splice in media_types:
        print(media_types[splice])
    else:
        print("application/octet-stream")
main()
