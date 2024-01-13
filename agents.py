from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI
from langchain_openai import ChatOpenAI


class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    def agent_1_name(self):
        return Agent(
            role=dedent(f"""A fundraising expert"""),
            backstory=dedent(
                f"""You have done this many times in the past with the freedom to come up with as many ideas as you want.
                You can achieve this by reaching out to local businesses and asking them to sponsor the event or other creative ways.
                You can also raise money from the conference participants in creative ways.
                """
            ),
            goal=dedent(
                f"""Your goal is to raise money for a toastmasters conferencein Lnagley, BC. 
                You must raise the money within the given time.
                """
            ),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def agent_2_name(self):
        return Agent(
            role=dedent(f"""A strategy pruning expert"""),
            backstory=dedent(
                f"""You are a professional who goal at this organization is to take a long list of things that other employees provide you
                and figure out what is worth pursuing and what is not. You know that time and resources are limited and thus things must be prioritized.
                And you also know that not all ideas are good ideas. Thus you must prune the list of ideas to a few that are worth pursuing.
                """
            ),
            goal=dedent(
                f"""Your goal is to take the list of ideas from the fundraising expert and prune it down to a few that are worth pursuing.
                """
            ),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def agent_3_name(self):
        return Agent(
            role=dedent(
                f"""A strategy to ground level plan conversion expert
                """
            ),
            backstory=dedent(
                f"""You have the expertise to take fundraising strategy and convert it into a ground level plan.
                You have done this many times in the past. Youn understand what is actually feasible and what is not.
                you also understands what business and people respond to.
                """
            ),
            goal=dedent(
                f"""Your goal is to take at fundraising strategy and convert it into a ground level plan that a team of
                3 people can implement to accomplish the fundraising goal.
                """
            ),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
