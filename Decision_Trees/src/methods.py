import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


def value_plots(df_series, y_label, x_label, title):
    """
    Function turns df series into ordered horitonzal bar graphs
    Inputs: df.series, pandas dataframe, column series object
            y_label, string, label for the catagories of data
            x_label, string, label for the counts
            title, string, label for the title
    Outputs: None, draws plot from matplotlib 
    """
    df_series = df_series.value_counts()
    vals = df_series.values
    types = df_series.index
    df = pd.DataFrame({x_label: vals
                       , y_label: types
                      }
                     )
    df.set_index(y_label, inplace = True)
    ax = df.plot.barh()
    ax.get_legend().remove()
    plt.xlabel(x_label)
    plt.title(title)
    plt.gca().invert_yaxis()
    plt.tight_layout

