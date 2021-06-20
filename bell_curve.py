import pandas as pd
import plotly.figure_factory as ff

data = pd.read_csv('./hwFiles/data/mobile_brands.csv')

dist_figure = ff.create_distplot([data["Avg Rating"]], ["Result"],  show_hist=False)

dist_figure.show()