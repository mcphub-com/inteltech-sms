# Inteltech SMS MCP Server

Welcome to the Inteltech SMS MCP Server documentation. This server enables you to send and receive SMS messages globally. It is designed to offer seamless integration for managing SMS communications with ease. To get started, you will need to create an account, which is free of charge.

## Features

- **Global Reach**: Send messages to any country in the world.
- **Intelligent SMS Management**: Allows for both sending and receiving of messages.
- **User-Friendly**: Requires an account setup to begin utilizing the service.

## Global Response Codes

- **0000**: Message added to queue OK.
- **2006**: Not enough information supplied for authentication. Ensure that your Username and Unique Key are provided in your request.
- **2007**: Your account has not been activated.
- **2015**: The destination mobile number is invalid.
- **2016**: Identical message already sent to this recipient. Please try again in a few seconds.
- **2017**: Invalid Sender ID. Ensure Sender ID is no longer than 11 characters and contains no spaces.
- **2018**: You have reached the end of your message credits. You need to purchase more message credits.
- **2022**: Your Unique Key is incorrect. This may be caused by a recent Key change.
- **2051**: Message is empty.
- **2052**: Too many recipients.
- **2100-2199**: Internal error.

## Testing

### Test Data

Below are the mobile numbers available for testing:

- **Australian Mobile Number**: 0411111111
- **International Mobile Number**: +8611111111111  

Messages sent to these numbers will receive a ‘message added to queue’ response, but no SMS will actually be sent. This testing does not use any of your credits.

### Test User

For testing purposes, a test user with no credit is available:

- **Username**: nocredit
- **Secure Unique Key**: e7e62e1826d6f9ac1dcc208963b58b8cdad9aa12b53  

This user will always return a no credit error.

## Tools

The Inteltech SMS MCP Server offers the following tools for managing your SMS communications:

- **Check Credit**: This tool allows you to check your prepaid account balance to manage and budget your message credits efficiently.
  - Function: `check_credit`
  - Description: Returns Prepaid Account Balance

- **Send SMS**: This tool enables you to send SMS messages through the Inteltech SMS MCP Server.
  - Function: `send_sms`
  - Description: Send an SMS with the Inteltech API

These tools are designed to provide a comprehensive management system for your SMS needs, ensuring efficient and effective communication.

## Conclusion

The Inteltech SMS MCP Server offers a reliable and user-friendly platform for managing your SMS communications. With global reach, intelligent management, and easy-to-use tools, it supports a wide range of messaging needs for businesses and individuals alike. For more detailed usage, refer to the specific tool functions provided in this documentation.