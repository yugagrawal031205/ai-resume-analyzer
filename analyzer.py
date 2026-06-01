from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3",
    temperature=0
)

def analyze_resume(resume_text, job_description):

    prompt = f"""
You are a professional technical recruiter.

Analyze the candidate's resume against the job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Instructions:
1. Compare the resume with the job description.
2. Give a realistic match score out of 100.
3. Identify strengths.
4. Identify missing skills.
5. Give practical suggestions.
6. Keep the response concise and professional.

Return ONLY the following format:

MATCH SCORE:
XX/100

STRENGTHS:
- ...
- ...
- ...

MISSING SKILLS:
- ...
- ...
- ...

SUGGESTIONS:
- ...
- ...
- ...

FINAL VERDICT:
(2-3 sentence summary)
"""

    response = llm.invoke(prompt)

    return response.content