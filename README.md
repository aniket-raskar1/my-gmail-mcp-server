Gmail MCP Server
Gmail MCP Server is a Python-based package that seamlessly integrates Gmail and Google Calendar with Claude Desktop, an AI-powered productivity tool. This server enables users to interact with their Gmail inbox and Google Calendar through natural language commands, streamlining email management and event scheduling. With features like email summarization, sending emails, and automatic calendar event creation for important emails, it enhances productivity by combining AI capabilities with Google’s ecosystem.
What This Project Does
The Gmail MCP Server runs as a background server that connects to Gmail and Google Calendar APIs via an MCP (Message Control Protocol) interface. It allows Claude Desktop to process commands for:

Email Summarization: Generate concise summaries of recent emails, optionally filtered by sender or label.
Email Sending: Send emails directly from Claude Desktop with customizable recipients, subjects, and bodies.
Calendar Event Creation: Create Google Calendar events manually or automatically for emails marked as "important" in Gmail.
Automatic Scheduling: Monitor the Gmail inbox every 10 minutes to create calendar events for new "important" emails, tagging them to avoid duplicates.

This project is ideal for users who want to automate email and calendar tasks using natural language, leveraging Claude Desktop’s AI to simplify workflows.
Features

Summarize Emails: Retrieve and summarize up to 5 recent emails from your Gmail inbox, with options to filter by sender or label.
Send Emails: Compose and send emails with support for CC and BCC fields.
Manual Calendar Events: Create Google Calendar events based on email content or custom details (e.g., subject, description, time).
Automatic Calendar Events: Automatically generate calendar events for emails labeled "important" in Gmail, processed every 10 minutes.
Secure Authentication: Uses OAuth 2.0 via Google Cloud credentials for secure access to Gmail and Google Calendar.
Lightweight Server: Built with FastMCP for efficient communication with Claude Desktop.
Cross-Platform: Supports Windows, macOS, and Linux (place credentials.json in ~/.gmail_mcp_server/).

Prerequisites
Before setting up the Gmail MCP Server, ensure you have:

Python 3.8 or higher installed.
Claude Desktop installed and configured.
A Google Cloud Project with Gmail and Google Calendar APIs enabled.
A Gmail account (e.g., your-email@gmail.com) with access to Google Calendar.
Basic familiarity with command-line tools.

Installation
Install the package using pip:
pip install gmail-mcp-server

Note: If the package name is aniket-gmail-mcp-server (due to a PyPI name conflict), use:
pip install aniket-gmail-mcp-server

Setup Instructions
Follow these steps to set up the Gmail MCP Server:
1. Create a Google Cloud Project

Go to Google Cloud Console.
Click Select a project > New Project.
Enter a project name (e.g., Gmail-MCP-Server) and click Create.
Select the new project from the top dropdown.

2. Enable APIs

Navigate to APIs & Services > Library.
Search for and enable:
Gmail API
Google Calendar API



3. Create OAuth 2.0 Credentials

Go to APIs & Services > Credentials.
Click Create Credentials > OAuth 2.0 Client IDs.
Select Desktop app as the application type.
Enter a name (e.g., Gmail MCP Client) and click Create.
Download the credentials.json file (it will be named something like client_secret_*.json).
Save the file as credentials.json.

4. Place credentials.json

Move credentials.json to the appropriate directory:
Windows: C:\Users\<YourUsername>\.gmail_mcp_server\credentials.jsonmkdir C:\Users\<YourUsername>\.gmail_mcp_server
move path\to\downloaded\credentials.json C:\Users\<YourUsername>\.gmail_mcp_server\credentials.json


macOS/Linux: ~/.gmail_mcp_server/credentials.jsonmkdir ~/.gmail_mcp_server
mv ~/Downloads/client_secret_*.json ~/.gmail_mcp_server/credentials.json





5. Configure Claude Desktop

Locate or create claude_desktop_config.json:
Windows: C:\Users\<YourUsername>\AppData\Roaming\Claude\claude_desktop_config.json
macOS/Linux: ~/.config/Claude/claude_desktop_config.json


Add the following configuration:{
  "mcpServers": {
    "email-mcp-server": {
      "command": "gmail-mcp-server",
      "args": [],
      "cwd": ""
    }
  }
}

