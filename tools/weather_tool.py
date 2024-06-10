'''
Weather tool to fetch weather current weather information about given city from openweathermap.org. 
Authentication required.'''

# import necessary libraries
from dotenv import load_dotenv
import os
import requests
from langchain.pydantic_v1 import BaseModel, Field
from langchain_core.tools import StructuredTool

# load environment variable
load_dotenv()

# load API key from environment variables
weather_api_key = os.environ['OPENWEATHER_API_KEY']

# Define the schema for the weather information request
class WeatherInfo(BaseModel):
    city: str = Field(description= 'the city you want to get weather information of. e.g. "London", "Abuja", "Lagos", "Akure"')

# Function to fetch weather information    
def fetch_weather_info(city:str) -> str:
    ''' 
    Fetch weather information of a city provided.
    
    '''
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return response

# Define the weather information tool using StructuredTool
weather_info_tool = StructuredTool.from_function(func=fetch_weather_info,
                                                name= "fetch_weather_info",
                                                description= '''Fetch highly detailed weather information about a city.
                                                In your answer, include information the following details: coordinate (coord), weather, temperature (main), 
                                                humidity (main), windspeed (wind), visibility. 
                                                ''',
                                                args_schema= WeatherInfo)