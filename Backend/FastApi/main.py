from fastapi import FastAPI
import uvicorn
import nest_asyncio
nest_asyncio.apply()
app = FastAPI()


@app.get("/")
#Siempre que llamamos a un servidor debe de ser asincrona
#es decir que tenemos que esperar la sincronia (comunicacion)
#entre el server y la app
async def root():
    return {"message": "Hello, world!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


