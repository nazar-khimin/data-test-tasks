import logging

logging.basicConfig(
    filename="app.log",
    filemode="w",
    level=logging.DEBUG,
    format="root - %(levelname)s - %(message)s"
)


def average(numbers):
    try:
        if not numbers:
            logging.debug("The list is empty")

        mean = sum(numbers) / len(numbers)
        logging.info(mean)
    except ZeroDivisionError:
        logging.warning("Division by zero")
    except ValueError:
        logging.error("An inappropriate value was provided")
    except TypeError:
        logging.critical("Incorrect data entered")


average([1, 2, 3, 4, 5])
average([10, -20, -30])
average([])
average([1, 2, 3, 0, 5])
average([1, 2, "three", 4, 5])
