from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.memory import ConversationBufferMemory

load_dotenv()


llm = ChatGroq(temperature=0)

search = DuckDuckGoSearchRun()

# Define the tool for the agent
tools = [
    Tool(
        name="DuckDuckGo Search",
        func=search.run,
        description="Useful for answering questions about current events or factual information.",
    )
]

# Initialize conversation memory
memory = ConversationBufferMemory(
    memory_key="chat_history", return_messages=True)

# Initialize the agent with tools and memory
agent_chain = initialize_agent(
    tools,
    llm,
    agent="chat-conversational-react-description",
    verbose=True,
    memory=memory,
    handle_parsing_errors=True,
)

if __name__ == "__main__":
    print("Welcome to the LangChain Chatbot! Type 'exit' to quit.\n")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = agent_chain.run(user_input)
        print(f"Bot: {response}\n")
