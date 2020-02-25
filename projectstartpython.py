import logging
import argparse

def main():
    args = parse_args()
    """
    If an error is encountered during configuration, this function will raise a
    ValueError, TypeError, AttributeError or ImportError with a suitably descriptive message.
    """
    logging.basicConfig(format='%(asctime)s - %(name)s : %(levelname)s - %(lineno)d: %(message)s',
                        level=logging.CRITICAL if args.verbose else logging.CRITICAL)
    logging.info()

"""
The argparse module makes it easy to write user-friendly command-line interfaces. 
The program defines what arguments it requires, and argparse will figure out how 
to parse those out of sys.argv. The argparse module also automatically generates 
help and usage messages and issues errors when users give the program invalid arguments.
"""
def parse_args():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-v', '--verbose', help='Verbose logging', action="store_true")
    return parser.parse_args()

if __name__ == '__main__':
    main()
