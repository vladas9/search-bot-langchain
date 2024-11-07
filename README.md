# Streamlit LangChain Chatbot

A robust, interactive chatbot application powered by [Streamlit](https://streamlit.io) and [LangChain](https://langchain.com). This project integrates language models and natural language processing capabilities to create an engaging user experience.

## Features

- **Real-time Chat Interface**
- **Modular Design for Customization**
- **Scalable and Easy to Deploy**

## Getting Started

### Building and Running the Project

#### With Docker

1. **Build the Docker image**:

   ```bash
   docker build -t streamlit-langchain-chatbot .
   ```

2. **Run the Docker container**:

   ```bash
   docker run -d -p 8501:8501 --name streamlit-chatbot-container streamlit-langchain-chatbot
   ```

3. **Access the App**: Navigate to `http://localhost:8501` in your web browser.

#### Without Docker

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/streamlit-langchain-chatbot.git
   cd streamlit-langchain-chatbot
   ```

2. **Create a Virtual Environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:

   ```bash
   streamlit run app.py
   ```

5. **Access the App**: Navigate to `http://localhost:8501` in your web browser.

## Showcase

Here's what the project looks like in action:

![Screenshot 1](./showcase/image1.png)
