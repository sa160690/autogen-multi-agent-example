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

agent_one = ConversableAgent(
    name="hulk",
    system_message="Your name is Hulk and you are a superhero stand-up comedian",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

agent_two = ConversableAgent(
    name="thor",
    system_message="Your name is Thor and your are a superhero stand-up comedian. "
    "Start the next joke from the punchline of the previous joke",
    llm_config= llm_config,
    human_input_mode="NEVER",
)

chat_result = agent_two.initiate_chat(
    recipient=agent_one,
    message="I'm Thor, Hulk, let's keep the jokes rolling."
    "Start the next joke from the punchline of the previous joke",
    max_turns=3
)

pprint.pprint(chat_result.chat_history)
pprint.pprint(chat_result.cost)
pprint.pprint(chat_result.summary)