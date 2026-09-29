import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv('data/netflix_titles.csv')

df = df.drop_duplicates()