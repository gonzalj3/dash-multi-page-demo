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

  3. Run the main platform (single-page):
  python app_6.py
  Navigate to http://localhost:8051
  
  4. Run the multi-page platform:
  python app_5.py
  Navigate to http://localhost:8050

  ## Architecture

  ### Individual Apps
  - **app_1.py** - Basic Dash application with simple button interactions
  - **app_2.py** - Advanced app using dcc.Store for state management and toggle functionality
  - **app_3.py** - Line vs scatter plot toggle demonstration
  - **app_4.py** - Dynamic graph appending approach
  - **app_7.py** - Dynamic graph appending with dictionary-style IDs

  ### Platform Apps
  - **app_6.py** - Single-page platform that combines all apps on one scrollable page (Main Platform)
  - **app_5.py** - Multi-page platform that combines apps using Dash's pages feature
