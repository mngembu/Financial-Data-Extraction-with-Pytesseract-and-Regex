from fastapi import FastAPI, Form, UploadFile, File
import uvicorn
from extractor import extract_fs


app = FastAPI()


@app.post("/extract_from_doc")
def extract_from_doc(file: UploadFile = File(...)):       #the data type for the file_path or file is UploadFile and its default value is File()

    contents = file.file.read()                        #read the content of the file

    file_path = "../uploads/test.pdf"
    with open(file_path, "wb") as f:               #write that content into an actual physical file, test.pdf
        f.write(contents)

    data = extract_fs(file_path)
    return data


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

