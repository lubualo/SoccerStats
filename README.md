---

# **SoccerStats: Your Go-To Soccer Data Parsing and Analysis Tool** ⚽

Welcome to **SoccerStats**, a powerful tool for fetching, parsing, and exporting soccer data from APIs into structured formats. Whether you're a soccer enthusiast, analyst, or developer, SoccerStats makes it easy to work with detailed soccer statistics. This project is carefully designed with clean code, object-oriented programming principles, and robust data processing to ensure reliability and ease of use.

---

## **Features**
- Fetch soccer league, team, and game data from APIs (compatible with Promiedos website).
- Parse the JSON data into structured Python objects using custom models.
- Export data into **CSV files** for further analysis:
  - Teams
  - Team statistics by table groups
  - Games
- Built with **OOP principles** for modular, maintainable, and extensible code.
- Handles unplayed games, missing data, and edge cases gracefully.
- Single-click usability with `.exe` generation for seamless distribution.

---

## **Installation**
Follow these steps to set up SoccerStats:

### **1. Clone the Repository**
```bash
git clone https://github.com/lubualo/SoccerStats.git
cd SoccerStats
```

### **2. Set Up Dependencies**
Ensure you have Python 3.10+ installed. Then install the required dependencies:
```bash
pip install -r requirements.txt
```

### **3. Configure the Environment**
Create a `.env` file in the root directory with the following variables:
```plaintext
API_GAMES_URL=<API_URL>
API_TABLES_AND_FIXTURES_URL=<API_URL_FOR_FIXTURE>
```

### **4. Run the Application**
To run the application directly:
```bash
python main.py
```

---

## **How to Use the Executable**
If you want a portable version of the app for distribution:
1. Build the `.exe` using PyInstaller:
   ```bash
   pyinstaller --onefile --add-data ".env;." main.py
   ```
2. Share the `.exe` file. The `.env` file is already bundled for convenience.

---

## **Project Structure**
Here's an overview of the SoccerStats project structure:

```plaintext
SoccerStats/
│
├── models/                  # Python models for League, Team, TeamStats, Game, etc.
│   ├── league.py
│   ├── team.py
│   ├── team_stats.py
│   ├── game.py
│   └── match_result_type.py
│
├── service/                 # Helper services for parsing and exporting
│   ├── json_parser.py       # Parses JSON data into models
│   ├── export_service.py    # Exports data to CSV files
│
├── main.py                  # Main script to execute the application
├── requirements.txt         # Python dependencies
└── .env                     # Environment configuration
```

---

## **Examples**
### **1. Fetch and Parse Data**
- Fetch league details and team statistics from the provided API URLs.
- Parse the data into structured models for easy access.

### **2. Export to CSV**
SoccerStats exports the following CSV files:
- **`<league_name>_teams.csv`**: Details of all teams in the league.
- **`<league_name>_<table_name>_teams_stats.csv`**: Team statistics categorized by table groups (e.g., Apertura, Clausura).
- **`<league_name>_games.csv`**: Comprehensive game data, including played and unplayed games.

---

## **Technical Highlights**
- **Object-Oriented Design**:
  - The codebase is modular, adhering to OOP principles for clean, reusable, and extendable logic.
- **Error Handling**:
  - Gracefully handles unplayed games (`Prog.` status), missing data, and other edge cases.
- **Export Service**:
  - Uses Python’s `csv` module to generate structured, clean, and human-readable CSV outputs.
- **PyInstaller Integration**:
  - Distribute the app as a portable `.exe` with the `.env` file bundled for convenience.

---

## **Future Enhancements**
- Add support for additional leagues and APIs.
- Create a Graphical User Interface (GUI) for improved usability.
- Add data visualization features for team or game statistics.
- Introduce support for database storage (e.g., SQLite or PostgreSQL).

---

## **Contributions**
Contributions, issues, and feature requests are welcome! Please feel free to open a pull request or issue on the repository.
