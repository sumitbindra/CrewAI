from crewai import Task
from textwrap import dedent


class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def task_1_name(self, agent, var1, var2):
        return Task(
            description=dedent(
                f"""
            For this task you are to come up with innovative ideas for a fundraising task for a in person toastmasters conference.
            
            {self.__tip_section()}
    
            Make sure to use the most recent data as possible.
    
            How much do you have to raise: {var1}
            How much time do you have: {var2}
        """
            ),
            agent=agent,
        )

    def task_2_name(self, agent, var1, var2):
        return Task(
            description=dedent(
                f"""
            For this task you take the list from the previous task and prune it down to a list of top 3 strategies that are most likely to 
            work. You must also provide a rationale for why you chose the top 3 strategies.
                                       
            {self.__tip_section()}

            The final output must be the top three strategies that will accomplish the goal to raise {var1} dollars in {var2} weeks.
        """
            ),
            agent=agent,
        )

    def task_3_name(self, agent, var1, var2):
        return Task(
            description=dedent(
                f"""
            For this task you take the input from the previous task and convert it to a plan that can be executed by a team of three 
            on the ground.
                                       
            {self.__tip_section()}

            The final output must be a comprehensive plan to accomplish the goal to raise {var1} dollars in {var2} weeks.
        """
            ),
            agent=agent,
        )
