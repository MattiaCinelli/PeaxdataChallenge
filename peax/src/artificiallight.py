import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from ..logs import logging


class ArtificialLighting():
    """
    For crops to grow, they require substantial levels of radiation. A great source of radiation is, of course, the sun. 
    However, as you might have experienced yourself, the sun does not always show up for providing its beloved rays. 
    To overcome this issue, growers have installed assimilation lighting to provide the crops with additional "artificial" radiation. 
    But, as we say in Dutch: "Voor niets gaat de zon op" and assimilation lighting requires a substantial amount of electricity.
    Which makes it a quite expensive option that should be avoided whenever possible. 
    Over the years the greenhouse grower has gained plenty of experience to know when to turn on the **assimilation lightning** and when not to.
    However, he is tired of *switching the light on and off himself and thinks this process is ready to be automated. 
    Do you agree with him that this process can be automated?* If yes, can you show us how this could be achieved?    
    """
    def __init__(self, gc_path:str = 'data/GreenhouseClimate.csv', weather_path:str = 'data/Weather.csv'):
        self.logger = logging.getLogger("ArtificialLighting")
        self.gc_path = gc_path
        self.weather_path = weather_path

    def load_conditions(self):
        """
        """
        self.logger.info("Loading conditions")
        gc = pd.read_csv(self.gc_path, low_memory=False, index_col='%time')
        weather = pd.read_csv(self.weather_path, index_col='%time')
        conditions = pd.merge(gc, weather, left_index=True, right_index=True)
        for col in conditions.columns:
            conditions[col]=conditions[col].astype('float64')
        conditions.index = pd.TimedeltaIndex(conditions.index, unit='d') + datetime(1899, 12, 30)
        return conditions

    def plot_data(self, data, title:str, xlabel:str, ylabel:str, fig_name:str, figsize=(13, 5)):
        _ = plt.figure(figsize=figsize)
        data.plot()
        plt.suptitle(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.savefig(fig_name)
        plt.show()

    