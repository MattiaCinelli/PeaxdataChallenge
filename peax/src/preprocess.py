import pandas as pd
from pathlib import Path
from ..logs import logging

class PreProcess():
    """
    Due to incompatibility among parquet libraries, jupyter and iOS,  I've decided that the easiest way to show the data on a notebook, is to load in the the terminal and then save as a csv.  
    I've used the following snip of code in the terminal:
    """
    def __init__(self, path:Path = Path('data/').glob('*.parquet')):
        self.logger = logging.getLogger("ProProcess")
        self.path = path

    def preprocess(self):
        for parquet_file in self.path:
            self.logger.info(f"Converting: {parquet_file}")
            df = pd.read_parquet(parquet_file, engine='pyarrow')
            df.to_csv(Path(parquet_file.with_suffix('.csv')), index=False)