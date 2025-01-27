
## :information_source: Overview

The Instagram Poster AI Agent will generate a topic, source an image related to the topic, add a title to this image, and generate a caption which will all be combined and uploaded to Instagram. The use case here is for an automotive themed Instagram account posting about cars. The code is modular and can be edited to work with any topic such as tech, finance, world affairs, or any other niche. 

## :book: How it works

- The program is run using ```main```. A prepared prompt is sent to Google Gemini AI in which it is instructed to choose a car and generate a breif title for the image. It also generates a longer caption which describes the car. A list of already used topics is stored in ```existing_cars.txt``` and is also sent to Gemini so that no repeats are generated.
- Gemini is instructed to reply in a specified format, so that fields for the car name, image title, and caption can be easily extracted.
- The extracted car name is sent to Bing Image Search which sources an image related to the given field, and returns a text URL. 
- The car name, image title, and image URL are inserted into a pre made  ```template.html``` which contains placeholders for each of these fields. 
- A properly formated HTML file is generated as ```car_news.html```. This generated HTML file is opened using WebDriver in a background window where it is screenshotted and saved as a .PNG image file. 
- Instagrapi is used to log into an Instagram account and upload this image along with the previously generated caption. 

Editing the Gemini prompt to replace car name, title, and caption with any other topic will provide the same results. 

## :arrow_down_small: Installation

Install `Instagram Poster` and run `main.py`

To run tests, install the following packages:



```bash
pip install python-dotenv
```
```bash
pip install google.generativeai
```
```bash
pip install requests
```
```bash
pip install selenium
```
```bash
pip install webdriver-manager
```
```bash
pip install instagrapi
```


## :key: Environment Variables

Obtain a Google Gemini API key from https://ai.google.dev/

Create a resource on Microsoft Azure Portal for `Bing Search v7` and get API key

To run this project, you will need to assign your API keys to the `GEMINI_API_KEY` and ` BING_API_KEY`, as well as update Instagram `USER` and `PASSWORD` environment variables in `.env`
