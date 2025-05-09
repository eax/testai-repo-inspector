from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class TestaiRepoInspector():
    """TestaiRepoInspector crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools

    @agent
    def tester(self) -> Agent:
        return Agent(
            config=self.agents_config['tester'], # type: ignore[index]
            verbose=True
        )

    @agent
    def verifier(self) -> Agent:
        return Agent(
            config=self.agents_config['verifier'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task

    @task
    def api_testing_task(self) -> Task:
        return Task(
            config=self.tasks_config['api_testing_task'], # type: ignore[index]
        )

    @task
    def code_verification_task(self) -> Task:
        return Task(
            config=self.tasks_config['code_verification_task'], # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the TestaiRepoInspector crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            inputs={
                'project_folder': '/Users/eax/worx/spring-petclinic'
            }
        )
