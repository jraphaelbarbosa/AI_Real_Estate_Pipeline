# AI Real Estate Underwriter (Monday.com Integrated)

## Executive Summary
The **AI Real Estate Underwriter** is an autonomous agent designed to streamline the property analysis process. It ingests raw property data, leverages **GPT-4** to perform sophisticated risk analysis (generating "Buy" or "Pass" recommendations), and seamlessly syncs strict, structured results to a **Monday.com** board via GraphQL. This system eliminates manual data entry and provides instant, AI-driven insights for real estate investment decisions.

## Visuals
![Dashboard Demo](link_to_gif_or_video)
*The system automatically updates the Monday.com dashboard, visualizing risk levels via status colors (Red/Orange/Green).*

## Tech Stack
*   **Python 3.12**: Core programming language.
*   **LangChain**: Framework for orchestrating AI workflows.
*   **OpenAI GPT-4**: Engine for advanced logic and risk assessment.
*   **Monday.com API**: Integration target for results visualization.
*   **Pydantic**: Data validation and schema definition.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd AI_Real_Estate_Pipeline
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    Create a `.env` file in the root directory and add your API keys:
    ```env
    OPENAI_API_KEY=your_openai_key
    MONDAY_API_KEY=your_monday_key
    ```

## Usage

To run the full pipeline:

```bash
python -m src.main
```

The system will:
1.  Ingest mock property data.
2.  Analyze each property using the AI model.
3.  Post the results to the configured Monday.com board.
