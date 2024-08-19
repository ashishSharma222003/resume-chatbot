### AGENT[QueryEngine]

![App Preview](assets/dashboard.png)

This project is a custom query engine built to provide comprehensive information about Ashish Sharma using the Llama Index and Gemini LLM (Language Learning Model). The application allows users to interact with the engine to obtain details about Ashish Sharma's professional background, as well as capturing contact information provided by users.

#### Features
- **Custom Query Engine**: Handles specific queries related to Ashish Sharma.
- **Bullet Point Responses**: All responses are formatted in bullet points for clarity and ease of reading.
- **Information Capture**: Collects and processes contact information provided by users.
- **Streamlit Interface**: A user-friendly interface built with Streamlit to interact with the query engine.

#### Requirements
- Python 3.8+
- Llama Index
- Gemini LLM API Key
- Streamlit

#### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the `Gemini_api` key in the `constant.py` file.

#### Usage
1. **Running the Application**: 

   Run the `app.py` script to start the Streamlit interface for the query engine.
   ```bash
   streamlit run app.py
   ```

2. **Querying Information**:

   Use the chat interface to ask questions about Ashish Sharma. The application will respond with structured, bullet-point answers.

3. **Capturing User Information**:

   The application allows users to share their contact details, which will be processed and forwarded.

#### Code Structure
- **llm.py**: Contains the core logic for the custom query engine, including handling queries and generating responses.
- **app.py**: Contains the Streamlit interface code, allowing users to interact with the query engine in a web-based environment.
- **constant.py**: Stores the API keys and other constants used in the application.
- **MyInfo.py**: Contains prompts required to form answer.

#### Example Queries
- **Ask for contact**: 
  - "My name is John Doe and my email id is xyz@gmail.com. I want to contact Ashish Sharma."
- **Request qualifications**: 
  - "Tell me about Ashish Sharma's academic qualifications."
- **Inquire about experience**: 
  - "What is Ashish Sharma's professional experience?"

#### Files in the Project
- **app.py**: The main file that runs the Streamlit application. It provides the frontend interface for users to interact with the assistant.
- **llm.py**: Handles the backend logic of querying and processing information about Ashish Sharma.
