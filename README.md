# Workout-Tracker

## Overview

**Workout-Tracker** is a Python application that allows users to log their workouts and track their exercise routines. By inputting the exercises performed, the application retrieves exercise data such as duration and calories burned, then logs this information into a Google Sheet for easy tracking and analysis.

## Features
```markdown
- Logs workouts by retrieving exercise details via the Nutritionix API.
- Records the date, time, exercise type, duration, and calories burned.
- Integrates with Google Sheets to store workout data for easy access and analysis.
```
## Requirements
```markdown
- Python 3.6 or higher
- `requests` library for making HTTP requests
- Environment variables for sensitive data
```
## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/BTAG16/Workout-Tracker.git
   cd Workout-Tracker
   ```

2. **Install the required libraries:**

   You can use pip to install the necessary packages:

   ```bash
   pip install requests
   ```

3. **Set up your Nutritionix account:**

   - Sign up at [Nutritionix](https://developer.nutritionix.com/) and create a new application to get your `APP_ID` and `API_KEY`.

4. **Set up your Google Sheets API:**

   - Create a Google Sheet to log your workouts.
   - Use the [Sheety API](https://sheety.co/) to interact with Google Sheets. Set up a project in Sheety and get your `SHEETY_API` and `SHEETY_AUTH` credentials.

5. **Create a `.env` file:**

   In the root of your project directory, create a file named `.env` and add the following lines, replacing the placeholders with your actual credentials:

   ```env
   APP_ID=your_app_id
   API_KEY=your_api_key
   SHEETY_API=your_sheety_api
   SHEETY_AUTH=your_sheety_auth
   ```

## Usage

1. Run the application:

   ```bash
   python main.py
   ```

2. When prompted, enter the exercises you performed. For example:

   ```
   Tell me which exercises you did: running, cycling, weight lifting
   ```

3. The application will log the date, time, exercise type, duration, and calories burned into your Google Sheet.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request. Any contributions are welcome!

## Acknowledgments

- [Nutritionix API](https://developer.nutritionix.com/)
- [Sheety API](https://sheety.co/)
- [Requests library](https://docs.python-requests.org/en/master/)

## Contact

For any questions or feedback, feel free to open an issue on the repository or contact me at [rumeighoraye@gmail.com] or [LinkedIn](https://www.linkedin.com/in/cosmos-junior-ighoraye-4a8109239/).

