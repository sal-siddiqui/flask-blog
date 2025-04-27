from app import create_app


def main():
    # create the application
    app = create_app()

    # initialize server
    app.run(host="localhost", port=5000, debug=True)


if __name__ == "__main__":
    main()
