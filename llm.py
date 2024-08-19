from llama_index.core.agent import ReActAgent
from llama_index.core.tools import BaseTool, FunctionTool
from typing import Optional
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.query_engine import CustomQueryEngine
from llama_index.llms.gemini import Gemini
from MyInfo import resume_points,agent_prompt
from constant import Gemini_api
from llama_index.core import Settings
from llama_index.core.llms import MessageRole, ChatMessage
from llama_index.core.prompts import ChatPromptTemplate


Settings.llm = Gemini(api_key=Gemini_api)

llm = Gemini(api_key=Gemini_api)
class myqueryEngine(CustomQueryEngine):
    """RAG String Query Engine."""
    
    llm: Gemini
    prompt: str = None

    def custom_query(self, query: str):
        """Give query response to my answer"""
        if self.prompt is None:
            raise ValueError("Prompt cannot be None")

        question = (
            "You are an admirer of Ashish Sharma and provide comprehensive information about him.\n"
            "Instructions:\n"
            "1. Always understand what the question is asking.\n"
            "2. Break down the question into multiple parts. Answer each part separately, and then combine the answers to form a comprehensive response.\n"
            "3. Utilize the information provided below to formulate a response to the query concerning Ashish Sharma.\n"
            "4. Always answers in bullets that are comprehensive."
        )
        question += self.prompt + "\n\n**IMPORTANT**\nRespond only to questions related to Ashish Sharma and refrain from addressing any other questions.\n\nQuery: " + query + "\nResponse: "
        
        response = self.llm.complete(question)
        
        return str(response)


def send_information(mail_id: Optional[str] = None, phone:Optional[str] = None,name:Optional[str] = None,links:Optional[str] = None):
    """If user want to contact me or he has given any of his contact information or want to share any of the link """
    print("****************")
    print("****************")
    print(mail_id)
    print(phone)
    print(name)
    print(links)
    print("*****************")
    print("*****************")

information_tool=FunctionTool.from_defaults(fn=send_information,name="Information_capturer")

resume_engine=myqueryEngine(llm=llm,prompt=resume_points)

tools=[
    QueryEngineTool(
        query_engine=resume_engine,
        metadata=ToolMetadata(
            description="This Tool will gives all information regarding of Ashish Sharma",
            name="Ashish",
        ),
    ),
    information_tool,
]

chat_history_template=[
    ChatMessage(
        content="You are a supporter of Ashish Sharma, providing comprehensive professional information about him.",
        role=MessageRole.SYSTEM,
    ),
    ChatMessage(
        content="Give introduction about Ashish Sharma in 20 words",
        role=MessageRole.USER
    )
]
chat_template=ChatPromptTemplate(chat_history_template)


agent = ReActAgent.from_tools(
    tools=tools,
    llm=llm,
    # chat_history=chat_history_template,
    max_iterations=5,
    verbose=True,
    context=agent_prompt,
    response_mode="accumulate"
)


if __name__=="__main__":
    resp=resume_engine.query("what is ashish qalifications.")
    print(str(resp))