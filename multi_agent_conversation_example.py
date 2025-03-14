import pprint
from utils import get_openai_api_key
from autogen import ConversableAgent


OPEN_API_KEY = get_openai_api_key()
llm_config = {"model": "gpt-3.5-turbo"}

agent = ConversableAgent(
    name="chatBot",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

hulk = ConversableAgent(
    name="hulk",
    system_message="Your name is Hulk and you are a superhero stand-up comedian. "
    "When you're ready to end the conversation, say 'I gotta go'.",
    llm_config=llm_config,
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: "I gotta go" in msg["content"]
)

thor = ConversableAgent(
    name="thor",
    system_message="Your name is Thor and your are a superhero stand-up comedian. "
    "Start the next joke from the punchline of the previous joke. "
    "When you're ready to end the conversation, say 'I gotta go'.",
    llm_config= llm_config,
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: "I gotta go" in msg["content"]
)

chat_result = thor.initiate_chat(
    recipient=hulk,
    message="I'm Thor, Hulk, let's keep the jokes rolling."
    "Start the next joke from the punchline of the previous joke",
    summary_method="reflection_with_llm",
    summary_args={
        "summary_prompt": "Summarise the conversation"
    }
)

pprint.pprint(chat_result.chat_history)
pprint.pprint(chat_result.cost)
pprint.pprint(chat_result.summary)

thor.send(message="What's the last joke we talked about?", recipient= hulk)