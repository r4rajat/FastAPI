from config import app
import constant


@app.get('/hello-world')
async def helloWorld():
    return {constant.MESSAGE: "Hello World!!"}
