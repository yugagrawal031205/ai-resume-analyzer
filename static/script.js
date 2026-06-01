document
.getElementById("resume-form")
.addEventListener("submit", async function(e){

    e.preventDefault();

    const formData = new FormData();

    const file =
        document.getElementById("resume").files[0];

    const jobDescription =
        document.getElementById("job-description").value;

    if (!file) {
        alert("Please upload a resume.");
        return;
    }

    formData.append("resume", file);
    formData.append("job_description", jobDescription);

    document.getElementById("result").innerHTML =
    `
    <div class="loading">
        ⏳ Analyzing Resume...
        <br><br>
        This may take 10-30 seconds
    </div>
    `;

    try {

        const response = await fetch("/analyze", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        document.getElementById("result").innerHTML =
        `
        <h2>📊 Analysis Result</h2>

        <div class="analysis-box">
            ${data.analysis.replace(/\n/g, "<br>")}
        </div>

        <br>

        <button id="copy-btn">
            📋 Copy Analysis
        </button>
        `;

        document
        .getElementById("copy-btn")
        .addEventListener("click", function(){

            navigator.clipboard.writeText(data.analysis);

            alert("Analysis copied to clipboard!");
        });

    } catch(error) {

        document.getElementById("result").innerHTML =
        `
        <div class="analysis-box">
            ❌ Something went wrong while analyzing the resume.
        </div>
        `;

        console.error(error);
    }

});


document
.getElementById("resume")
.addEventListener("change", function(){

    const file = this.files[0];

    if(file){

        document.getElementById("file-name").innerHTML =
        "📄 " + file.name;

    }

});