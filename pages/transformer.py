import subprocess
import streamlit as st

sentence = st.text_input('English text')
st.write('The sentence you have typed is', sentence)
if sentence!="":
   # Construct the command
    command = ["python", "pages/model/inference.py", "--text", f"'{sentence}'", "-l", "hi", "-s"]
    
    # Run the command
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Capture the output and error messages
    output, error = process.communicate()
    
    # Display output and error
    st.write("Output:", output.decode())
    st.write("Error:", error.decode())
