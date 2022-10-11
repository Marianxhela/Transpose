#!/usr/bin/env python
# coding: utf-8


import pandas as pd


def add_optimised_cash_flow(input_file):
    data = pd.read_excel(input_file, sheet_name='Cash Flow', header=None)

    df = pd.DataFrame(data)
    df = df.iloc[7:]
    df.dropna(axis=1, how="all", inplace=True)
    df.dropna(axis=0, how='all', inplace=True)
    with pd.ExcelWriter(input_file, mode="a", if_sheet_exists='replace',
                        engine="openpyxl") as writer:
        df.T.to_excel(writer, sheet_name="Optimised Cash Flow")
