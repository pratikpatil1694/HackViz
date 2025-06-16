from flask import Flask, render_template, request

app = Flask(__name__)

# Pre-defined OWASP Top 10 simulation steps
SIMULATIONS = {
    "Injection": [
        "User submits a malicious SQL query via login form.",
        "Application executes the query directly on the database.",
        "Attacker retrieves or modifies sensitive data.",
        "Database is compromised due to lack of input sanitization."
    ],
    "Broken Authentication": [
        "Attacker guesses or brute-forces weak credentials.",
        "No multi-factor authentication is enabled.",
        "Session tokens are predictable or reused.",
        "Account takeover is achieved."
    ],
    "Sensitive Data Exposure": [
        "Sensitive data like credit cards is sent over HTTP.",
        "No encryption at rest or in transit.",
        "Attacker intercepts data via MITM or sniffing.",
        "Data breach occurs."
    ],
    "XML External Entities (XXE)": [
        "App accepts user-uploaded XML without validation.",
        "Malicious XML entity tries to access internal files.",
        "Server discloses sensitive info (e.g., /etc/passwd)."
    ],
    "Broken Access Control": [
        "Attacker accesses restricted URLs directly.",
        "No proper role-based authorization checks.",
        "Privileged actions performed as a regular user."
    ],
    "Security Misconfiguration": [
        "Default admin pages or credentials left unchanged.",
        "Unpatched software versions used.",
        "Error stack traces exposed to end users."
    ],
    "Cross-Site Scripting (XSS)": [
        "Attacker injects malicious JS into a comment field.",
        "Script runs in victim's browser.",
        "Session cookies stolen or user is redirected."
    ],
    "Insecure Deserialization": [
        "Untrusted serialized data sent to backend.",
        "Data includes malicious executable code.",
        "System executes the code, granting remote access."
    ],
    "Using Components with Known Vulnerabilities": [
        "Old jQuery version used with known bugs.",
        "Attacker exploits public CVE to attack site.",
        "RCE or data exfiltration achieved."
    ],
    "Insufficient Logging & Monitoring": [
        "Unauthorized access goes undetected.",
        "No logs generated or alerts raised.",
        "Post-incident investigation becomes difficult."
    ]
}

@app.route("/", methods=["GET", "POST"])
def index():
    scenario = ""
    simulation = []
    if request.method == "POST":
        scenario = request.form.get("scenario")
        simulation = SIMULATIONS.get(scenario, [])

    return render_template("index.html", scenario=scenario, simulation=simulation)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
