import streamlit as st

def hello_world():
    return "Oi docker, sumido 123"

def main():
    st.write(hello_world())

if __name__ == "__main__":
    main()

