'''
Search tool for accessing information on the internet.
Employs Wikipedia
'''

# Import necessary libraries for Wikipedia search tool
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import Tool

# Initialize the Wikipedia API wrapper
wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

# Create a tool instance for Wikipedia search
wikipedia_tool = Tool(
    name="Wikipedia Tool",
    func=wikipedia.run,
    description=(
        "A useful tool for searching the Internet to find information on "
        "popular people, events, history, issues, biographies, etc. Worth using for "
        "general topics. Use precise questions."
    ),
)


