# AI-Powered Annual Report Analyzer

A Python-based financial analysis portfolio project that combines financial KPI calculations, data visualization, PDF text extraction, and AI-generated commentary.

The project analyzes **Hove A/S Annual Report 2025** and presents the results in an interactive Streamlit dashboard.

## Project Overview

The goal of this project is to demonstrate how Python and AI can support financial statement analysis.

The application presents:

- Financial KPIs for 2024 and 2025.
- Revenue and EBITDA growth calculations.
- EBITDA margin analysis.
- Financial data visualizations.
- AI-generated commentary explaining financial performance.
- References to the annual report.

## Technologies Used

- **Python** — financial calculations and application logic.
- **pandas** — financial data processing.
- **matplotlib** — financial charts.
- **pdfplumber** — extraction of management commentary from the PDF during development.
- **Qwen2.5-3B-Instruct** — AI-generated financial analysis using Google Colab.
- **Streamlit** — interactive dashboard.

## Key Financial Findings

The analysis of Hove A/S shows:

- Revenue increased by **23.5%** from 2024 to 2025.
- EBITDA increased by **67.3%**.
- EBITDA margin improved from **8.0% to 10.8%**.
- Gross margin declined from **37.0% to 34.8%**.

The AI-generated analysis explains the EBITDA development using financial data and management commentary from the annual report.

## How to Run the Application

1. Download or clone this repository.
2. Install the required libraries:

   `python -m pip install -r requirements.txt`

3. Start the Streamlit application:

   `python -m streamlit run app.py`

4. Open the local address displayed in your terminal.

## Methodology

Financial figures were transcribed and verified against Hove A/S Annual Report 2025.

Python was used to calculate financial KPIs and visualize financial performance.

Management commentary was extracted from the PDF using pdfplumber. Qwen2.5-3B-Instruct was used in Google Colab to generate an initial financial analysis. A missing verified cost contribution was subsequently added using Python.

The Streamlit application displays the saved analysis.

## Limitations

This is a **Hove-specific proof-of-concept (V1)**.

The application does not currently support automatic financial statement extraction from arbitrary uploaded annual reports or live AI inference.

Future improvements could include automated KPI extraction, support for multiple companies, and more robust AI output validation.

## Data Sources

Hove A/S Annual Report 2025:

- Page 17 — Consolidated financial figures.
- Page 4 — Management commentary on revenue.

## Project Purpose

This project was developed as a practical learning and portfolio project to demonstrate skills in Python programming, financial analysis, data visualization, and applied AI.
