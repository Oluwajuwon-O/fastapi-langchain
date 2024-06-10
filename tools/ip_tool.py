'''
IP Address Tool for fetching IP information about IP addresses from ipapi.co
No authentication required
'''


# import libraries
import requests
from langchain.pydantic_v1 import BaseModel, Field
from langchain_core.tools import StructuredTool

# Define the schema for the IP information request
class IPInfo(BaseModel):
    ip_address: str = Field(description = "the ip address we want to fetch the information about e.g. 102.128.192.0, 41.203.78.171")

# Function to fetch IP information from ipapi.co    
def fetch_ip_info(ip_address : str) -> str:
    ''' 
    Fetch information about an ip address provided
    '''
    url = f'https://ipapi.co/{ip_address}/json/'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
      return f"Error: Unable to fetch data for IP {ip_address}"

# Define the IP information tool using StructuredTool
ip_info_tool = StructuredTool.from_function(func= fetch_ip_info, 
                                            name= 'fetch_ip_info',
                                            description= '''
                                            Fetch highly detailed information about a ip address.
                                            
                                            '''
                                            ,
                                            args_schema= IPInfo)