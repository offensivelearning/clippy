import requests
import pyperclip

def get_data_from_api(number):
    # Placeholder API URL
    api_url = f"http://clippy.offensivelearning.com/id/{number}"
    
    # Make a GET request to the API
    response = requests.get(api_url)


    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.text.strip()  # Get the response content
        
        # Copy the data to the clipboard
        pyperclip.copy(data)
        
        print("Data copied to clipboard.")
    else:
        print("Failed to retrieve data from the API.")
    
    """
    pyperclip.copy("Testy")
    print("Data copied to clipboard.")
    """

user_input = input("Enter a number: ")
get_data_from_api(user_input)
