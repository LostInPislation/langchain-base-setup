#from app.comp.base_comp import libcomps
#from app.chains.base_chains import libchains
#from app.agents.base_agents import libagents

#Autogen configuration and initialisation
#Run in a new terminal conda activate autogen AND litellm --model ollama/mistral, get the url with the port
#Run this again in a new terminal for each model required for each agent
#Make sure a config exist for each agent

import autogen

config_list_mistral = [
    {
        'base_url': "http://0.0.0.0:8000",
        'api_key': "NULL"
    }
]

config_list_orca2 = [
    {
        'base_url': "http://0.0.0.0:27712",
        'api_key': "NULL"
    }
]

config_list_deepseek = [
    {
        'base_url': "http://0.0.0.0:39831",
        'api_key': "NULL"
    }
]

llm_config_mistral={
    "config_list": config_list_mistral,
}

llm_config_orca2={
    "config_list": config_list_orca2,
}

llm_config_deepseek={
    "config_list": config_list_deepseek,
}

assistant = autogen.AssistantAgent(
    name="Assistant",
    llm_config=llm_config_mistral
)

coder = autogen.AssistantAgent(
    name="Coder",
    llm_config=llm_config_deepseek
)

writer = autogen.AssistantAgent(
    name="Writer",
    llm_config=llm_config_mistral
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswidth("TERMINATE"),
    code_execution_config={"work_dir": "web"},
    llm_config=llm_config_mistral,
    system_message="""Reply TERMINATE if the task has beeen solved at full satisfaction. Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

task="""Tell me a joke"""

groupchat = autogen.GroupChat(agents=[user_proxy, coder, assistant, writer], messages=[],max_round=12)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config_mistral)
user_proxy.initiate_chat(manager,message=task)

#assistant = autogen.AssistantAgent(
#    name="Imgmaker",
#    llm_config=llm_config_mistral
#)

#def start():
    #response = libcomps["llm"]("Tell me a joke")
    #print(response)