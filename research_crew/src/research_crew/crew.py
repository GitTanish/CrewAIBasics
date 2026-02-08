from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


# define the class for our crew
@CrewBase
class ResearchAndBlogCrew():

    agents: list[BaseAgent]
    tasks: list[Task]

    #define the path of config files
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    # ========== Agents ==========
    @agent
    def report_generator(self) -> Agent:
        return Agent(
            config= self.agents_config['report_generator'] # type: ignore[index]

        )
    @agent
    def blog_writer(self) -> Agent:
        return Agent(
            config = self.agents_config['blog_writer'] # type: ignore[index]

        )

    # +++++++++++ Tasks +++++++++++
    # order of task definition matters
    @task
    def report_task(self) -> Task:
        return Task(
            config = self.tasks_config['report_task'],
            output_file='reports/report.md'
        )

    @task
    def blog_writing_task(self) -> Task:
        return Task(
            config = self.tasks_config['blog_task'],
            output_file='blogs/blog.md'
        )

    # ~~~~~~~~~~~~ Crew ~~~~~~~~~~~~
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            verbose = True
        )