This is a web scraper for live cases of Coronavirus worldwide. 
The site used for data scraping is: https://www.worldometers.info/

Clone de project:
$ git close https://github.com/alexandrusava/COVID-19-Web-Scraper.git

Prerequisites:
1. Name your folder

2. In that folder, use the following command to create a virtual environment named scraper based on your current interpreter:
# macOS/Linux
sudo apt-get install python3-venv    # If needed
python3 -m venv scraper
# Windows
python -m venv scraper

3. Install flask framework:
# macOS/Linux
pip3 install flask
# Windows
pip install flask

4. Run the project: 
# port 5000 by default
python -m flask run 
# your port
python -m flask run --port #typeyourport
