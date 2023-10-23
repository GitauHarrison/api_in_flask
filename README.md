# APIs In Flask

Sample project used in the tutorial [Working With APIs In Flask](https://github.com/GitauHarrison/notes/blob/master/api_flask/00_overview.md):
- [API Blueprint](https://github.com/GitauHarrison/notes/blob/master/api_flask/01_api_blueprint.md)
- [Resource Representation](https://github.com/GitauHarrison/notes/blob/master/api_flask/02_resource_representation.md)
- [Error Handling](https://github.com/GitauHarrison/notes/blob/master/api_flask/03_error_handling.md)
- [Unique Resource Identifiers](https://github.com/GitauHarrison/notes/blob/master/api_flask/04_unique_resource_identifiers.md)
- [API Authentication](https://github.com/GitauHarrison/notes/blob/master/api_flask/05_api_authentication.md)
- [API-friendly Error Messages](https://github.com/GitauHarrison/notes/blob/master/api_flask/06_api_friendly_error_messages.md)
- [Testing API Using Postman](https://github.com/GitauHarrison/notes/blob/master/api_flask/07_api_testing_postman.md)


## Demo

Live app: [On render](https://api-in-flask.onrender.com)

## Test Locally

- Clone this repo:

    ```python
    $ git clone git@github.com:GitauHarrison/api_in_flask.git
    ```

- Change directory into the cloned directory

    ```python
    $ cd api_in_flask
    ```

- Create and activate a virtual environment
    ```python
    $ python3 -m venv venv
    $ source venv/bin/activate

    # Or
    $ mkvirtualenv venv
    ```

- Install dependancies
    ```python
    (venv)$ pip3 install -r requirements.txt
    ```

- Update needed environment variables
    ```python
    (venv)$ cp .env-template .env
    ```
    - Remember to add your values in `.env`
- Start the flask server
    ```python
    (venv)$ flask run
    ```
- Paste the link http://localhost:5000 on your browser to see the application