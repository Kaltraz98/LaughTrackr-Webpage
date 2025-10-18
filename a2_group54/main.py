# Call to Flask Flask Multi-File Package App
from laughtrackr import create_app
if __name__ == '__main__':
    app = create_app()
    app.run(debug = True)

