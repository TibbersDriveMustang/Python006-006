import datetime
import pathlib2
import sys


def print_time(stdout='/dev/null'):
    now = datetime.datetime.now()
    print pathlib2.Path(__file__).parent.absolute()

    original_stdout = sys.stdout

    with open(stdout, 'a+') as f:
        sys.stdout = f
        print(now)
        sys.stdout = original_stdout


if __name__ == '__main__':
    print_time(stdout='./test.log')
