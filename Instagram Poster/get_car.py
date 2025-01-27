# Imports
import re
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Get API key and configure Gemini AI
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-pro")  # use gemini-1.5.pro

# Send prompt to Gemini - then extract details from its response
def generate_car():
    
    # Load a list with all cars in existing_cars.txt
    with open("existing_cars.txt", "r") as file:
        already_used_cars = file.read().splitlines()  

    # Send prompt to Gemini
    prompt = f"""
    Pick a random car. Make is somewhat interesting. Do not repeat any car that has been used before in previous prompts. do something exotic or unique, or a limited special edition
    Provide a very brief 1-sentence title about this car, describing it in an interesting way. Only do this once. I need 1 title and car only. 
    Make sure the title is unique. Heres some cars that have already been generated: {already_used_cars}. Do not use these, use something unique to them
    After that, specify the car make, model, and year. And at the end give a summary in around 5 sentences. in the following format:

    Title: [brief description of the car]Car: [Car make, model, year]Caption: [summary]
    """

    try:

        # Hardcoded prompt for debugging
        # response = ("Title: This is a sample title.0s.\nCar: Ferrari LaFerrari")

        # Extract text response
        response = model.generate_content(prompt).text.strip()\

        # Print response to terminal
        print("-----------------------------------------------------\nFull AI Response:")
        print(response)

        # Clean response and extract title, car info, and caption
        response = response.strip()
        title = extract_field(response, "Title")
        car_info = extract_field(response, "Car")
        caption = extract_field(response, "Caption")

        # Print extracted title, car info, and caption to terminal
        print(f"\nExtracted Title: {title}")
        print(f"Extracted Car Info: {car_info}")
        print(f"Extracted Caption: {caption}\n")

        # Load a list with all cars in existing_cars.txt
        with open("existing_cars.txt", "r") as file:
            existing_cars = file.read().splitlines()  

        # If the car exists in list, exit program
        if car_info in existing_cars:
            print("Already Used Before...\n-----------------------------------------------------")
            exit()

        # Continue if car is not in list
        else:
            print("Hasnt Been Used Before!")

            # Add new generated car to list
            existing_cars.append(car_info)
            with open("existing_cars.txt", "w") as file:
                file.write("\n".join(existing_cars))

            return title, car_info, caption

    # Error handling in case of blunder
    except Exception as e:
        print(f"Error while generating content: {e}")
        return "Error", "Unknown Car"

# Extracts the value of specific fields from response based on the specified prompt format
def extract_field(response, field_name):

    match = re.search(rf"{field_name}:\s*(.+)", response)

    if match:
        return match.group(1).strip()  # Strip extra spaces if any
    
    # Error handling
    else:
        print(f"Field '{field_name}' not found in response.")
        return f"Unknown {field_name}"
