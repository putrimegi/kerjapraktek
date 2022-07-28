import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
Web App URL: <https://template.streamlitapp.com>
GitHub Repository: <https://github.com/giswqs/streamlit-multipage-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Marker Cluster")

# with st.expander("See source code"):
#     with st.echo():

#          m = leafmap.Map(center=[40, -100], zoom=4)
# #         cities = 'https://github.com/putrimegi/kerjapraktek/blob/5cbd738e3c96e0b89fe2f8cb8357838fa24845ee/Titik%20Lokasi%20Kalimantan.csv'
# #         #regions = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_regions.geojson'

# #         #m.add_geojson(regions, layer_name='US Regions')
# #         m.add_points_from_xy(
# #             cities,
# #             x="Longitude",
# #             y="Latitude",
# #             color_column='Type',
# #             icon_names=['gear', 'map'],
# #             spin=True,
# #             add_legend=True,
# #         )
        
#  m.to_streamlit(height=700)
