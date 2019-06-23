import argparse
import json

from prediction.task import Task

if __name__ == '__main__':
    # Define and parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', type=str, required=True)
    parser.add_argument('--config', type=str, required=True)
    arguments = parser.parse_args()
    # Read the configuration file and run a task
    with open(arguments.config) as file:
        Task().run(arguments.action, json.load(file))
