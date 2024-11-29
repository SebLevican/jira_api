# jira_api
Overview

This project provides a Python-based integration with the Jira API, enabling efficient interaction with Jira issues and projects. The tool automates data retrieval and manipulation, offering features like fetching issue details, analyzing project data, and generating reports.
Features

    Retrieve Issues: Fetch detailed issue information using the Jira API.
    Project Analysis: Gather data on project status, priorities, and deadlines.
    Reporting: Generate custom reports for team productivity and progress tracking.

Installation

    Clone the repository:

git clone https://github.com/SebLevican/jira_api.git  
cd jira_api  

Create a virtual environment (optional but recommended):

python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  

Install the required dependencies:

    pip install -r requirements.txt  

Configuration

    Obtain a Jira API token and ensure you have the correct Jira base URL.
    Create a .env file in the project root directory with the following variables:

    JIRA_BASE_URL=<your-jira-base-url>  
    JIRA_API_TOKEN=<your-api-token>  
    JIRA_EMAIL=<your-email>  

Usage
Running the Script

    Ensure your environment is activated.
    Run the main script to interact with the Jira API:

    python main.py  

Examples

    Fetch All Issues: Retrieve all issues for a specified project.
    Generate Reports: Create an overview of team progress and issue priorities.

File Structure

jira_api/  
│  
├── main.py              # Entry point of the project  
├── utils/               # Utility functions for API interaction  
│   └── jira_client.py   # Wrapper for Jira API requests  
├── reports/             # Scripts for generating reports  
│   └── report_generator.py  
├── requirements.txt     # Python dependencies  
└── README.md            # Project documentation  

Dependencies

    requests: Simplifies HTTP requests for interacting with the Jira API.
    python-dotenv: Manages environment variables securely.

Contributing

Contributions are welcome!

    Fork the repository.
    Create a new branch:

    git checkout -b feature-name  

    Commit your changes and push to the branch.
    Open a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for more details.
Contact

For questions or suggestions, feel free to reach out via LinkedIn or raise an issue on this repository.
