# Imports
from get_car import generate_car
from get_image import get_car_image_bing
from publish_pic import post_to_instagram
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Create html using pre-made template
def generate_html(title, image_url):

    # Read the template HTML file
    with open('template.html', 'r') as file:
        html_template = file.read()

    # Replace placeholders with generated content
    html_content = html_template.replace('{{ title }}', title).replace('{{ image_url }}', image_url)

    # Save the edited HTML to new file
    with open('car_news.html', 'w') as file:
        file.write(html_content)

    print("\nHTML file 'car_news.html' has been generated.")

    return 'car_news.html'

# Screenshot the generated html and save as png
def generate_image_from_html(html_file, car_info):
    
    # Set up Chrome winddow to run headless in background
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=1200x800")

    # Automatically download and install ChromeDriver
    service = Service(ChromeDriverManager().install())  # Set up the service
    driver = webdriver.Chrome(service=service, options=options)

    # Set file path to generated html
    input_html_file = 'file:///C:/PATH_TO_GENERATED_HTML'  # Update this path

    # Load html and take a screenshot as png
    driver.get(input_html_file)
    time.sleep(2)
    screenshot_path = f'C:/PATH_TO_GENERATED_PIC'  # Update this path
    driver.save_screenshot(screenshot_path)

    # Close chrome window
    driver.quit()
    print(f"Your HTML has been converted and saved as {screenshot_path}.")

# Main function to run entire project
def main():

    # Generate info to be used in car post
    news_title, car_name, caption = generate_car()
    
    if car_name != "Unknown Car":

        # Get image using generated car name
        image_url = get_car_image_bing(car_name)
        
        print(f"\nImage credit: {image_url}")
            
        # Generate html file with title and image URL
        html_file = generate_html(news_title, image_url)
        
        # Generate png image from html file
        generate_image_from_html(html_file, car_name)

        # Post pic to instegram
        username = os.getenv("USER")
        password = os.getenv("PASSWORD")
        image_path = f'C:/PATH_TO_GENERATED_PIC' # Update this path
        ig_caption = f"{caption} \n\nPic Credit: {image_url}\n\n#replace #these #hashtags" # Update caption accordingly
        post_to_instagram(username, password, image_path, ig_caption)
            
    else:
        print("No valid car name extracted.")

if __name__ == "__main__":
    main()
