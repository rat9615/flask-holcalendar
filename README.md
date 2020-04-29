# flask-holcalendar
A simple **Holiday Calendar** web application written using [Flask](https://flask.palletsprojects.com/). The application uses [Google Sheets](https://sheets.google.com) as the back-end to get information pertaining to the holiday calendars of offices.

[Flask](https://flask.palletsprojects.com/) is used as the web framework for building the application. [HTML](), [CSS]() and [jQuery](https://jquery.com/) is used for front-end development.

## Demo
![Imgur](https://i.imgur.com/23FustR.gif)

## Built With
- [Python](https://www.python.org)
- [Flask](https://flask.palletsprojects.com)
- [Bootstrap4](https://getbootstrap.com/)
- [jQuery](https://jquery.com/)
- [jQuery-flexdatalist-2.2.4](http://projects.sergiodinislopes.pt/flexdatalist/)

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
### Prerequisites
- Create the **Google Sheets** API key from [here](https://developers.google.com/sheets/api/quickstart/python).
- Download the *credentials.json* file and keep it aside.
### Installation
- Clone the repo: ```git clone https://github.com/rat9615/flask-holcalendar.git```.
- Change directory:```cd flask-holcalendar```.
- Create a folder called ```google_api_client_keys``` in the root directory : ```mkdir google_api_client_keys```.
- Move the ```credentials.json``` file to ```google_api_client_keys``` directory.
- A sample excel sheet consisting of various holiday calendars for offices is kept in the ```sample``` folder. Add it to your Google Sheets (Spreadsheet).
- Obtain the [spreadsheetID](https://developers.google.com/sheets/api/guides/concepts) and add it to the ```sheet_id``` variable in ```contojson.py``` and ```holiday.py``` scripts.
- Type ``` pip install -r requirements.txt ``` in your terminal.
### Run
After installation type the following command in your terminal to run the application.\
```python routes.py```
## Note 
If you want to *send email* through the Contact Us form, make sure you have entered all the required credentials in the scripts.
