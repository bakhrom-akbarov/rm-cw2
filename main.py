import pandas as pd
import plotly.express as px

# Load the dataset
data = pd.read_csv('./Results_21Mar2022.csv')

# Prepare data by selecting relevant columns
columns_to_visualize = ['sex', 'age_group', 'diet_group', 'mean_ghgs', 'mean_land', 'mean_watscar', 'mean_eut', 'mean_bio']
filtered_data = data[columns_to_visualize]

# Convert 'diet_group' from categorical text to categorical codes for color mapping
filtered_data['diet_group_codes'] = filtered_data['diet_group'].astype('category').cat.codes

# Create a parallel coordinates plot using the numeric codes for colors and a continuous colorscale
fig = px.parallel_coordinates(filtered_data, color='diet_group_codes',
                              labels={
                                  'mean_ghgs': 'GHG Emissions (kg)',
                                  'mean_land': 'Land Use (sq meters)',
                                  'mean_watscar': 'Water Scarcity',
                                  'mean_eut': 'Eutrophication (gPO4e)',
                                  'mean_bio': 'Biodiversity Impact (species/day)'
                              },
                              color_continuous_scale=px.colors.diverging.Tealrose)

# Display the plot
fig.show()
