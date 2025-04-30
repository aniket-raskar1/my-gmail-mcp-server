import json
import base64
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from mcp.server.fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("EmailMcpServer")

# Gmail API setup
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.send']
CREDS_FILE = 'C:/Users/Aniket/OneDrive/Desktop/gmail-mcp-server/credentials.json'

# Debug: Check if credentials.json exists
if not os.path.exists(CREDS_FILE):
    print(f"Error: {CREDS_FILE} not found. Please ensure the file exists.")
else:
    print(f"Found {CREDS_FILE}")

def get_gmail_service():
    creds = None
    try:
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    except FileNotFoundError:
        flow = InstalledAppFlow.from_client_secrets_file(CREDS_FILE, SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

@mcp.tool()
def summarize_emails(max_results: int = 5) -> str:
    """Summarize the latest emails from the inbox."""
    try:
        service = get_gmail_service()
        results = service.users().messages().list(userId='me', maxResults=max_results).execute()
        messages = results.get('messages', [])
        
        if not messages:
            return "No emails found."
        
        summaries = []
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id'], format='full').execute()
            headers = msg['payload']['headers']
            subject = next((header['value'] for header in headers if header['name'] == 'Subject'), 'No Subject')
            snippet = msg['snippet']
            summaries.append(f"Subject: {subject}\nSummary: {snippet[:100]}...")
        
        return "\n\n".join(summaries)
    except Exception as e:
        return f"Error summarizing emails: {str(e)}"

@mcp.tool()
def send_email(to: str, subject: str, body: str, cc: str = "", bcc: str = "") -> str:
    """Send an email to the specified recipient."""
    try:
        service = get_gmail_service()
        message = {
            'to': to,
            'subject': subject,
            'message': body,
            'cc': cc,
            'bcc': bcc
        }
        raw_message = base64.urlsafe_b64encode(
            f"From: me\nTo: {to}\nCc: {cc}\nBcc: {bcc}\nSubject: {subject}\n\n{body}".encode()
        ).decode()
        service.users().messages().send(userId='me', body={'raw': raw_message}).execute()
        return f"Email sent to {to} with subject '{subject}'"
    except Exception as e:
        return f"Error sending email: {str(e)}"

# Run the MCP server
if __name__ == "__main__":
    mcp.run()