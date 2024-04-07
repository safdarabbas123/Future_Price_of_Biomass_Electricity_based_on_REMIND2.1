# -*- coding: utf-8 -*-
"""
Created on Sunday Apr 7 2024

@author: sabbas
"""
import pyam

# Load the data
df = pyam.IamDataFrame(data="AR6_Scenarios_Database_R5_regions_v1.1.csv")

# Display the dataframe
print(df)

# Access model, scenario, region, and unit mapping information
print(df.model)
print(df.scenario)
print(df.region)
print(df.unit_mapping)

# Filter dataframe by model and scenario
print(df.filter(model="REMIND 2.1").scenario)

# Filter out a specific region
print(df.filter(region="World", keep=False).region)

# Filter and display timeseries data
display_df = df.filter(model="REMIND 2.1*", variable="Price|Secondary Energy|Electricity", region="R5OECD90+EU")
print(display_df.timeseries())

# Filter timeseries data for specific years
print(display_df.filter(year=[2010, 2030, 2050]).timeseries())

# Filter dataframe by additional scenarios
additional_scenarios = ["R2p1_SSP2-Base", "R2p1_SSP2-PkBudg1100", "R2p1_SSP2-PkBudg900"]
display_df = df.filter(model="REMIND 2.1*", variable="Price|Secondary Energy|Electricity",
                       scenario=additional_scenarios, region="R5OECD90+EU")
print(display_df.timeseries())

# Filter timeseries data for specific years with additional scenarios
print(display_df.filter(year=[2030, 2040, 2050]).timeseries())

# Plot timeseries data with multiple scenarios
df.filter(model="REMIND 2.1*", variable="Price|Secondary Energy|Electricity",
          scenario=additional_scenarios, region="R5OECD90+EU").plot(color="scenario")

# Filter and display timeseries data for primary energy biomass
display_df = df.filter(model="REMIND 2.1*", variable="Price|Primary Energy|Biomass",
                       scenario=additional_scenarios, region="R5OECD90+EU")
print(display_df.timeseries())

# Filter timeseries data for specific years with primary energy biomass
print(display_df.filter(year=[2030, 2040, 2050]).timeseries())

