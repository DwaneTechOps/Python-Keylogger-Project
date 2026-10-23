# Python Keyboard Monitoring Project

## Project Overview

This is my first Python cybersecurity project that was developed as part of my hands-on learning in cybersecurity and Python programming.

The project explores how keyboard events can be detected and recorded in a controlled Windows testing environment.

## Objectives

- Understand how Python handles keyboard events.
- Learn how individual keystrokes can be written to a text file.
- Practise using Python and Visual Studio Code.
- Develop awareness of the privacy and security risks associated with keyboard monitoring.

## Tools and Technologies

- Python
- Visual Studio Code
- Windows
- GitHub

## How to Run the Project

### Requirements

- Windows computer
- Python 3 installed
- Visual Studio Code or another Python editor

### Step 1: Download the Project

1. Open this GitHub repository.
2. Click the green **Code** button.
3. Select **Download ZIP**.
4. Extract the ZIP file to a folder on your computer.
5. Open the extracted folder in Visual Studio Code.

### Step 2: Run the Keyboard Monitor

Open the VS Code terminal and enter:

```powershell
python keylogger.py
```

A window titled **Keyboard Input Monitor** will appear.

1. Click inside the input box.
2. Type a test phrase such as `Hello Cybersecurity`.
3. Observe the keyboard events and timestamps displayed in the window.
4. Click **Save Log** to save your test results to a text file.
5. Use **Clear Log** to clear the displayed events if needed.

The program records keyboard events only while the application's input box is active.

### Step 3: Run the Log Analyzer

The repository includes `sample_output.txt`, which contains demonstration keyboard events.

In the VS Code terminal, enter:

```powershell
python log_analyzer.py
```

The analyzer reads `sample_output.txt` and displays:

- Total number of keyboard events
- Five most frequently recorded keys
- Timestamp of the first event
- Timestamp of the last event

### Step 4: Verify the Results

When using the included sample file, the analyzer should report:

- **Total events:** 6
- **Most frequent key:** `l` (2 occurrences)
- **First event:** `2026-10-22 04:44:31`
- **Last event:** `2026-10-22 04:44:33`

The analyzer uses the demonstration file by default. It does not automatically analyze a newly saved keyboard log.

### Troubleshooting

If the analyzer reports that the log file cannot be found, verify that `sample_output.txt` is in the same folder as `log_analyzer.py`.
## Project Testing

I tested the program on my own Windows computer using the phrase `Hello Cybersecurity`.

The program recorded the individual keyboard events and saved them to a local text file.

A simulated example is included in the `sample_output.txt` file.

## Log Analysis

In addition to monitoring keyboard events, I developed a Python log analyzer (`log_analyzer.py`) to process the recorded events.

I successfully tested the analyzer in my Windows environment.

This component helped me develop a basic understanding of log processing and analysis using Python.

## Security and Ethical Considerations

This project is intended for educational purposes and authorized local testing only.

Actual keyboard logs are excluded from the public repository to avoid exposing potentially sensitive information.

## Skills Developed

- Basic Python programming
- Keyboard event handling
- File input/output
- Program testing
- Cybersecurity awareness
- Technical documentation
- Basic log processing and analysis

## Future Improvements

- Improve error handling.
- Add clearer user-facing controls.
- Explore privacy-preserving keyboard event testing.
- Continue learning Python and defensive cybersecurity techniques.
