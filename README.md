# AI Real Estate Pipeline (Enterprise Architecture)

## Executive Summary
The **AI Real Estate Pipeline** is a robust, end-to-end autonomous agent designed to revolutionize property underwriting. By orchestrating a seamless flow from raw data ingestion to advanced geospatial visualization, functionality extends beyond simple analysis. The system leverages **GPT-4** for sophisticated risk assessment, **Geopy** for precise location intelligence, and **Monday.com Enterprise** for high-fidelity visualization. This solution eliminates manual overhead, delivering instant, actionable intelligence for high-volume real estate investment.

## Key Features

### 1. Automated Geocoding & Location Intelligence
*   **Precision Mapping**: Utilizes `geopy` to automatically resolve raw address strings into precise Latitude/Longitude coordinates.
*   **Geospatial Data Enrichment**: Enables downstream systems to plot properties accurately on map layers, crucial for neighborhood analysis and logistics planning.

### 2. Advanced Financial Modeling
*   **Investment Logic**: Automatically calculates critical financial metrics including **ARV (After Repair Value)** and **Estimated Renovation Costs** based on property characteristics and condition reports.
*   **Decision Support**: Synthesizes financial data with AI-derived qualitative analysis to generate a definitive "Buy" or "Pass" recommendation.

### 3. Enterprise Visualization
*   **Monday.com Integration**: Pushes structured data to a Monday.com Enterprise Board.
*   **Map View**: Leverages the geocoded coordinates to populate Monday.com's interactive **Map Views**, allowing stakeholders to visualize portfolio distribution and geographic clustering instantly.

## Tech Stack
*   **Core**: Python 3.12
*   **AI/LLM**: OpenAI GPT-4 (via LangChain)
*   **Geospatial**: `geopy` (Nominatim)
*   **Integration**: Monday.com API v2 (GraphQL)
*   **Architecture**: Enterprise Board Architecture
*   **Validation**: Pydantic Strict Schemas

## Installation

1.  **Clone the Repository**
    ```bash
    git clone <repository_url>
    cd AI_Real_Estate_Pipeline
    ```

2.  **Environment Setup**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuration**
    Create a `.env` file in the root directory:
    ```env
    OPENAI_API_KEY=your_openai_key
    MONDAY_API_KEY=your_monday_key
    ```

## Usage

Execute the full data pipeline:

```bash
python -m src.main
```

**Workflow Reference:**
1.  **Ingestion**: Loads raw property data.
2.  **Enrichment**: Geocodes addresses to (Lat, Lon).
3.  **Analysis**: AI evaluates condition & financials.
4.  **Deployment**: Syncs final payload to Monday.com Dashboard & Map View.
