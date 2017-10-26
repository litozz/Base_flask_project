from app import create_app
 
app = create_app('default')
app.run(host='localhost',port=54321)