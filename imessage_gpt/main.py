from constants import * 
from utils import *

import pandas as pd 
import subprocess
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

### GETTING THE PHONE NUMBERS TO WHICH WE WANT TO SEND MESSAGES
contact_numbers = ALLOWED_RECIPIENT_NUMBERS

### FETCHING THE MESSAGES
df = messages_data(DB_PATH, contact_numbers)
should_answer = actions_to_take(df, contact_numbers)
print(should_answer)
cleaned_df = cleaning_messages(df)

### GETTING THE LAST MESSAGES FOR ADDITIONAL CONTEXT
### For now, we’ll use the last messages from the interlocutor. There can be several messages. We’ll concatenate them.
last_messages_context = last_messages(cleaned_df, should_answer)

for user in should_answer.keys():
    if should_answer[user]:
        print("Sending a message to " + user)
        print(user, contact_numbers[user])

        #### CHAT MODEL
        chat = ChatOpenAI(temperature=0, openai_api_key=OPEN_AI_KEY, model_name="gpt-3.5-turbo-0613")

        # Templates
        chat_template = "You are a great conversationalist. You are talking to {user}, and they just sent you a text. Craft an answer pretending to be me (my name is {your_name}). I often use emojis."
        system_message_prompt = SystemMessagePromptTemplate.from_template(chat_template)
        human_template = "{messages}"
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
        
        # Chat prompt
        chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
        chat_prompt.format_messages(user=contact_numbers[user], your_name = YOUR_NAME, messages=last_messages_context[user])

        # Chain
        chain = LLMChain(llm=chat, prompt=chat_prompt)
        response = chain.run(user=contact_numbers[user], messages=last_messages_context[user])

        # Formatting the response    
        MESSAGE = "{}".format(response)
        MESSAGE = MESSAGE.replace("Malo:", "", 1)  # The third argument ensures only the first occurrence is replaced
        MESSAGE = MESSAGE.strip()
        print(MESSAGE)
        # Sending the message
        subprocess.run(['osascript', SCRIPT_PATH, user, MESSAGE], check=True)
