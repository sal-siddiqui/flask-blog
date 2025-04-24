from app import create_app

# create the application
app = create_app()

# initialize server
if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
