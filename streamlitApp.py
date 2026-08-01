import streamlit as st

st.title("What on your mind today?")
input_text = st.text_input("Ask anything")


#conditional logic with widgets

name = st.text_input("Enter your name:")
if st.button("Great"):
    st.success(f"Hello, {name}!")

st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("**Bold**, *Italic*, 'Code', [Link](https://streamlit.io)")

st.text_input("what is your name?")
st.text_area("Write something...")
st.number_input("Pick a number", min_value=0, max_value=100)
st.slider("choose a range, o, 100")
st.selectbox("Select a fruit", ["Apple", "Banana", "Mango"])
st.multiselect("choose toppings", ["cheeze", "Tomato", "olives"])
st.radio("Pick one", ["Option A", "Option B"])
st.checkbox("I agree to the terms")

if st.checkbox("Show Details"):
    st.info("Here are more details...")


option = st.radio("Choose view", ["Show Chart", "Show Table"])
if option == "Show Chart":
    st.write("Chart would appear here")
else:
    st.write("Table would appear here")

with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")

    if submitted:
            st.success(f"Welcome, [username]!")


st.image("https://www.gq.com/story/captain-america-civil-war-trailer-spider-man-reveal", caption="Sample Image", width=True)

st.video("https://youtu.be/5IJycI1VJMI?si=aHBvwrwqtJ81pST7")