import numpy as np
import csv
import matplotlib.pyplot as plt
import webbrowser
import streamlit as st

def load_file(file_name: str) -> np.array:
    """This function loads the raster files using the csv library
    Args:
        file_name (str): name of file to be added to path
    Returns:
        np.array: Array containing values for each of the elements (population, railway, geology)
    """

    # Defining an empty list
    file = []

    # Opening raster file and populating list with its content
    with open(f"best.{file_name}.txt") as data:
        csvreader = csv.reader(data, quoting=csv.QUOTE_NONNUMERIC)
        for row in csvreader:
            rowlist = []
            for value in row:
                rowlist.append(value)
            file.append(rowlist)

    return np.array(file)


def scale_map(combined_map: np.array):

    """This function scales the values in the array so that they are between 0-255
    Args:
        combined_map (np.array): values for population, railway and geology combined and not scaled
    Returns:
        scaled map
    """

    # Scaling up the array so that its maximum value is 255
    return (
        (combined_map - combined_map.min())
        * (1 / (combined_map.max() - combined_map.min()) * 255)
    ).astype("uint8")


def multiply_array(chosen_map: list, level: int) -> np.array:
    """This function takes the values in one of the files (map) and multiplies it by the level of importance
        given by user input to that element (population, railway, geology)
    Args:
        chosen_map (list): name of element (population, railway, geology)
        level (int): importance given to element via user input
    Returns:
        np.array: array with values multiplied by level of importance
    """

    # Transforming list into array
    chosen_array = np.array(chosen_map)

    # Multiplying array based on user input
    return np.dot(chosen_array, level)


def combine_maps(pop_level, rail_level, geo_level):

    """This function merges the three maps (population, railway and geology) by summing their values
    Returns:
        function call (combined_map)
    """

    # Loading files for each of the categories
    population_arr = load_file("population")
    railway_arr = load_file("railway")
    geology_arr = load_file("geology")

    # Summing the values of each pixel
    combined_map = (
        multiply_array(population_arr, pop_level)
        + multiply_array(railway_arr, rail_level)
        + multiply_array(geology_arr, geo_level)
    )

    return scale_map(combined_map)


def save_file(combined_map: np.array) -> None:

    """
    This function saves the combined map into a txt file for later download
    Args:
        combined_map (np.array): combined maps containing scaled values for population, railway and geology
    """
    # Opening file to write
    file = open("/tmp/map.txt", "w+")

    # Converting array into string
    content = str(combined_map.tolist())

    # Writing content into file and closing file
    file.write(content)
    file.close()


def update_plot(
    pop_level: int, rail_level: int, geo_level: int, streamlit_run: bool = True
) -> None:
    """
    This function updates the plot after user input
    Args:
        pop_level: level of importance attributed to population
        rail_level: level of importance attributed to railway
        geo_level: level of importance attributed to geology
    """

    map_plot = combine_maps(pop_level, rail_level, geo_level)
    # Saving map to a file
    save_file(map_plot)

    # Plotting map
    fig = plt.figure()
    plt.imshow(map_plot, cmap="gray")

    # If running the app through streamlit, it will plot the map with stramlit syntax
    if streamlit_run is True:

        st.pyplot(fig)

    else:
        plt.show()


def on_confirm_button_clicked(confirm_button, args_list: list) -> None:

    """
    This function calls the update_plot function and passes the list of arguments containing the user iput
    Args:
        args_list: list with user inputs for importance level of population, railway and geology
    """

    pop, rail, geo = args_list

    pop_level = pop.value
    rail_level = rail.value
    geo_level = geo.value

    update_plot(pop_level, rail_level, geo_level, streamlit_run=False)


def on_download_button_clicked(download_button):

    """
    This function generates the download file when button is clicked by user
    """
    url = "file:///tmp/map.txt"
    webbrowser.open(url)
