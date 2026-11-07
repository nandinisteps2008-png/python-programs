from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
from backend import calculate_score

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "loan_applications.db")


# DATABASE

def create_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            account_number TEXT,
            phone TEXT NOT NULL,
            amount REAL NOT NULL,
            income REAL NOT NULL,
            credit_history TEXT NOT NULL,
            score INTEGER,
            status TEXT
        )
    """)

    # Add account_number to an existing database if missing
    cursor.execute("PRAGMA table_info(applications)")
    columns = [column[1] for column in cursor.fetchall()]

    if "account_number" not in columns:
        cursor.execute(
            "ALTER TABLE applications ADD COLUMN account_number TEXT"
        )

    conn.commit()
    conn.close()


# HOME

@app.route("/")
def home():
    return render_template("dashboard.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# APPLY FOR LOAN

@app.route("/apply", methods=["GET", "POST"])
def apply():

    if request.method == "POST":

        name = request.form.get("name")
        account_number = request.form.get("account_number")
        phone = request.form.get("phone")
        amount = float(request.form.get("amount"))
        income = float(request.form.get("income"))
        credit_history = request.form.get("credit_history")

        score, status = calculate_score(
            income, amount, credit_history
        )

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO applications
            (name, account_number, phone, amount, income,
             credit_history, score, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            name, account_number, phone, amount, income,
            credit_history, score, status
        ))

        conn.commit()
        conn.close()

        return render_template(
            "success.html",
            name=name,
            phone=phone,
            amount=amount,
            score=score,
            status=status
        )

    return render_template("apply.html")


# VIEW APPLICATIONS

@app.route("/applications")
def applications():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, phone, amount, income,
        credit_history, score, status
        FROM applications
        ORDER BY id DESC
    """)

    application_list = cursor.fetchall()
    conn.close()

    return render_template(
        "applications.html",
        applications=application_list
    )


# CHECK CREDIT SCORE

@app.route("/check-score", methods=["GET", "POST"])
def check_score():

    score = None
    status = None
    name = None
    message = None

    if request.method == "POST":

        phone = request.form.get("phone")

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT name, score, status
            FROM applications
            WHERE phone = ?
            ORDER BY id DESC
            LIMIT 1
        """, (phone,))

        result = cursor.fetchone()
        conn.close()

        if result:
            name = result[0]
            score = result[1]
            status = result[2]
        else:
            message = "No application found."

    return render_template(
        "credit_score.html",
        name=name,
        score=score,
        status=status,
        message=message
    )


# LOGOUT

@app.route("/logout")
def logout():
    return redirect(url_for("home"))


# RUN APPLICATION

if __name__ == "__main__":
    create_table()
    app.run(debug=True)