# MediVbot- Voice Enabled Medical Assistant

This project combines several Python scripts to create a medical assistant with voice recognition capabilities and the ability to control a robotic surgeon. The code is structured into three main components: Bot.py, RobotControl.py, and PatientDatabase.py.

## 1. Bot.py
This script acts as a medical assistant, using the Speech Recognition library to convert spoken commands into text. The assistant responds to various voice commands related to patient information, robotic surgeon control, searching for articles, and more.

Key Functions:

* speak_text(text): Initializes the text-to-speech engine and speaks the given text.

* voice_command(command): Processes voice commands related to patient information, surgeon control, and more.

* search(search_term): Searches for articles or general information online based on the given search term.

* time(): Retrieves and returns the current time.

* recognize_speech(): Listens for audio input, converts it to text, and processes the voice command.

## 2. RobotControl.py
This module provides a framework for controlling a robotic surgeon. Note that this code is a placeholder and only outlines the idea of how to automate a robot for complex surgeries. Actual implementation would require interfacing with specific robotic systems.

Key Functions:

* control_robotic_surgeon(command): Processes commands related to controlling the robotic surgeon.

Functions like move_robotic_surgeon(), rotate_robotic_surgeon(), etc., simulate actions the robotic surgeon might perform.

## 3. PatientDatabase.py
This script interacts with a MySQL database to manage patient information. It includes functions for listing patients, scheduling CT scans, checking blood pressure, recording notes, viewing lab results, and ordering medications.

Key Functions:

* list_patients(): Retrieves and speaks information about all patients in the database.

* schedule_ct_scan(patient_id): Updates the database to schedule a CT scan for a specific patient.

* check_blood_pressure(patient_id): Retrieves and speaks the blood pressure of a specific patient.

* record_note_patient(patient_id): Records a note for a specific patient in the database.

* view_latest_lab_results(patient_id): Retrieves and speaks the latest lab result for a specific patient.

* order_medication(patient_id): Records medication orders for a specific patient in the database.

### Additional Files:
* Sql_code.txt: Includes SQL statements for creating the necessary database and tables, along with an initial patient entry.

### Setup and Dependencies:
* The code relies on Python 3.x, the Speech Recognition library, and the Pyttsx3 library for text-to-speech functionality.
* It uses requests to get the HTML content.
* The project uses beautifulsoup library to parse the HTML Content.
* Wikipedia libary is used for getting the results from wikipedia.
* Ensure the MySQL connector library is installed for database interactions.

### Usage:
&nbsp; 1. Set up the MySQL database using the provided SQL statements.

&nbsp; 2. Ensure the necessary Python libraries are installed  (speech_recognition, pyttsx3).

&nbsp; 3. Run Bot.py to start the medical assistant.

&nbsp; 4. Speak commands to interact with the assistant, control the robotic surgeon (simulated), and manage patient information.

### Note:
The RobotControl.py module contains placeholder functions for controlling the robotic surgeon. 

Actual implementation depends on the specific robotic system used.