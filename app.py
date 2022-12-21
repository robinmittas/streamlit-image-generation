import streamlit as st
import openai
import yaml

# get API key
with open("env_vars.yaml", encoding='utf8') as conf:
  config = yaml.load(conf, Loader=yaml.FullLoader)
  conf.close()
openai.api_key = config["open_ai_api_key"]

st.set_page_config(layout="wide")

# Webpage Title
st.title('Image Generation Tool')

# Add input field
text = st.text_input(label="Input some Text")

# define number of returned images
n = 3

# define some big-font
st.markdown("""<style>.big-font {font-size:50px !important;}</style>""", unsafe_allow_html=True)

st.sidebar.image("./logo.png")

# check if text is inputed, if so get results
if text != "":
  response = openai.Image.create(
    prompt=text,
    n=n,
    size="1024x1024"
  )
  image_urls = [data['url'] for data in response['data']]
  # add some text
  st.markdown('<p class="big-font">Suggested Images :)</p>', unsafe_allow_html=True)

  for i in range(n):
    st.image(image_urls[i], width=800)

#  st.markdown(f"<h1 style='text-align: center;>![Alt Text]({image_urls[0]})</h1>")
#  st.markdown("<h1 style='text-align: center; color: grey;'>Big headline</h1>", unsafe_allow_html=True)
else:
  st.markdown('<p class="big-font">Waiting for some input! :)</p>', unsafe_allow_html=True)


# https://discuss.streamlit.io/t/streamlit-footer/12181/3
footer = """<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: right;
}
</style>
<div class="footer">
<p>Developed by <a style='display: block; text-align: right;' href="https://www.linkedin.com/in/robin-mittas-a29a11201/" target="_blank">Robin Mittas</a></p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)


