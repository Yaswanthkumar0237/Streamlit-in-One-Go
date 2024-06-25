
import streamlit as st
st.title("Hello World, welcome")                     # Title
st.header("Header -> GeeksforGeeks")                 # header
st.subheader("subheader-> Geeksforgeeks")            # Subheader
st.text('Text -> Geeksforgeeks')                     # Text

st.markdown('Hi')                                    # Markdown
st.markdown('# Hi')
st.markdown("## Hi")
st.markdown("#### Hi")

st.success("Data is submitted")                      # Success
st.info('Information')                               # Info
st.warning("Warning")                                # Warning
st.error("Error")                                    # Error

exp=ZeroDivisionError('Division not possible with 0')
st.exception(exp)                                    # Exception
st.help(ZeroDivisionError)                           # Help

st.write('range(1,10)')                              # Write
st.write(range(1,10))
st.write("1+2+3")
st.write(1+2+3)

st.code('x = 10\n'                                   # Code                          
        'for i in range(x):\n'
              '\tprint(i)')

st.checkbox('Male')                                  # Checkbox
if(st.checkbox('female')):                           # Checkbox with Validation
    st.write("You are adult")

#st.radio('Select: ', ('Check','Uncheck','Other'))
radioButton = st.radio('Select: ', ('Male','Female','Others'))

if(radioButton == 'Male'):                           # Radio
    st.write("You are a Male")
elif(radioButton == 'Female'):
    st.write("You are a Female")
elif(radioButton == 'Others'):
    st.write("You are Others")

st.subheader('Select Box')                          # SelectBox
selectbox = st.selectbox("Data Science :", ["Data Analysis", 'Web Scraping','Machine Learning','Deep Learning','Natural Language Processing','Computer Vision',"Image Processing"])
st.write("You select: ", selectbox)

st.subheader('MultiSelect Box')
multiselect = st.multiselect("Data Science :", ['Data Analysis','Web Scarpping','Machine Learning','Deep Learning','Natural Language Processing','Computer Vision','Image Processing'])
st.write("You select: ",len(multiselect),"courses")

st.subheader('Button')                             # Button
if(st.button('Clickme')):
    st.write("Thanks for Clicking")

st.subheader('Slider')                             # Slider
vol = st.slider('Select the level',1,10,step=1)
st.write("Volume is: ",vol)

st.subheader('Text Input')                         # Text Input
username = st.text_input('Enter your name: ')
if (username):
    st.write('Your user name is ',username)
st.text_input("Password: ", type = 'password')

st.subheader('Text Area')                          # Text Area
st.text_area("write something in 20 Words",height =20)
st.write('text area')

st.subheader("Input Number")                          # Text Area
st.number_input("Select your age",18,20)

st.subheader("Input Date")
st.date_input("Date")

st.subheader("Input Time")
st.time_input("Time")



