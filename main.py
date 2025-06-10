import streamlit as st

def main():
    st.title("Hello, Streamlit!")
    st.write("This is a basic example of a Streamlit app.")

    name = st.text_input("Enter your name:")
    if name:
        st.write(f"Hello, {name}!")

    if st.button("Say Hi"):
        st.success("Hi there! 👋")

if __name__ == "__main__":
    main()