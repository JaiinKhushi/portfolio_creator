from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# Create table
conn = get_db_connection()
conn.execute("""
CREATE TABLE IF NOT EXISTS portfolio (
    name TEXT,
    college TEXT,
    cgpa TEXT,
    tenth TEXT,
    twelfth TEXT,
    skills TEXT,
    project1 TEXT,
    project1_link TEXT,
    project2 TEXT,
    project2_link TEXT,
    email TEXT,
    github TEXT,
    linkedin TEXT
)
""")
conn.commit()
conn.close()

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        data = (
            request.form["name"],
            request.form["college"],
            request.form["cgpa"],
            request.form["tenth"],
            request.form["twelfth"],
            request.form["skills"],
            request.form["project1"],
            request.form["project1_link"],
            request.form["project2"],
            request.form["project2_link"],
            request.form["email"],
            request.form["github"],
            request.form["linkedin"]
        )

        conn = get_db_connection()
        conn.execute("DELETE FROM portfolio")
        conn.execute("INSERT INTO portfolio VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", data)
        conn.commit()
        conn.close()

        return portfolio()

    return render_template("form.html")

@app.route("/portfolio")
def portfolio():
    conn = get_db_connection()
    data = conn.execute("SELECT * FROM portfolio").fetchone()
    conn.close()
    return render_template("portfolio.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
