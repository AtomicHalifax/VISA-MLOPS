import logging
import logger  # This executes logger.py configuration

def calculate_division(a, b):
    logging.info(f"Starting division operation with a={a} and b={b}")
    try:
        result = a / b
        logging.info(f"Division successful: Result = {result}")
        return result
    except Exception as e:
        logging.error(f"Error occurred during division: {str(e)}")
        raise e

if __name__ == "__main__":
    logging.info("Executing demo.py script...")
    calculate_division(10, 2)
    
    try:
        calculate_division(10, 0)
    except Exception:
        logging.warning("Handled division by zero in main execution.")
