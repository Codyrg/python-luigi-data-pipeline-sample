# Luigi Data Pipeline Sample

This is a dead simple example of a Luigi data pipeline. It is meant to be a starting point for your own data pipelines. This specific example is a bit contrived, but it is meant to be simple and easy to understand. This pipeline does the following:
    1. Generate a numpy array of zeros
    2. Add one to each element of the array
    3. Add a random number to each element of the array

Each step of the pipeline will be saved to a CSV file in the `/data` folder.

## Running the pipeline

Ensure that you have the following installed:
    - Python 3.6
    - Luigi
    - Numpy

To run the pipeline, simply run the following commands:
    - Start the Luigi scheduler: `luigid`
    - Run the pipeline: `python main.py`