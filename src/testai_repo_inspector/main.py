#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from testai_repo_inspector.crew import TestaiRepoInspector

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'project_folder': '/Users/eax/worx/spring-petclinic'
    }

    try:
        TestaiRepoInspector().crew().kickoff(inputs=inputs)
    except Exception as e:
        print(f"An error occurred while running the crew: {e}", file=sys.stderr)
        sys.exit(1)


def train():
    """
    Train the crew for a given number of iterations.
    """
    if len(sys.argv) < 3:
        print("Usage: train <n_iterations> <filename>", file=sys.stderr)
        sys.exit(1)

    inputs = {
        'project_folder': '/Users/eax/worx/spring-petclinic'
    }
    try:
        n_iterations = int(sys.argv[1])
        filename = sys.argv[2]
        TestaiRepoInspector().crew().train(n_iterations=n_iterations, filename=filename, inputs=inputs)

    except Exception as e:
        print(f"An error occurred while training the crew: {e}", file=sys.stderr)
        sys.exit(1)


def replay():
    """
    Replay the crew execution from a specific task.
    """
    if len(sys.argv) < 2:
        print("Usage: replay <task_id>", file=sys.stderr)
        sys.exit(1)

    try:
        task_id = sys.argv[1]
        TestaiRepoInspector().crew().replay(task_id=task_id)

    except Exception as e:
        print(f"An error occurred while replaying the crew: {e}", file=sys.stderr)
        sys.exit(1)


def test():
    """
    Test the crew execution and returns the results.
    """
    if len(sys.argv) < 3:
        print("Usage: test <n_iterations> <eval_llm>", file=sys.stderr)
        sys.exit(1)

    inputs = {
        'project_folder': '/Users/eax/worx/spring-petclinic'
    }

    try:
        n_iterations = int(sys.argv[1])
        eval_llm = sys.argv[2]
        TestaiRepoInspector().crew().test(n_iterations=n_iterations, eval_llm=eval_llm, inputs=inputs)

    except Exception as e:
        print(f"An error occurred while testing the crew: {e}", file=sys.stderr)
        sys.exit(1)
