# Gmail MCP Server

**Gmail MCP Server** is a Python-based package that seamlessly integrates Gmail and Google Calendar with Claude Desktop, an AI-powered productivity tool. This server enables users to interact with their Gmail inbox and Google Calendar through natural language commands, streamlining email management and event scheduling.

With features like email summarization, sending emails, and automatic calendar event creation for important emails, it enhances productivity by combining AI capabilities with Google’s ecosystem.

---

## What This Project Does

The Gmail MCP Server runs as a background server that connects to Gmail and Google Calendar APIs via an MCP (Message Control Protocol) interface. It allows Claude Desktop to process commands for:

- **Email Summarization**: Generate concise summaries of recent emails, optionally filtered by sender or label.
- **Email Sending**: Send emails directly from Claude Desktop with customizable recipients, subjects, and bodies.
- **Calendar Event Creation**: Create Google Calendar events manually or automatically for emails marked as "important" in Gmail.
- **Automatic Scheduling**: Monitor the Gmail inbox every 10 minutes to create calendar events for new "important" emails, tagging them to avoid duplicates.

This project is ideal for users who want to automate email and calendar tasks using natural language, leveraging Claude Desktop’s AI to simplify workflows.

---

## Features

- **Summarize Emails**: Retrieve and summarize up to 5 recent emails from your Gmail inbox, with options to filter by sender or label.
- **Send Emails**: Compose and send emails with support for CC and BCC fields.
- **Manual Calendar Events**: Create Google Calendar events based on email content or custom details (e.g., subject, description, time).
- **Automatic Calendar Events**: Automatically generate calendar events for emails labeled "important" in Gmail, processed every 10 minutes.
- **Secure Authentication**: Uses OAuth 2.0 via Google Cloud credentials for secure access to Gmail and Google Calendar.
- **Lightweight Server**: Built with FastMCP for efficient communication with Claude Desktop.
- **Cross-Platform**: Supports Windows, macOS, and Linux (`credentials.json` goes in `~/.gmail_mcp_server/`).

---

## Prerequisites

Before setting up the Gmail MCP Server, ensure you have:

- Python 3.8 or higher
- Claude Desktop installed and configured
- A Google Cloud Project with Gmail and Google Calendar APIs enabled
- A Gmail account
- Basic familiarity with command-line tools

---

## Installation

Install the package using pip:

```bash
pip install gmail-mcp-server
