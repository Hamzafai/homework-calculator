from flask import Flask, render_template_string, url_for

app = Flask(__name__)

# USER_AGREEMENT_HTML 
USER_AGREEMENT_HTML = """
    <!doctype html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>User Agreement</title>
    <style>
    :root{--maxw:900px;--accent:#0b63d3}
    body{font-family:Inter, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial; margin:0; background:#f7f9fc; color:#1b1f23}
    .container{max-width:var(--maxw); margin:40px auto; background:#fff; padding:28px; border-radius:12px; box-shadow:0 6px 24px rgba(12,18,30,0.06)}
    header{display:flex; align-items:center; gap:18px}
    .logo{width:56px; height:56px; border-radius:10px; background:linear-gradient(135deg,var(--accent),#6fb1ff); display:flex; align-items:center; justify-content:center; color:#fff; font-weight:700}
    h1{margin:0; font-size:20px}
    p.lead{color:#374151}
    nav.breadcrumb{font-size:13px; color:#6b7280; margin-top:10px}
    section{margin-top:22px}
    section h2{font-size:16px; margin:14px 0}
    ul{margin:8px 0 16px 20px}
    .muted{color:#6b7280}
    footer{margin-top:28px; font-size:13px; color:#6b7280}
    .notice{background:#f0f9ff; border-left:4px solid var(--accent); padding:12px; border-radius:6px}
    @media (max-width:640px){.container{margin:18px;padding:18px}}
    </style>
    </head>
    <body>
    <div class="container">
    <header>
    <div class="logo">LI</div>
    <div>
    <h1>User Agreement</h1>
    <div class="muted">Effective date: January 1, 2025</div>
    </div>
    </header>
    
    
    <nav class="breadcrumb">Home / Legal / User Agreement</nav>
    
    
    <p class="lead">Welcome! This User Agreement explains the terms under which you may use our services. By using our website or services, you accept and agree to be bound by the terms below.</p>
    
    
    <section>
    <h2>1. Using our services</h2>
    <p class="muted">Permitted uses and account responsibilities</p>
    <ul>
    <li>You may use the services for lawful purposes only.</li>
    <li>You are responsible for maintaining the confidentiality of your account credentials.</li>
    <li>We may suspend or terminate accounts that violate this agreement or applicable law.</li>
    </ul>
    </section>
    
    
    <section>
    <h2>2. Content and intellectual property</h2>
    <p class="muted">What rights you grant us and what stays yours</p>
    """

# Routes
@app.route('/user-agreement')
def user_agreement():
return render_template_string(USER_AGREEMENT_HTML)


@app.route('/')
def index():
return ("<p>Flask app is running. Visit <a href='" + url_for('user_agreement') + "'>/user-agreement</a></p>")

# Export the Flask app for Vercel
if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
