import argparse

from prediction.task import Task

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', type=str, required=True)
    parser.add_argument('--config', type=str, required=True)
    arguments = parser.parse_args()
    Task().run(arguments.action, arguments.config)
