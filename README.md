# Weather App

This is a Flask-based web application that provides weather information based on location. The application utilizes the OpenWeatherMap API to retrieve weather data.

## Features

- **Weather Functionality**: The app includes a `weather` function that fetches the current weather status for a given location using the OpenWeatherMap API.

## Installation

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/Hdknife/weather--status.git
    ```

2. Navigate to the project directory:

    ```
    cd weather-app
    ```

3. Install the required dependencies:
   Flask, Requests
    ```

## Usage

1. Obtain an API key from OpenWeatherMap by signing up on their website: https://home.openweathermap.org/users/sign_up

2. Set your API key as an environment variable named `WEATHER_API_KEY`. You can do this by creating a `.env` file in the project directory and adding the following line:

    ```
    WEATHER_API_KEY=your_api_key_here
    ```

3. Run the Flask application:

    ```
    flask run
    ```

4. Access the Weather App in your web browser at `http://127.0.0.1:5000`.

5. Enter the desired location in the input field and click the "Search" button to view the current weather status for that location.

## Deactivation of API Key

Please note that the API key used in this application is private and should be kept confidential. If you encounter any issues with the weather data retrieval, it may be due to invalid or deactivated API key.



