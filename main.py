from pdf_loader import load_resume
from analyzer import analyze_resume

pdf_path = input("Enter PDF path: ")

resume_text = load_resume(pdf_path)

job_description = input("\nPaste Job Description:\n")

result = analyze_resume(
    resume_text,
    job_description
)

with open("report.txt", "w") as file:
    file.write(result)

    print("\nReport saved to report.txt")

print("\nANALYSIS:\n")
print(result)