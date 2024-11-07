import agent
import streamlit as st
import time


def stream_response(user_input):
    response_placeholder = st.empty()
    bot_response = ""

    try:
        for chunk in agent.agent_chain.run(user_input):
            bot_response += chunk
            response_placeholder.markdown(f"**Bot:** {bot_response}")
            time.sleep(0.02)

        st.session_state.chat_history.append(
            (user_input, bot_response.strip()))

    except AttributeError as e:
        print(f"AttributeError: {e}")
        st.error(
            "An error occurred while processing the response. Please try again later."
        )


st.title("LangChain Chatbot")
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

if "last_input" not in st.session_state:
    st.session_state["last_input"] = None


st.subheader("Chat History")
for user_msg, bot_msg in st.session_state["chat_history"]:
    st.markdown(f"**You:** {user_msg}")
    st.markdown(f"**Bot:** {bot_msg}")


with st.form(key="input_form"):
    user_input = st.text_input("You:", key="user_input")
    submit_button = st.form_submit_button(label="Send")

if submit_button and user_input and user_input != st.session_state["last_input"]:
    st.session_state["last_input"] = user_input
    try:
        stream_response(user_input)
    except Exception as e:
        st.error("The service is currently unavailable. Please try again later.")
        print(f"Error details: {e}")
