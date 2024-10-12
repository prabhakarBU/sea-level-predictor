import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    linegressfitone = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    minyear = df["Year"].min()
    # print(minyear)
    xone = range(minyear, 2050, 1)
    yone = linegressfitone.intercept + linegressfitone.slope*xone
    plt.plot(xone,yone)

    # Create second line of best fit
    df_2000 = df[df["Year"]>2000]
    # maxyear = df["Year"].max()
    # print(maxyear)
    linegressfittwo = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    xtwo = range(2000, 2050, 1)
    ytwo = linegressfittwo.intercept + linegressfittwo.slope*xtwo
    plt.plot(xtwo,ytwo)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()