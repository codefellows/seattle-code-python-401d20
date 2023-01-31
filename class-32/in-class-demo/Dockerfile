### This Dockerfile creates a Docker container based on the official Python 3 image. It sets environment variables to prevent the creation of .pyc files and to run Python in unbuffered mode. It then creates a directory named /code in the Docker container, sets it as the working directory, and copies the requirements.txt file and the application code into the Docker container. Finally, it installs the dependencies listed in requirements.txt using the pip command. In summary, this Dockerfile sets up an isolated environment for the Python application and its dependencies, making it easy to run the application in any environment. ###


# This line specifies the base image for the Docker container. The image used here is python:3, which is the official Python 3 image. The Docker container built using this Dockerfile will have the same environment as the Python 3 image.

    # A base image is the image that is used to create all of your container images. Your base image can be an official Docker image, such as Centos, or you can modify an official Docker image to suit your needs, or you can create your own base image from scratch. Parent topic: Docker.
FROM python:3

# This line sets the environment variable PYTHONDONTWRITEBYTECODE to 1. This environment variable is used to prevent Python from writing .pyc files, which are compiled Python files, to the file system.

    # https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE
    # If this is set to a non-empty string, Python won’t try to write .pyc files on the import of source modules. This is equivalent to specifying the -B option.
ENV PYTHONDONTWRITEBYTECODE 1

# This line sets the environment variable PYTHONUNBUFFERED to 1. This environment variable is used to run Python in unbuffered mode, which means that Python will not buffer the output from the standard output stream. This can be useful for debugging, as it allows you to see the output from the application in real-time.

    # https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUNBUFFERED
    # If this is set to a non-empty string it is equivalent to specifying the -u option.
    # Force the stdout and stderr streams to be unbuffered. This option has no effect on the stdin stream.

    # Allows for log messages to be immediately dumped to the stream instead of being buffered. This is useful for receiving timely log messages and avoiding situations where the application crashes without emitting a relevant message due to the message being "stuck" in a buffer.
ENV PYTHONUNBUFFERED 1

# This line runs the command mkdir /code inside the Docker container. The command creates a directory named /code in the root of the Docker container's file system.
RUN mkdir /code

# This line sets the working directory of the Docker container to /code. This means that any subsequent commands in the Dockerfile will run in the /code directory.
WORKDIR /code

# This line copies the requirements.txt file from the host file system to the /code directory inside the Docker container. The requirements.txt file lists the dependencies required by the application.

    # In a Dockerfile, if a file path starts with a forward slash '/', it is considered an absolute file path, otherwise it is a relative file path.
COPY requirements.txt /code/

# This line runs the command pip install -r requirements.txt inside the Docker container. The command installs the dependencies listed in the requirements.txt file.
RUN pip install -r requirements.txt

# This line copies the entire current directory (represented by .) from the host file system to the /code directory inside the Docker container. This copies the application code and any other files needed by the application into the Docker container.
COPY . /code/
