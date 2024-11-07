import agent
import streamlit as st

st.title("LangChain Chatbot")

# Initialize session state for chat history and input tracking
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

if "last_input" not in st.session_state:
    st.session_state["last_input"] = None

# Create a form to handle user input and submission
with st.form(key="input_form"):
    user_input = st.text_input("You:", key="user_input")
    submit_button = st.form_submit_button(label="Send")

# Process input only if the form is submitted
if submit_button and user_input and user_input != st.session_state["last_input"]:

    try:
        response = agent.agent_chain.run(user_input)
    except Exception as e:
        st.error("The service is currently unavailable. Please try again later.")
        print(f"Error details: {e}")

    st.session_state.chat_history.append((user_input, response))

    st.session_state["last_input"] = user_input

# Display chat history
if st.session_state["chat_history"]:
    for user_msg, bot_msg in st.session_state["chat_history"]:
        st.markdown(f"**You:** {user_msg}")
        st.markdown(f"**Bot:** {bot_msg}")
