from crewai import Agent
from langchain.llms import OpenAI
from langchain_openai import ChatOpenAI


class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    def agent_1_name(self):
        return Agent(
            role="Define agent 1 role here",
            goal="Define agent 1 goal here",
            backstory="Define agent 1 backstory here",
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def agent_2_name(self):
        return Agent(
            role="Define agent 2 role here",
            goal="Define agent 2 goal here",
            backstory="Define agent 2 backstory here",
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
