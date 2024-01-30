import mysql.connector
from RobotControl import *

# Initialize database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hello@sql",
    database="csaht"
)

def list_patients():

    # create a cursor to execute SQL queries
    mycursor = mydb.cursor()

    # fetch all the patients from the database
    mycursor.execute("SELECT * FROM patients")
    patients = mycursor.fetchall()
    for patient in patients:
        patient_id = patient[0]
        name = patient[1]
        dob = patient[2]
        bp = patient[3]
        ct_scan_status = patient[4]
        
    # speak patient record
    engine.say(f"Patient ID: {patient_id}. Name: {name}. Born on {dob}. Blood pressure {bp}. CT scan status {ct_scan_status}.")
    engine.runAndWait()
    # speak_text(patients)

def schedule_ct_scan(patient_id):
    cursor = mydb.cursor()
    cursor.execute(
        f"UPDATE patients SET ct_scan = 'scheduled' WHERE id = {patient_id}")
    mydb.commit()
    speak_text("CT scan has been scheduled for the patient.")

def check_blood_pressure(patient_id):
    cursor = mydb.cursor()
    cursor.execute(
        f"SELECT blood_pressure FROM patients WHERE id = {patient_id}")
    result = cursor.fetchone()
    if result is not None:
        blood_pressure = result[0]
        speak_text(f"The patient's blood pressure is {blood_pressure}.")
    else:
        speak_text(
            "Sorry, I could not find the patient's blood pressure in the database.")

def record_note_patient(patient_id):
    speak_text("Please speak the note you would like to record.")
    note = recognize_speech()
    if note is not None:
        cursor = mydb.cursor()
        cursor.execute(
            f"INSERT INTO notes (patient_id, note) VALUES ({patient_id}, '{note}')")
        mydb.commit()
        speak_text("Note has been recorded for the patient's chart.")

def view_latest_lab_results(patient_id):
    cursor = mydb.cursor()
    cursor.execute(
        f"SELECT result FROM lab_results WHERE patient_id = {patient_id} ORDER BY date DESC LIMIT 1")
    result = cursor.fetchone()
    if result is not None:
        lab_result = result[0]
        speak_text(f"The latest lab result for the patient is {lab_result}.")
    else:
        speak_text(
            "Sorry, I could not find any lab results for the patient in the database.")

def order_medication(patient_id):
    speak_text("Please speak the name of the medication you would like to order.")
    medication = recognize_speech()
    if medication is not None:
        speak_text("Please speak the dosage and instructions for the medication.")
        dosage_instructions = recognize_speech()
        if dosage_instructions is not None:
            cursor = mydb.cursor()
            query = "INSERT INTO medications (patientid, medication, dosage_instructions) VALUES ({patient_id}, %s, %s)"
            cursor.execute(
                query, (patient_id, medication, dosage_instructions))

            # cursor.execute("INSERT INTO medications (patient_id, medication, dosage_instructions) VALUES (%s, %s, %s)", (patient_id, medication, dosage_instructions))
            mydb.commit()
            speak_text("Medication has been ordered for the patient.")
