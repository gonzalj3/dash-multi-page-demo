# Multi-Page Dash Application Platform

  A demonstration of how to create a unified Dash platform that integrates multiple standalone applications.

  ## Quick Start

  1. Install dependencies:
  ```bash
  pip install dash dash-daq numpy

  2. Run individual apps:
  python app_1.py  # Basic application
  python app_2.py  # Toggle state management  
  python app_3.py  # Line vs scatter plots
  python app_4.py  # Append approach

  3. Run the multi-page platform:
  python app_5.py
  Navigate to http://localhost:8050

  Architecture

  - app_1.py: Basic Dash application
  - app_2.py: dcc.Store for toggle state persistence
  - app_3.py: Plot type switching (line/scatter)
  - app_4.py: Graph append approach
  - app_5.py: Multi-page platform integrating all apps
