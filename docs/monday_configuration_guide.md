# Monday.com Configuration Guide (Phase 2 BI)

This guide walks through the manual steps required to configure Monday.com for Business Intelligence visualizations using the Real Estate Pipeline data.

## 1. Map View Setup
The Map View allows you to visualize property locations directly on the board.

1.  Open your **Monday.com Board**.
2.  Click the **+ (Plus)** icon next to the "Main Table" tab at the top left.
3.  Select **Map** from the Views dropdown.
4.  In the Map View settings (right sidebar):
    *   **Location Column:** Select **"Name"** (The first column, created by `item_name`).
    *   *Note:* The pipeline places the full address string into the Item Name, so Monday.com can geocode it automatically.

## 2. Dashboard & Chart Setup
Create a dashboard to analyze portfolio performance and AI recommendations.

1.  Click the **+ (Plus)** icon at the top left again.
2.  Select **Blank View** (or **Dashboard** if creating a separate board view).
3.  Click **Add Widget** -> **Chart**.
4.  Click on the settings (three dots) of the Chart Widget -> **Settings**.
5.  **Configure the Chart:**
    *   **Chart Type:** Pie Chart.
    *   **Labels (X-Axis):** Select **"Status"**.
    *   **Values (Y-Axis):** Select **"Count Items"**.
    *   *Goal:* This visualizes the distribution of AI recommendations (BUY, PASS, REVIEW).

## 3. Automation Setup
Get notified when the AI finds a high-potential property.

1.  Click the **Automate** button at the top right of the board.
2.  Select **Create Custom Automation**.
3.  **Trigger:** "When **Status** changes to..."
    *   Select the **Status** column.
    *   Select **"Buy"** (or the specific label for recommended properties).
4.  **Action:** "Notify **me**".
    *   Customize the notification message (e.g., *"AI found a new BUY opportunity: {Item Name}"*).
5.  Click **Create Automation**.
