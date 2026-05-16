# ece105-lab3-plots

Synthetic temperature sensor data visualizations using NumPy and Matplotlib.

## Description

This project generates simulated readings from two temperature sensors and produces three publication-quality plots: a scatter plot, an overlaid histogram, and a side-by-side box plot. All visualizations are saved to a single PNG file.

## Installation

1. Activate the ece105 conda environment:
2. Install dependencies if not already present:
## Usage
This produces `sensor_analysis.png` in the project directory.

## Example Output

Running the script creates a 1x3 subplot figure (`sensor_analysis.png`) containing:

- **Scatter plot** — Sensor A (blue) and Sensor B (orange) temperature readings over time (0-10 seconds).
- **Histogram** — Overlaid distributions of both sensors with dashed vertical lines at each sensor's mean.
- **Box plot** — Side-by-side comparison of the two sensor distributions with a dashed line at the combined overall mean.

## Project Structure
## AI Tools Used and Disclosure

This project was completed with the assistance of Claude (Anthropic) as an AI coding tool. These tools were used to:
- Generate initial implementations of each plotting function based on intent comments written beforehand.
- Suggest NumPy-style docstring formatting for all functions.
- Help draft this README.

All generated code was reviewed and tested before being committed.
