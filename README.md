### AGENT[Query Engine]

This project is a custom query engine built to provide comprehensive information about Ashish Sharma using the Llama Index and Gemini LLM (Language Learning Model). It allows users to interact with the engine to obtain details about Ashish Sharma's professional background and other related queries. The application also captures contact information provided by users.

#### Features
- **Custom Query Engine**: Handles specific queries related to Ashish Sharma.
- **Bullet Point Responses**: All responses are formatted in bullet points for clarity and ease of reading.
- **Information Capture**: Collects and processes contact information provided by users.
- **Agent-Based Interaction**: Utilizes a ReActAgent to handle user queries and context-based responses.

#### Requirements
- Python 3.8+
- Llama Index
- Gemini LLM API Key

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

   Run the `llm.py` script to start the query engine.
   ```bash
   python llm.py
   ```

2. **Querying Information**:

   Example query:
   ```python
   resp = resume_engine.query("What are Ashish Sharma's qualifications?")
   print(resp)
   ```
   The response will be given in bullet points, providing the requested information.

3. **Capturing User Information**:

   The `send_information` function can be used to capture and process contact details:
   ```python
   send_information(mail_id="example@example.com", phone="1234567890", name="John Doe", links="https://linkedin.com/in/johndoe")
   ```

#### Code Structure
- `myqueryEngine`: A custom query engine class that processes user queries and provides structured responses.
- `send_information`: A function that handles and prints user-provided contact information.
- `tools`: A list of tools integrated with the agent to handle specific tasks.
- `ReActAgent`: Manages the tools and the overall query handling process.

#### Example Queries
- **Ask for contact**: 
  - "My name is John Doe and my email id is xyz@gmail.com. I want to contact Ashish Sharma."
- **Request qualifications**: 
  - "Tell me about Ashish Sharma's academic qualifications."
- **Inquire about experience**: 
  - "What is Ashish Sharma's professional experience?"

