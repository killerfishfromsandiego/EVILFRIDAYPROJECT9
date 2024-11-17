import tkinter as tk
import openai
from tkinter import messagebox
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()  # Load the environment variables from the .env file

# Get the API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")  # Ensure this matches the variable in your .env

# Check if the API key is loaded
if openai.api_key is None:
    messagebox.showerror("API Error", "API key not found! Please check your .env file.")
    raise Exception("API key not found")

# Function to handle the API call and display the response
def generate_completion():
    prompt = prompt_entry.get("1.0", tk.END).strip()  # Get text from the prompt text box
    if not prompt:
        messagebox.showwarning("Input Error", "Please enter a prompt.")
        return
    
    try:
        # Call OpenAI API to get the completion (Updated method using ChatCompletion)
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # You can switch this to gpt-4 if you have access
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        
        # Clear previous output and display the new response
        output_text.delete(1.0, tk.END)  
        output_text.insert(tk.END, response['choices'][0]['message']['content'].strip())
    except Exception as e:
        messagebox.showerror("API Error", f"Error contacting OpenAI API: {str(e)}")

# Set up the main window
root = tk.Tk()
root.title("OpenAI Completion GUI")

# Set window size for a better appearance
root.geometry("500x500")  # Set an appropriate window size (adjust as needed)

# Instruction Label
instruction_label = tk.Label(root, text="Enter your prompt and click 'Submit' to get a completion.")
instruction_label.pack(padx=10, pady=10)

# Text box for the user to input the prompt
prompt_entry = tk.Text(root, height=5, width=50)  # Adjust width for better readability
prompt_entry.pack(padx=10, pady=10)

# Submit button
submit_button = tk.Button(root, text="Submit", command=generate_completion)
submit_button.pack(pady=10)

# Output box to display the generated text
output_text = tk.Text(root, height=10, width=50)  # Adjust width for better readability
output_text.pack(padx=10, pady=10)

# Run the main loop to display the GUI
root.mainloop()
