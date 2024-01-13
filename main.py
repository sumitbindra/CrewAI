import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from decouple import config

from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks

# Install duckduckgo-search for this example:
# !pip install -U duckduckgo-search

from langchain.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
os.environ["OPENAI_ORGANIZATION"] = config("OPENAI_ORGANIZATION_ID")


class CustomCrew:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def run(self):
        agents = CustomAgents()
        tasks = CustomTasks()

        custom_agent_1 = agents.agent_1_name()
        custom_agent_2 = agents.agent_2_name()
        custom_agent_3 = agents.agent_3_name()

        custom_task_1 = tasks.task_1_name(
            custom_agent_1,
            self.var1,
            self.var2,
        )

        custom_task_2 = tasks.task_2_name(
            custom_agent_2,
            self.var1,
            self.var2,
        )

        custom_task_3 = tasks.task_3_name(
            custom_agent_3,
            self.var1,
            self.var2,
        )

        crew = Crew(
            agents=[custom_agent_1, custom_agent_2, custom_agent_3],
            tasks=[custom_task_1, custom_task_2, custom_task_3],
            verbose=True,
        )

        result = crew.kickoff()
        return result


if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    var1 = input(dedent("""Enter dollar amount: """))
    var2 = input(dedent("""Enter weeks to raise: """))

    custom_crew = CustomCrew(var1, var2)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
