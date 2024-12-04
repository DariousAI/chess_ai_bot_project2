# Chess AI Bot Project

## Project Overview
This project is a Chess AI Bot built using Python. The goal of the bot is to play chess autonomously, using artificial intelligence techniques to make strategic moves. The project can be interacted with via a user interface that allows users to play against the bot.

## Features
- Play chess against an AI bot that makes strategic moves.
- User-friendly interface built with `Streamlit` for easy interaction.
- The AI uses a combination of basic chess heuristics and decision-making algorithms to determine the best moves.

## Requirements
To run this project, you need to have the following installed:
- Python 3.x
- Required Python libraries (listed in `requirements.txt`)

To install the required libraries, run:
```sh
pip install -r requirements.txt
```

## Project Structure
```
chess_ai_bot_project2/
│
├── .streamlit/             # Configuration for Streamlit
├── assets/                 # Assets like images and other resources
├── helpers/                # Helper functions and utilities for the bot
├── vcpkg/                  # Dependencies manager for C++ libraries (if needed)
├── chess_ai_bot.py         # Main Python script for the Chess AI Bot
└── requirements.txt        # Python dependencies for the project
```

## Usage
1. Clone this repository to your local machine:
   ```sh
   git clone https://github.com/YourUsername/chess_ai_bot_project2.git
   ```

2. Navigate to the project directory:
   ```sh
   cd chess_ai_bot_project2
   ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the bot using Streamlit:
   ```sh
   streamlit run chess_ai_bot.py
   ```

## How It Works
- The bot is designed to make strategic chess moves using a set of heuristics and algorithms.
- The `Streamlit` interface allows users to play against the bot interactively, viewing the moves made by both players.

## Contributing
Feel free to fork this repository and make your own changes. Pull requests are welcome if you have improvements to suggest.

## License
This project is open source and available under the [MIT License](LICENSE).

