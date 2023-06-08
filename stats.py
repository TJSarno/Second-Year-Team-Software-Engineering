import pandas as pd
import numpy as np
from app import cache, CACHE_TIMEOUT_S


@cache.memoize(CACHE_TIMEOUT_S)
def normalize(df, norm_type):
    if norm_type == 'Min-Max':
        df_num = df.select_dtypes(include=[np.number])
        df = df.apply(lambda x: (x - np.mean(x)) / (np.max(x) - np.min(x)))
        df[df_num.columns] = df_num
    elif norm_type == 'Z-Score':
        df_num = df.select_dtypes(include=[np.number])
        df_num = df_num.apply(lambda x: (x - np.mean(x)) / np.std(x))
        df[df_num.columns] = df_num
    return df
