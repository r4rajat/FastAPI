from config import app
import constant


@app.get('/hello-world')
def helloWorld():
    return {constant.MESSAGE: "Hello World!!"}
