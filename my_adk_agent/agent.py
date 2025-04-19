
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from my_adk_agent.tools import get_wikipedia_content, create_dynamic_presentation

PROVIDER = "google"  # or "litellm", "vllm", "google"

if PROVIDER == "litellm":
    # Use any anthropic, openai, or ollama model, api_key should be provided in the .env file
    model=LiteLlm(model="anthropic/claude-3")
 
elif PROVIDER == "vllm":
    # Self-hosted vLLM model
    api_base_url = "http://vllm_url/v1"
    model_name = "provider/model_name"  # e.g. "openai/gpt-4o"
    model=LiteLlm(
            model=model_name,
            api_base=api_base_url,
            api_key="12345"
        )

elif PROVIDER == "google":
    # Use a Google Gemini model
    model="gemini-2.0-flash-exp"
       



# This agent will use the get_wikipedia_content tool to search for any Wikipedia page and return the complete content.
wikipedia_agent = LlmAgent(
    name="wikipedia_agent",
    model=model,
    description=(
        "Agent to search any Wikipedia page and return the complete content."
        ),
    instruction=(
        "You are an agent that can search Wikipedia pages and return the complete content by using the given tool."
        ),
    tools=[get_wikipedia_content],
    output_key="data"   # Saves output to state['data']
)

# This agent will use the output of the wikipedia agent to create a dynamic presentation
generate_ppt_agent = LlmAgent(
    name="generate_ppt_agent",
    model=model,
    description=(
        """Generates a PowerPoint presentation based on the provided specification.
        The specification includes a title and a list of slides with varying layouts and content.
        The agent can handle title-only slides, title + content slides, bullet point slides, and image slides."""  
    ),
    instruction=(
        """Get complete data from state key 'data', according to the data, create a json input for the create_dynamic_presentation tool. Include all the required data for the presentation.
        To create the dynamic input JSON for the PowerPoint generation function, you need to define a dictionary that includes a presentation "title" and a list of "slides", where each slide is a dictionary specifying its "layout" and relevant content fields. The layout determines which keys are required: for example, a "title_only" layout needs only a "title"; a "title_content" layout needs both "title" and "content"; a "bullet_slide" requires a "title" and a list of "bullets"; and an "image_slide" should include a "title" and an "image" URL. You can dynamically generate this JSON from user input, form data, or another structured source by appending slide dictionaries to the "slides" list according to the desired content and layout. The complete dictionary can then be passed to the function as ppt_spec. Include as much detailed information as possible in the json.
        Example json:
        {
        "title": "Dynamic Presentation Demo",
        "slides": [
            {
                "layout": "title_only",
                "title": "Welcome to the Demo"
            },
            {
                "layout": "title_content",
                "title": "Overview",
                "content": "This slide explains how dynamic layouts can adapt based on content from an LLM."
            },
            {
                "layout": "bullet_slide",
                "title": "Key Points",
                "bullets": [
                    "Different layouts based on input",
                    "Adaptive slide creation",
                    "Easy integration with agentic systems"
                ]
            },
            {
                "layout": "image_slide",
                "title": "Featured Image",
                "image": "https://dualbootpartners.com/wp-content/uploads/2025/01/Introducin-Agentic-AI_op2.png"
            }
        ]
    }
    After this json is created, use the tool: create_dynamic_presentation to create the presentation with the json as an input to the tool."""   
    ),
    tools=[create_dynamic_presentation]
)

# This agent will use the wikipedia agent and generate_ppt_agent and provide the final output
root_agent = LlmAgent(
    name="coordinator_agent",
    description=(
        "Agent to retrieve Wikipedia content and generate a PowerPoint presentation based on that content."
    ),
    model=model,
    sub_agents=[wikipedia_agent,generate_ppt_agent]   
)



