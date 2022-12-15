# Site Location Project

Website: https://juliananovaes-site-location-app-vu1rnl.streamlit.app/


<img width="889" alt="image" src="https://user-images.githubusercontent.com/46926638/207828729-feacaf3f-c387-47d2-9124-5e88df7e4114.png">


## Overview
This project aims to create a combined view of the UK map that is able to highlight the best areas to build a factory that makes rock aggregates based on three factors: population, railway networks and geology. 

## Features

### User input: importance of population, railway and geology

In this program, the user is invited to choose the level of importance he/she wants to attribute to each of these categories. The levels vary from 0 to 3 for geology and railway and from 1 to 3 for population. The reason why population is different is because the facotry will need people to work on it regardless. As soon as the user picks the importance level, it is invited to click on the `Confirm my choices` button, and then immediately the program will display the map with the choices reflected on it. 

<img width="390" alt="image" src="https://user-images.githubusercontent.com/46926638/207830760-0c65007c-6139-45e0-bb17-0fc2637aa6e0.png">


### Download the map 

The user is also able to download the final result in the form of a raster file. In order to do so, it is invited to click on the `Download File` button that will appear under the map. 

<img width="370" alt="image" src="https://user-images.githubusercontent.com/46926638/207830834-f540d0a6-3d6c-4b43-9bdf-a70a3439ae16.png">

## Packages and dependencies

The list of libraries and dependencies for the project can be found in the `requirements.txt` file. 
In summary, the main libraries used are `numpy`, `csv`, `matplotlib`, `requests`, `pytest`, `streamlit`,  and `ipywidgets`.

## Interactive Website 

The project is displayed as an interactive website, similar to a notebook, where the user is able to add input tha results in changes in the plot. The website can be accessed here: https://juliananovaes-site-location-app-vu1rnl.streamlit.app/

## Interactive Notebook 

In addition to the website, an interactive notebook is also available. The notebook can be found under the name `notebook_app.ipynb`. In order to run the notebook, you must first run the first cell, which includes all the imports and then the second cell, which contains the interactive widgets. 
Both the website and notebook rely on the same backend file, which is `map.py`. The notebook works in a similar way as the website. The user is invited to add the input and then click on `Confirm my choices`. Finally, if the user wishes to download the file, he/she can do so by clicking on `Download File`. 

<img width="787" alt="image" src="https://user-images.githubusercontent.com/46926638/207830373-25e9e15c-475f-4016-b6ff-31dccaacb399.png">


## Pipeline

The `map.py` file contains all the functions that allow the program to run. It contains the entire process, from the loading of the files to the plotting of the map.

## Tests
Tests were built using `pytest` and can be found in the `map_test.py` file. The report containing the results of the tests 
can be found in the `report.html` file.
