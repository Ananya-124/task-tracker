from fastapi import FastApi
app = FastApi()

@app.get("/")
def home():
  # print("Hello devloper")
  return {"message":"Hello"}
