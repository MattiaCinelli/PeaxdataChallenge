
import os
import numpy as np
import pandas as pd
import seaborn as sns
from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime

from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import r2_score, mean_squared_error

from ..logs import logging

from abc import ABC, abstractmethod
class Forecast(ABC):
    '''Operations'''
    @abstractmethod
    def forecast():
        pass

class GetAutoReg(Forecast):
    '''Compute Max'''
    def forecast(data, lags:int=1):
        model = AutoReg(data, lags=lags)
        model_fit = model.fit()
        return model_fit.predict()[1:]

class GetARIMA(Forecast):
    """
    This method is used to forecast the heating consumption using the ARIMA model.
    """
    def forecast(data, order:tuple=(1, 1, 1)):
        model = ARIMA(data, order=order)
        model_fit = model.fit()
        return model_fit.predict()[1:]


class GetSARIMAX(Forecast):
    """
    This method is used to forecast the heating consumption using the SARIMA model.
    """
    def forecast(data, order:tuple=(2, 0, 1)):
        model = SARIMAX(data, order=order)
        model_fit = model.fit()
        return model_fit.predict()[1:]

class HeatingConsumption:
    """
    This class is used to forecast the heating consumption.
    """
    def __init__(self):
        self.logger = logging.getLogger("Heating Consumption")

    @abstractmethod
    def get_forecast(self):
        r2_scores, mses = [], []
        for forecast in Forecast.__subclasses__():
            predict = forecast.forecast(self)
            r2_scores.append(r2_score(self[1:], predict))
            mses.append(mean_squared_error(self[1:], predict))
        return pd.DataFrame(
            {'r2_score': r2_scores, 'MSE': mses}, 
            index=[model.__name__ for model in Forecast.__subclasses__()])

