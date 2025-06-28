from flask import Flask, render_template, request
import pytesseract
from PIL import Image
import os
import csv
import re

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
CSV_FILE = "student_data.csv"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize CSV file if not exists
if not os.path.isfile(CSV_FILE):
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Aadhaar", "Marks", "DOB"])

# Extract fields using regex from raw text
def extract_fields(text):
    fields = {
        "Name": None,
        "Aadhaar": None,
        "Marks": None,
        "DOB": None
    }

    lines = text.splitlines()
    for line in lines:
        line = line.strip()

        if not fields["Name"]:
            # Try to guess name (if it looks like a name and comes early)
            if re.match(r"^[A-Z][a-z]+\s[A-Z][a-z]+$", line):
                fields["Name"] = line

        if not fields["DOB"]:
            dob_match = re.search(r"(Date of Birth|DOB)[^\w]*([\w\s,]+)", line, re.IGNORECASE)
            if dob_match:
                fields["DOB"] = dob_match.group(2).strip()

        if not fields["Aadhaar"]:
            aadhaar_match = re.search(r"(\d{4}[\s-]?\d{4}[\s-]?\d{4})", line)
            if aadhaar_match:
                fields["Aadhaar"] = aadhaar_match.group(1).strip()

        if not fields["Marks"]:
            marks_match = re.search(r"Marks[^\d]*(\d+)", line, re.IGNORECASE)
            if marks_match:
                fields["Marks"] = marks_match.group(1).strip()

    return fields

@app.route("/", methods=["GET", "POST"])
def upload():
    extracted = None
    if request.method == "POST":
        file = request.files["image"]
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            text = pytesseract.image_to_string(Image.open(filepath))
            extracted = extract_fields(text)

            with open(CSV_FILE, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    extracted.get("Name", ""),
                    extracted.get("Aadhaar", ""),
                    extracted.get("Marks", ""),
                    extracted.get("DOB", "")
                ])

    return render_template("index.html", extracted=extracted)

if __name__ == "__main__":
    app.run(debug=True)
