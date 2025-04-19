# Wikipedia-to-PPT Agent System

An intelligent agent system that retrieves content from Wikipedia and generates dynamic PowerPoint presentations based on that content. Leveraging language models and structured tools, it automates the creation of informative and visually appealing presentations.

## 🚀 Features

- **Wikipedia Integration**: Fetches complete content from any English Wikipedia page.
- **Dynamic Slide Generation**: Creates slides with various layouts, including title-only, content, bullet points, and images.
- **Customizable Presentations**: Allows users to define slide layouts and content types.
- **Image Handling**: Supports both local and URL-based images for slides.
- **Logging**: Provides detailed logs for debugging and tracking.

## 🛠️ Components

### `tools.py`

Contains utility functions:

- `get_wikipedia_content(query: str) -> str`: Fetches the full content of a Wikipedia page.
- `create_dynamic_presentation(ppt_spec: dict, output_filename: str = "dynamic_presentation.pptx") -> str`: Generates a PowerPoint presentation based on a given spec.

### `agent.py`

Defines intelligent agents:

- `wikipedia_agent`: Retrieves Wikipedia content using `get_wikipedia_content`.
- `generate_ppt_agent`: Generates a PowerPoint presentation from structured content.
- `root_agent`: Coordinates the above agents to perform the full Wikipedia-to-PPT flow.

## 📦 Installation

### Prerequisites

- Python 3.7+
- `pip` package manager

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/kevalmahajan/google-adk-multiagent-system.git
   cd google-adk-multiagent-system
   ```

2. Install dependencies
    ```bash   
   pip install -r requirements.txt
   ```

3. Install dependencies
    ```bash   
   pip install -r requirements.txt
   ```

4. Run the agents
    ```bash   
   adk run           #Run an interactive CLI for a certain agent.
   adk api_server    #Start a FastAPI server for agents.
   adk web           #Start a FastAPI server with Web UI for agents.
   ```


## 🧪 Usage

To use the system:

1. **Interact with the `root_agent`**: Provide a Wikipedia query.
2. **`wikipedia_agent`**: Fetches content from Wikipedia based on the query.
3. **`generate_ppt_agent`**: Converts the fetched content into a structured slide JSON.
4. **`create_dynamic_presentation` tool**: Generates a PowerPoint `.pptx` file based on the structured slide JSON.

The output will be saved as `dynamic_presentation.pptx`.

##
**Note:** This repo is just for exploring google-adk and creating a multiagent system.

