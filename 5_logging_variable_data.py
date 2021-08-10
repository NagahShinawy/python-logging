import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(name)s - %(levelname)s - %(message)s",
)

username = "John"
books = ["clean code", "clean arch", "clean design"]


# we can add variable data into our logs using any formatting style, like f-string.
logging.info("{} has books {}".format(username, books))  # it works
logging.info(f"{username} has books {books}")  # it works
