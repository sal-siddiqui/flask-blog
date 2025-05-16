# flask_blog

## 📝 Project Overview

This is my attempt at learning the **Flask Python framework**. I am following the [Python Flask Tutorial](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH) by [Corey Schafer](https://www.youtube.com/@coreyms).

The application is a blog website that offers the following features:

- Visitors can register for an account.
- Registered users can log in using valid credentials.
- Users can view all posts available on the platform.
- Users can create new posts, as well as update or delete posts they have authored.
- Users can update their account details, including their username, email address, and password.
- **Ideally, users would receive a token via email with instructions to reset their password. However, since I could not get the email service working, I instead flash the reset link directly to the user.**

## ▶️ Usage

To run the application, you can either clone the GitHub repository to your local machine or pull the image from Docker. Thereafter, navigate to `localhost:5000/auth/login`.

### GitHub Repository

1.  Clone the repository from GitHub:

    ```bash
    git clone https://github.com/sal-siddiqui/flask-blog.git
    ```

2.  Navigate to the project directory:

    ```bash
    cd flask-blog
    ```

3.  Create a virtual environment and activate it:

    ```bash
    # Create a virtual environment
    python -m venv .venv

    # Activate the virtual environment
    # For PowerShell (Windows):
    .venv\Scripts\Activate.ps1

    # For Linux or macOS:
    source .venv/bin/activate
    ```

4.  Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

5.  Run the application:

    ```bash
    python run.py
    ```

### Docker

1.  Pull the image to your local machine:

    ```bash
    docker image pull salsiddiqui02/flask-blog
    ```

2.  Run the container:

    ```bash
    docker container run --rm -d -p 5000:5000 --name flask_blog salsiddiqui02/flask-blog
    ```


3.  Stop the container:

    ```bash
    docker container stop flask_blog
    ```

4. Remove the image:

    ```bash
    docker image remove salsiddiqui02/flask-blog
    ```

## 🎥 Project Demo

To see the application in action, please click [here](https://youtu.be/z8yGFXgWYDo).
The video provides a guided tour of the project's features and functionality.

## 🧭 Future Work

- **Explore the [Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by [Miguel Grinberg](https://blog.miguelgrinberg.com/)**  
  I would like to learn more about Flask and apply relevant concepts to enhance this project.

- **Take the [Building REST APIs with Flask Course](https://www.udemy.com/course/building-rest-apis-with-flask-and-python/) by [Pratam Sharmaa](https://www.udemy.com/user/pratap-sharma-2/)**  
  I would like to learn how to build RESt APIs with Flask and integrate them with the frontend.
