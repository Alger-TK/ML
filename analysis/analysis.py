"""agent_yl data analysising"""

import numpy as np
import pandas as pd
import json
import os
from data import load_tran_data

df = load_tran_data('unpy_devcod.csv')
cust_no = list(set(df.custno))



