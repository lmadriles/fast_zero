from fastapi import FastAPI
  
app = FastAPI() # instancia do objeto
  

@app.get('/') # request do método get de HTTP
def root():
    return {'message': 'Hello World'}