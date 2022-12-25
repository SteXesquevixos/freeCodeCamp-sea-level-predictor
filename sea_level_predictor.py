import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

'''Use Pandas to import the data from epa-sea-level.csv'''

df = pd.read_csv('epa-sea-level.csv')

'''Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column 
    as the y-axis. 
    Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best 
    fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict 
    the sea level rise in 2050.
    Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the 
    line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has 
    since the year 2000.
    The x label should be Year, the y label should be Sea Level (inches), and the title should be Rise in Sea Level.'''


def draw_plot():
    # Increasing data by 2050
    for i in range(1, 38):
        df.loc[133 + i] = [2013 + i, np.nan, np.nan, np.nan, np.nan]

    # Scatter plot
    fig, ax = plt.subplots(figsize=(10, 9))

    ax.scatter(df['Year'].loc[:133],
               df['CSIRO Adjusted Sea Level'].loc[:133],

               color=(0.2, 0.4, 0.6, 0.6), linewidth=2.5)

    # Create first line of best fit
    result = linregress(df['Year'].loc[:133], df['CSIRO Adjusted Sea Level'].loc[:133])
    slope = result.slope
    intercept = result.intercept

    # Create an array with the years 1880 through 2050 for x-values
    x_vals_CSIRO = np.array(list(df['Year']))
    y_vals_CSIRO = slope * x_vals_CSIRO + intercept

    ax.plot(x_vals_CSIRO,
            y_vals_CSIRO,
            color='red', alpha=0.5, linewidth=2)


    # Create second line of best fit
    result2 = linregress(df['Year'].iloc[120:134], df['CSIRO Adjusted Sea Level'].iloc[120:134])
    slope2 = result2.slope
    intercept2 = result2.intercept

    # Create an array with the years 2000 through 2050 for x-values
    x_vals_later = np.array(list(df['Year'].iloc[120:]))
    y_vals_later = slope2 * x_vals_later + intercept2

    ax.plot(x_vals_later,
            y_vals_later,
            color='red', alpha=0.5, linestyle='--', linewidth=2)

    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    plt.savefig('sea_level_plot.png')

    return plt.gca()