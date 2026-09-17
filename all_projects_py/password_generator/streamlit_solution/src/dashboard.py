import streamlit as st

from src.password_generator import (
    MemorablePasswordGenerator,
    PinGenerator,
    RandomPasswordGenerator,
)

st.image('https://cdn-icons-png.flaticon.com/256/11817/11817723.png', width=200)
st.title(":zap: Password Generator")


option = st.radio(
    "Select the type of password you want to generate:",
    ("Random Password", "Memorable Password", "PIN")
)

if option == 'PIN':
    length = st.slider("Select the length of the PIN:", 4, 12, 4)
    generator = PinGenerator(length)
    password = generator.generate()
    st.write(f"Your PIN is: `{password}`")

elif option == 'Random Password':
    length = st.slider("Select the length of the password:", 8, 32, 8)
    include_numbers = st.toggle("Include numbers?")
    include_symbols = st.toggle("Include symbols?")
    generator = RandomPasswordGenerator(
        length=length,
        include_numbers=include_numbers,
        include_symbols=include_symbols
    )

    password = generator.generate()
    st.write(f"Your password is: `{password}`")

elif option == 'Memorable Password':
    num_of_words = st.slider("Select the number of words:", 4, 8, 4)
    separator = st.text_input("Enter the separator:", "-")
    capitalization = st.toggle("Capitalize the first letter of each word?")
    generator = MemorablePasswordGenerator(
        num_of_words=num_of_words,
        separator=separator,
        capitalization=capitalization,
    )

    password = generator.generate()
    st.write(f"Your password is: `{password}`")
