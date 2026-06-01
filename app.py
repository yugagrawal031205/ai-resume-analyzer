from flask import Flask, render_template, request, jsonify
from pdf_loader import load_resume
from analyzer import analyze_resume

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    try:
        print("\n========== STEP 1 ==========")

        resume = request.files["resume"]
        job_description = request.form["job_description"]

        print("PDF:", resume.filename)
        print("Job Description received")

        print("\n========== STEP 2 ==========")

        resume.save("uploaded_resume.pdf")

        print("PDF saved successfully")

        print("\n========== STEP 3 ==========")

        resume_text = load_resume("uploaded_resume.pdf")

        print("PDF text extracted")
        print("Characters:", len(resume_text))

        print("\n========== STEP 4 ==========")

        result = analyze_resume(
            resume_text,
            job_description
        )

        print("AI analysis completed")

        print("\n========== STEP 5 ==========")

        # Save analysis to report.txt
        with open("report.txt", "w", encoding="utf-8") as file:
            file.write(result)

        print("Report saved to report.txt")

        return jsonify({
            "analysis": result
        })

    except Exception as e:

        print("\n========== ERROR ==========")
        print(str(e))

        return jsonify({
            "analysis": f"ERROR: {str(e)}"
        }), 500


if __name__ == "__main__":
    app.run(debug=True)