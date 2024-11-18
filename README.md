# LangChain Agent with GPT-3.5-turbo
This project implements a LangChain-powered agent using Python and GPT-3.5-turbo for natural language processing. The agent interacts with multiple tools, including SQL databases, weather data APIs, and Wikipedia, providing versatile and intelligent responses via a FastAPI HTTP interface.

Features
* Natural Language Query Handling: Processes queries using GPT-3.5-turbo for accurate and meaningful responses.
* Tool Integration: Supports operations with SQL databases, weather data APIs, and Wikipedia.
* FastAPI Endpoint: Exposes the agent for external interaction through an HTTP endpoint.
* Scalability: Deployed on Render.com

📂 fastapi-langchain  
├── main.py              # FastAPI application and agent set up 
├── 📂tools             # Definitions for tool integration    
    ├── ip_tool.py      # ip address tool
    ├── search_tool.py  # for fetching wikipedia information
    ├── sql_tool.py      # query database
    ├── weather_tool.py   # to fetch weather information
├── northwind.db       # database 
├── requirements.txt       # Dependencies  
├── README.md              # Project documentation  
└── .env                   # Environment variables (excluded from version control)  