Note: If using aniket-gmail-mcp-server, update command to aniket-gmail-mcp-server.
Save the file.

6. Run the Server

Activate your Python virtual environment (if using one):path\to\venv\Scripts\activate  # Windows
source path/to/venv/bin/activate  # macOS/Linux


Start the server:gmail-mcp-server


On first run, a browser window will open:
Sign in with your Gmail account (e.g., your-email@gmail.com).
Approve the requested permissions (Gmail read/send, Calendar events).
Bypass the “unverified app” warning by clicking Advanced > Go to Gmail MCP Server (unsafe).


The server will create token.json in ~/.gmail_mcp_server/ and start:Found C:\Users\<YourUsername>\.gmail_mcp_server\credentials.json
[email-mcp-server] [info] Server started and connected successfully



7. Set Up Gmail Label

The server automatically processes emails labeled "important" in Gmail.
Ensure the calendar_event_created label exists:
Go to Gmail.
In the left sidebar, click Create new label.
Name it calendar_event_created and save.



Usage
Once the server is running, interact with it through Claude Desktop using natural language commands. Below are examples:
Summarize Emails
Summarize the last 3 emails in my inbox.


Retrieves the 3 most recent emails and provides a summary of their subject and content (up to 200 characters per email).
Optional filters:Summarize the last 5 emails from john.doe@example.com.
Summarize emails with label "work".



Send Emails
Send an email to friend@example.com with subject "Meeting Tomorrow" and body "Hi, let's meet at 10 AM."


Sends an email with the specified recipient, subject, and body.
Supports CC and BCC:Send an email to friend@example.com, cc colleague@example.com, with subject "Update" and body "Here’s the latest report."



Create Calendar Events
Create a calendar event for the last important email.


Creates a Google Calendar event using the subject and content of the specified email, scheduled for the next day at 10 AM (default).
Manual event creation:Create a calendar event with subject "Team Meeting" and description "Weekly sync" starting tomorrow at 2 PM for 60 minutes.



Automatic Calendar Events

The server checks for new emails labeled "important" every 10 minutes.
For each new important email:
A calendar event is created with the email’s subject and content.
The email is tagged with calendar_event_created to prevent duplicate events.


To test:
Send an email to your Gmail account with keywords like “urgent” or “important”.
In Gmail, apply the “important” label (manually or via filters).
Wait up to 10 minutes and check Google Calendar for a new event.



Dependencies
The following Python packages are automatically installed with gmail-mcp-server:

google-api-python-client: For interacting with Gmail and Google Calendar APIs.
google-auth-oauthlib: For OAuth 2.0 authentication.
mcp: For the FastMCP server framework.
schedule: For scheduling automatic email checks.

Troubleshooting

Credentials Error:
Ensure credentials.json is in C:\Users\<YourUsername>\.gmail_mcp_server\ (Windows) or ~/.gmail_mcp_server/ (macOS/Linux).
Delete token.json to re-authenticate:del C:\Users\<YourUsername>\.gmail_mcp_server\token.json  # Windows
rm ~/.gmail_mcp_server/token.json  # macOS/Linux




Server Not Starting:
Check mcp-server-email-mcp-server.log in the directory where you ran gmail-mcp-server.
Verify dependencies with pip list.


Claude Desktop Issues:
Ensure claude_desktop_config.json has the correct command (e.g., gmail-mcp-server).
Run Claude Desktop in the same virtual environment as the server.


No Calendar Events:
Confirm the important and calendar_event_created labels exist in Gmail.
Test manually:python -c "from gmail_mcp_server.server import check_important_emails; check_important_emails()"





Contributing
Contributions are welcome! To contribute:

Fork the repository at GitHub.
Create a branch for your feature or bug fix.
Submit a pull request with a clear description.

Please follow the Code of Conduct.
License
This project is licensed under the MIT License. See the LICENSE file for details.
Support
For questions or issues:

Email: fakeloginpage13@gmail.com
GitHub Issues: https://github.com/yourusername/gmail-mcp-server/issues
Check the PyPI page for updates.

Acknowledgments

Built with FastMCP for efficient server communication.
Powered by Google’s Gmail and Calendar APIs.
Designed for integration with Claude Desktop by Anthropic.

Thank you for using Gmail MCP Server! 🚀
