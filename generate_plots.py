"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np
import matplotlib.pyplot as plt


def generate_data(seed):
    """Generate synthetic temperature sensor readings.

    Parameters
    ----------
    seed : int
        Random number generator seed for reproducibility.

    Returns
    -------
    sensor_a : numpy.ndarray
        Temperature readings from sensor A in Celsius, shape (200,).
    sensor_b : numpy.ndarray
        Temperature readings from sensor B in Celsius, shape (200,).
    timestamps : numpy.ndarray
        Measurement timestamps in seconds, shape (200,).
    """
    rng = np.random.default_rng(seed=seed)
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=200)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=200)
    timestamps = rng.uniform(low=0.0, high=10.0, size=200)
    return sensor_a, sensor_b, timestamps


def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Plot sensor readings vs timestamps as a scatter plot.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Temperature readings from sensor A in Celsius, shape (200,).
    sensor_b : numpy.ndarray
        Temperature readings from sensor B in Celsius, shape (200,).
    timestamps : numpy.ndarray
        Measurement timestamps in seconds, shape (200,).
    ax : matplotlib.axes.Axes
        Axes object to draw the plot on. Modified in place.

    Returns
    -------
    None
    """
    ax.scatter(timestamps, sensor_a, color='blue', alpha=0.6, label='Sensor A', s=15)
    ax.scatter(timestamps, sensor_b, color='orange', alpha=0.6, label='Sensor B', s=15)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Sensor Readings vs Time')
    ax.legend()


def plot_histogram(sensor_a, sensor_b, ax):
    """Plot overlaid histograms of sensor temperature distributions.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Temperature readings from sensor A in Celsius, shape (200,).
    sensor_b : numpy.ndarray
        Temperature readings from sensor B in Celsius, shape (200,).
    ax : matplotlib.axes.Axes
        Axes object to draw the plot on. Modified in place.

    Returns
    -------
    None
    """
    ax.hist(sensor_a, bins=30, alpha=0.5, color='blue', label='Sensor A')
    ax.hist(sensor_b, bins=30, alpha=0.5, color='orange', label='Sensor B')
    ax.axvline(np.mean(sensor_a), color='blue', linestyle='--', linewidth=1.5, label='Mean A')
    ax.axvline(np.mean(sensor_b), color='orange', linestyle='--', linewidth=1.5, label='Mean B')
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Count')
    ax.set_title('Temperature Distribution by Sensor')
    ax.legend()


def plot_boxplot(sensor_a, sensor_b, ax):
    """Plot side-by-side box plots comparing sensor distributions.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Temperature readings from sensor A in Celsius, shape (200,).
    sensor_b : numpy.ndarray
        Temperature readings from sensor B in Celsius, shape (200,).
    ax : matplotlib.axes.Axes
        Axes object to draw the plot on. Modified in place.

    Returns
    -------
    None
    """
    ax.boxplot([sensor_a, sensor_b], tick_labels=['Sensor A', 'Sensor B'])
    overall_mean = np.mean(np.concatenate([sensor_a, sensor_b]))
    ax.axhline(overall_mean, color='red', linestyle='--', linewidth=1.5, label=f'Overall Mean ({overall_mean:.2f}°C)')
    ax.set_xlabel('Sensor')
    ax.set_ylabel('Temperature (deg C)')
    ax.set_title('Sensor Temperature Box Plot')
    ax.legend()


def main():
    """Generate data, create all three plots, and save the figure.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    sensor_a, sensor_b, timestamps = generate_data(seed=2214)

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    plot_scatter(sensor_a, sensor_b, timestamps, axes[0])
    plot_histogram(sensor_a, sensor_b, axes[1])
    plot_boxplot(sensor_a, sensor_b, axes[2])

    plt.tight_layout()
    plt.savefig('sensor_analysis.png', dpi=150, bbox_inches='tight')
    print("Saved sensor_analysis.png")


if __name__ == '__main__':
    main()
