from main import creat_app
import os

app = creat_app()

app.app_context().push()

if __name__ == '__main__':
    app.run(debug=True,port=os.getenv("PORT"))