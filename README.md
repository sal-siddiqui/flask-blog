# flask-blog

## 📝 Project Overview

This is my attempt at learning the **Flask Python framework**. I am following the [Python Flask Tutorial](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH) by [Corey Schafer](https://www.youtube.com/@coreyms).

The application is a blog website that offers the following features:

- Visitors can register for an account.
- Registered users can log in using valid credentials.
- Users can view all posts available on the platform.
- Users can create new posts, as well as update or delete posts they have authored.
- Users can update their account details, including their username, email address, and password.
- **Ideally, users would receive a token via email with instructions to reset their password. However, since I could not get the email service working, I instead flash the reset link directly to the user.**

I have completed the project. In the future, I would like to explore the Flask [Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by [Miguel Grinberg](https://blog.miguelgrinberg.com/) to further enhance my knowledge. I plan to integrate additional concepts from the tutorial into this project.

## ▶️ Usage

To run the application, you can either clone the GitHub repository to your local machine or pull the image from Docker.

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
    docker container run -d -p 5000:5000 salsiddiqui02/flask-blog
    ```

## 🎥 Project Demo

To see the application in action, please click [here](https://youtu.be/z8yGFXgWYDo).
The video provides a guided tour of the project's features and functionality.
