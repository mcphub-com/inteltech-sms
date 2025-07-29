import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/inteltech/api/inteltech-sms'

mcp = FastMCP('inteltech-sms')

@mcp.tool()
def check_credit(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Returns Prepaid Account Balance'''
    url = 'https://inteltech.p.rapidapi.com/credit.php'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'inteltech.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def send_sms(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Send an SMS with the Inteltech API'''
    url = 'https://inteltech.p.rapidapi.com/send.php'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'inteltech.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
