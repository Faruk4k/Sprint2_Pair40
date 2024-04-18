# DataCube Operations Library (dco)

## Introduction

The DataCube Operations Library (dco) is a Python library designed to facilitate operations on datacubes, particularly for querying and analyzing spatiotemporal data. This README provides an overview of the library's functionalities and usage.

## Requirements

- Python 3.x
- IPython (for displaying images)
- Requests library

## Installation

You can install dco via pip:

```bash
pip install dco
```

## Usage

### Initialization

To start using dco, import the library and create an instance of the `dco` class by passing the name of the datacube:

```python
from lib import dco

# Initialize a dco object with the name of the datacube
cube = dco("YourDataCubeName")
```

### Functions

#### 1. Constructing Queries

- **Construct Mean Query**: Constructs a query to retrieve the mean of the datacube.

```python
query = cube.construct_mean_query()
```

- **Construct Temperature Color Query**: Constructs a query to visualize temperature color scaled data for a specific date.

```python
query = cube.construct_temp_color_query(date)
```

- **Construct Diagram Query**: Constructs a query to retrieve a diagram of data within a specified spatiotemporal range.

```python
query = cube.construct_diagram_query(latitude, longitude, start_date, end_date)
```

- **Construct Average Query**: Constructs a query to calculate the average of data within a specified spatiotemporal range.

```python
query = cube.construct_avg_query(latitude, longitude, start_date, end_date)
```

- **Construct Maximum Query**: Constructs a query to find the maximum value within a specified spatiotemporal range.

```python
query = cube.construct_max_query(latitude, longitude, start_date, end_date)
```

- **Construct Minimum Query**: Constructs a query to find the minimum value within a specified spatiotemporal range.

```python
query = cube.construct_min_query(latitude, longitude, start_date, end_date)
```

#### 2. Executing Queries

- **Mean Query**: Executes the constructed query to retrieve the mean of the datacube.

```python
data = cube.mean_query()
```

- **Temperature Color Query**: Executes the constructed query to visualize temperature color scaled data for a specific date.

```python
data = cube.temp_color_query(date)
```

- **Diagram Query**: Executes the constructed query to retrieve a diagram of data within a specified spatiotemporal range.

```python
data = cube.diagram_query(latitude, longitude, start_date, end_date)
```

- **Average Query**: Executes the constructed query to calculate the average of data within a specified spatiotemporal range.

```python
data = cube.avg_query(latitude, longitude, start_date, end_date)
```

- **Maximum Query**: Executes the constructed query to find the maximum value within a specified spatiotemporal range.

```python
data = cube.max_query(latitude, longitude, start_date, end_date)
```

- **Minimum Query**: Executes the constructed query to find the minimum value within a specified spatiotemporal range.

```python
data = cube.min_query(latitude, longitude, start_date, end_date)
```

### Examples

Refer to the Examples.ipynb file for detailed examples on how to use each function.

## Notes

- When creating a `dco` object, ensure accuracy in naming the object as specified in the comments within the code.

- Make sure to verify the format of dates provided.

- Latitude and longitude values must be within the ranges [-90, 90] and [-180, 180] respectively.

---

This README provides an overview of the dco library and its functionalities. For further details and examples, refer to the provided code and documentation.

