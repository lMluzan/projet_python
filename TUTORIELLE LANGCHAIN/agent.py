from langchain.agents import create_agent # bibliotheque qui permet de creer des agnets avec langchain
from langchain.tools import tool #c'est un decorateur qui permet de considerer une fonction definit a sa suite comme etant un outils pour notre agent
from langchain_community.tools.tavily_search import TavilySearchResults # qui va nous permetre d'octoyer a l'agent la cappacite de pouvoir faire des recherches sur internet
from langchain_mistralai import chatMistralAI #  on  va utiliser le provider  mistral 
#from langfuse.langchain import callbackHandler
from datetime import datetime
from dotenv import load_dotenv # qui va nous permetre de charger automatiquement toute les variables d'environnement sans avoir besoin de les charger une par une

@tool   # outils permettant de faire des recherches sur internet
def research_tool(query: str)-> str:   # on a besoin d'une clef api pour que cette fonction fonctionne 
    """ Search the web for current price and info  about a product."""
    tavily = TavilySearchResults(max_results = 3) # c'est a dire qu'il va maxiun choisir 3 resultats issue de la  recherche qu'il va faire 
    return str (tavily.invoke(query))

@tool
def vital_charge()-> str: # c'est l'outil que l'agent va interoger a chaque fois qu'il a besoin de connaitre toutes les charges mensuels
    """return the user's monthly vital charges (rent, food , bills ,etc.)."""
    charges = {  #dictionaire contenant les charges mensuels
        "rend" : "$500",
        "food" : "$300",
        "children_schooling" : "$200",
        "electricity" : "$80",
        "internet" : "$40",
        "transport" : "$100",
    }
    return str(charges)


@tool
def salary()-> str: # outils qui va permetre a l'agent de prendre connaissance de mon sallaire
    """return the user's salary"""
    return "2000$"


@tool
def get_current_date()-> str:
    """returns the current date .""" # ceci es une docstring , cest extremenet important pour la comprehension de la tache a execute par l'agent
    return datetime.now().strftime("%Y-%m-%d")

system_prompt = """

    Role : You are a helpful AI assistant with access to tools
    
    goals : your main goal is to analyze something the user wants to buy , check if itis within their budget after vital charges, and provide financial advice.
    consider that the user receives their salary between the 1st and 5th of each month.
    If the purchase is not affordable right now, suggest the best time to buy it and how to save for it.
     
    you can:
    - Search the web for current information
    - Perform calculations
    - Get the current time
     
    Think step-by-step and use tools when needed to provide accurate answers.
    Be concise but thorough.
 """



agent = create_agent(
    model = ChatMistralAI(model= "mistral-large-latest", temperature=0.7)# la temperature c'est la creativite de l'agent plus elle es elevee plus le model es creatif et plus elle tend vers 0 et plus le model sera deterministe
    tools=[research_tool, vital_charge, salary, get_current_date]
    system_prompt = 
)


