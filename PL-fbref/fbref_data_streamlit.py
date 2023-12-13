# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 17:57:06 2023

@author: basus
"""

import streamlit as st
import pandas as pd
import numpy as np
import webScraper
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap
from pathlib import Path
from plottable import ColumnDefinition, Table
from plottable.cmap import normed_cmap
from plottable.formatters import decimal_to_percent
from plottable.plots import circled_image # image


def tableViz(df_old):    
    cols = [
        "_0_Squad",
        "PlayingTime_1_MP",
        "Performance_2_Gls",
        "Performance_2_Ast",
        "Performance_2_G+A",
        "Performance_2_PK",
        "Performance_2_CrdY",
        "Performance_2_CrdR",
        "Expected_3_xG",
        "Expected_3_npxG",
        "Expected_3_xAG",
    ]
    
    df = df_old[cols].copy()
    
    colnames = [
        "Team",
        "Matches Played",
        "Goals",
        "Assists",
        "G+A",
        "Penalties scored",
        "Yellow Cards",
        "Red Cards",
        "xG",
        "Non-penalty xG",
        "xG-Assisted Goals",
    ]

    col_to_name = dict(zip(cols, colnames))
    df = df.rename(col_to_name, axis=1)
    
    #https://logos-world.net/premier-league-team-logos-top-epl-logos/   
    
    flag_paths = list(Path("logos").glob("*.png"))
    country_to_flagpath = {p.stem: p for p in flag_paths}
    df.insert(0, "Flag", df["Team"].apply(lambda x: country_to_flagpath.get(x)))
    df = df.set_index("Team")

    cmap = LinearSegmentedColormap.from_list(
    name="bugw", colors=["#ffffff", "#f2fbd2", "#c9ecb4", "#93d3ab", "#35b0ab"], N=256
    )
    
    actual_cols = list(df.columns[2:7])
    expected_cols = list(df.columns[8:])
    
    
    col_defs = (
    [
        ColumnDefinition(
            name="Flag",
            title="",
            textprops={"ha": "center"},
            width=0.5,
            plot_fn=circled_image,
        ),
        ColumnDefinition(
            name="Team",
            textprops={"ha": "left", "weight": "bold"},
            width=1.5,
        ),
        ColumnDefinition(
            name="Matches Played",
            title = "Matches Played".replace(" ", "\n", 1),
            textprops={"ha": "center"},
            width=1,
        ),
    ]
    +[
        ColumnDefinition(
            name="Goals",
            width=0.75,
            textprops={
                "ha": "center",
                "bbox": {"boxstyle": "circle", "pad": 0.35},
            },
            #cmap=normed_cmap(df["Goals"], cmap=matplotlib.cm.PiYG, num_stds=2.5),
            group="Actual Performance",
            border="left",
        ),
        ColumnDefinition(
            name="Assists",
            width=0.75,
            textprops={
                "ha": "center",
                "bbox": {"boxstyle": "circle", "pad": 0.35},
            },
            #cmap=normed_cmap(df["Assists"], cmap=matplotlib.cm.PiYG_r, num_stds=2.5),
            group="Actual Performance",
        ),
    ]
    + [       
        ColumnDefinition(
            name=col,
            title=col.replace(" ", "\n", 1),
            #formatter=decimal_to_percent,
            group="Actual Performance",
        )
        for col in actual_cols[2:]
    ]
    + [
        ColumnDefinition(
            name=expected_cols[0],
            title=expected_cols[0].replace(" ", "\n", 1),
            #formatter=decimal_to_percent,
            cmap=cmap,
            group="Expected Performance",
            border="left",
        )
    ]
    + [
        ColumnDefinition(
            name=col,
            title=col.replace(" ", "\n", 1),
            #formatter=decimal_to_percent,
            cmap=cmap,
            group="Expected Performance",
        )
        for col in expected_cols[1:]
    ]
        )
    
    plt.rcParams["font.family"] = ["DejaVu Sans"]
    plt.rcParams["savefig.bbox"] = "tight"


    fig, ax = plt.subplots(figsize=(20, 22))

    table = Table(
        df,
        column_definitions=col_defs,
        row_dividers=True,
        footer_divider=True,
        ax=ax,
        textprops={"fontsize": 14},
        row_divider_kw={"linewidth": 1, "linestyle": (0, (1, 5))},
        col_label_divider_kw={"linewidth": 1, "linestyle": "-"},
        column_border_kw={"linewidth": 1, "linestyle": "-"},
    ).autoset_fontcolors(colnames=["Goals", "Assists"])    
    
    st.pyplot(fig)
    
    #fig.savefig("pl_standard.png", facecolor=ax.get_facecolor(), dpi=200)

if __name__ == "__main__":
    df = webScraper.pl_all("standard")    
    tableViz(df)
    





#st.write("Uber pickups in NYC")

# DATA_URL = 'D:\Study\scrape-bs\\'

# @st.cache_data
# def load_data(stat):
#     data = pd.read_csv(DATA_URL + stat)
#     return data

# def display_data(data):
#     # Create a text element and let the reader know the data is loading.
#     data_load_state = st.text('Loading data...')
#     # Notify the reader that the data was successfully loaded
#     data_load_state.text("Done! (using st.cache_data)")
#     st.subheader('Raw data')
#     st.dataframe(data,width = 1000)

# if 'clicked' not in st.session_state:
#     st.session_state.clicked = False

# def click_button():
#     st.session_state.clicked = True

# col1 , col2 = st.columns([0.2,0.8])

# with st.container():    
#     with col1:    
#         if st.button('Standard stats'#,on_click = click_button
#                      ):    
#             # Load 10,000 rows of data into the dataframe.
#             data = load_data('standard.csv')
#             with col2:
#                 display_data(data)
#         if st.button('Keeper stats'#,on_click = click_button
#                      ):
#             # Load 10,000 rows of data into the dataframe.
#             data = load_data('keeper.csv')
#             with col2:
#                 display_data(data)
#         if st.button('Passing stats'#,on_click = click_button
#                      ):
#             # Load 10,000 rows of data into the dataframe.
#             data = load_data('Passing.csv')
#             with col2:
#                 display_data(data)
#         if st.button('Possession stats'#,on_click = click_button
#                      ):
#             # Load 10,000 rows of data into the dataframe.
#             data = load_data('possession.csv')
#             with col2:
#                 display_data(data)
#         if st.button('Defense stats'#,on_click = click_button
#                      ):
#             # Load 10,000 rows of data into the dataframe.
#             data = load_data('Defense.csv')
#             with col2:
#                 display_data(data)
#         if st.button('Shot creating actions stats'#,on_click = click_button
#                      ):
#             # Load 10,000 rows of data into the dataframe.
#             data = load_data('gca.csv')
#             with col2:
#                 display_data(data)
