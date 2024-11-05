import streamlit as st

#text
tab1, tab2 , tab3 = st.tabs(["Basic Components","Basic Data Vis","Date & Time"])  

with tab1:
   st.markdown("# Basic Components")
   
   st.header("Learn")
   st.text("Learn")
   st.caption("Learn")
   st.code("Learn")
   st.write("Learn!")

   # hyperlink
   st.markdown("[Wikipedia](https://www.wikipedia.org/)")

   #show the actual URL
   st.markdown("https://www.wikipedia.org/")

   # simple HTML block
   # this will go into a st.markdown function which shows it
   html_page = """
   <h4>Simple HTML</h4>
   <div style = "background-color:blue;padding:50px">
   <p style = "color:white; font-size:50px"> Color </p>
   </div>
   """
   st.markdown(html_page, unsafe_allow_html= True)
   st.divider()
   st.success("Success!")
   st.error("Failed.")
   st.warning("Are you sure")
   st.info("Not a big deal.")

   from PIL import Image
   img = Image.open("Jurong_East_MRT_station_230622.jpg")
   st.image(img)
   st.caption("mass transit in Singapore.")

   st.button("Play", key = "play_1") # nothing happen unless...

   if st.button("Play", key = "play_2"):
      st.text("Ha! Nothing to play here:p")
      
   if st.checkbox("Checkbox"):
      st.text("selected, stop clicking it")
      
   radio_button = st.radio("Select one of these: Would you like to be a ...",["one who is with kindness", "one who reads and thinks"])
   if radio_button == "one who is with kindness":
      st.info("You then have to learn to think in other people shoes. It doesn't mean you should be a people pleaser.")
   else:
      st.info("You have critical thinking skills and a gentle heart. The hidden gem at the corner of humanity.")


   city = st.selectbox(
      "Which city do you like to live in?",
      ["Pewter City", "Serious City", "Smart City"]
   )

   if city == "Pewter City":
      st.info("You have a pure, untainted heart.")
   elif city == "Serious City":
      st.info("Your seriousness will one day lead to greatness.")
   else:
      st.info("You must be wearing wearables all over your bodies.")

   animal = st.text_input("What's your favorite animal?","e.g. a freed hippo?")
   st.text(animal)

   age = st.number_input("Your age?")

   occupation = st.multiselect("Your Occupation",
                               ["Programmer",
                               "Data Scientist",
                               "Data Analyst",
                               "IT Consultant",
                               "DBA"]
                               )
   name = st.text_input("Hello","Please write what you want...")
   st.text(name)
   
   message = st.text_area("Your Message", "...")
   
   select_val =st.slider("Select a Value", 1, 10)
   
   if st.button("Balloons"):
      st.balloons()
      
   if st.button("Completed"):
      st.balloons()
   
with tab2:
   st.markdown("# Basic Data Vis Skill")
   import pandas as pd
   df = pd.read_csv('auto.csv')
   st.dataframe(df.head(10))
   
   st.write("what if it's a table?")
   st.table(df.head(10))
   
   st.area_chart(df[["mpg","cylinders"]])
   st.caption("This is an area chart.")
   
   st.bar_chart(df[["mpg","cylinders"]].head(20))
   st.caption("This is a bar chart.")
   
   st.line_chart(df[["mpg","cylinders"]])
   st.caption("This is line chart.")
   
   import matplotlib.pyplot as plt
   import seaborn as sns
   
   fig, ax =plt.subplots()
   corr_plot= sns.heatmap(df[["mpg","cylinders","displacement"]].corr(), annot = True)
   ax.set_title('Correlation Heatmap of 3 variables')
   st.pyplot(fig)
   
with tab3:
   st.markdown("# Date, time, and more ")
   import datetime
   today = st.date_input("Today is", datetime.datetime.now())
   import time
   hour = st.time_input("The time is", datetime.time(12,30))
   
   data = {"key_1":"value_1", "key_2":"value_2"}
   st.json(data)
   
   st.code("""
           def example(code):
              return code
           """, language= 'python')
   
   my_bar = st.progress(0)
   for val in range(100):
      time.sleep(0.01)
      my_bar.progress(val + 1)
      
   with st.spinner("Working on it ..."):
      time.sleep(2)
   st.success("There!")