# MetricMind: Agentic Semantic BI Engine

## Project Overview

MetricMind is an analytics system designed to answer business questions using natural language.

The system connects business questions with a semantic layer, metric calculations, filtering, explanations, and visualizations.

## Key Features

- Natural-language business question parsing
- Semantic metric definitions using YAML
- Sales, profit, and profit-margin calculations
- Region-based filtering
- Product-based filtering
- Business-friendly explanations
- Sales visualization
- Agent orchestration layer
- Git-based project version control

## Example Questions

- What are the sales in Europe?
- What are the sales of laptops?
- What is our revenue in Europe?
- What is the margin in Europe?

## Project Structure

```text
MetricMind/
│
├── data/
│   └── sales_data.csv
│
├── semantic/
│   └── metrics.yaml
│
├── src/
│   ├── agent.py
│   ├── answer_engine.py
│   ├── explanation_engine.py
│   ├── metric_runner.py
│   ├── metrics.py
│   ├── query_engine.py
│   ├── question_parser.py
│   ├── semantic_layer.py
│   └── visualizer.py
│
├── main.py
├── README.md
└── .gitignore