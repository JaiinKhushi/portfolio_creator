import os
import uuid
from flask import Flask, render_template, request

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":

        # Handle photo upload
        photo_url = None
        photo_file = request.files.get("photo")
        if photo_file and photo_file.filename and allowed_file(photo_file.filename):
            ext = photo_file.filename.rsplit('.', 1)[1].lower()
            filename = f"{uuid.uuid4().hex}.{ext}"
            save_path = os.path.join(UPLOAD_FOLDER, filename)
            photo_file.save(save_path)
            photo_url = f"/static/uploads/{filename}"

        data = {
            # Personal
            "name":           request.form.get("name", "").strip(),
            "title":          request.form.get("title", "").strip(),
            "about":          request.form.get("about", "").strip(),
            "photo":          photo_url,

            # Education
            "college":        request.form.get("college", "").strip(),
            "degree":         request.form.get("degree", "").strip(),
            "cgpa":           request.form.get("cgpa", "").strip(),
            "grad_year":      request.form.get("grad_year", "").strip(),
            "tenth":          request.form.get("tenth", "").strip(),
            "twelfth":        request.form.get("twelfth", "").strip(),

            # Skills & Languages
            "skills":         request.form.get("skills", "").strip(),
            "languages":      request.form.get("languages", "").strip(),

            # Work Experience
            "exp1_role":      request.form.get("exp1_role", "").strip(),
            "exp1_company":   request.form.get("exp1_company", "").strip(),
            "exp1_duration":  request.form.get("exp1_duration", "").strip(),
            "exp1_desc":      request.form.get("exp1_desc", "").strip(),
            "exp2_role":      request.form.get("exp2_role", "").strip(),
            "exp2_company":   request.form.get("exp2_company", "").strip(),
            "exp2_duration":  request.form.get("exp2_duration", "").strip(),
            "exp2_desc":      request.form.get("exp2_desc", "").strip(),

            # Projects
            "project1":       request.form.get("project1", "").strip(),
            "project1_link":  request.form.get("project1_link", "").strip(),
            "project1_desc":  request.form.get("project1_desc", "").strip(),
            "project2":       request.form.get("project2", "").strip(),
            "project2_link":  request.form.get("project2_link", "").strip(),
            "project2_desc":  request.form.get("project2_desc", "").strip(),

            # Certifications
            "cert1_name":     request.form.get("cert1_name", "").strip(),
            "cert1_issuer":   request.form.get("cert1_issuer", "").strip(),
            "cert2_name":     request.form.get("cert2_name", "").strip(),
            "cert2_issuer":   request.form.get("cert2_issuer", "").strip(),
            "cert3_name":     request.form.get("cert3_name", "").strip(),
            "cert3_issuer":   request.form.get("cert3_issuer", "").strip(),

            # Achievements
            "achieve1":       request.form.get("achieve1", "").strip(),
            "achieve2":       request.form.get("achieve2", "").strip(),
            "achieve3":       request.form.get("achieve3", "").strip(),

            # Contact
            "email":          request.form.get("email", "").strip(),
            "phone":          request.form.get("phone", "").strip(),
            "github":         request.form.get("github", "").strip(),
            "linkedin":       request.form.get("linkedin", "").strip(),
        }

        return render_template("portfolio.html", data=data)

    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)