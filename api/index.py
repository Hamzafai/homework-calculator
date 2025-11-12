from flask import Flask, render_template_string, url_for

app = Flask(__name__)

USER_AGREEMENT_HTML = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>DzRide User Agreement</title>
    <style>
      :root{--maxw:900px;--accent:#00d12e;--dzride-green:#00d12e;--dark-gray:#1a1a1a;--light-gray:#f5f5f5}
      body{font-family:Inter, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial; margin:0; background:#f7f9fc; color:#1b1f23; line-height:1.6}
      .container{max-width:var(--maxw); margin:40px auto; background:#fff; padding:28px; border-radius:12px; box-shadow:0 6px 24px rgba(12,18,30,0.06)}
      header{display:flex; align-items:center; gap:18px; border-bottom:1px solid #eaeaea; padding-bottom:20px}
      .logo{width:56px; height:56px; border-radius:10px; background:linear-gradient(135deg,var(--dzride-green),#6bff8f); display:flex; align-items:center; justify-content:center; color:#fff; font-weight:700; font-size:24px}
      h1{margin:0; font-size:24px; color:var(--dark-gray)}
      .contact-info{background:var(--light-gray); padding:20px; border-radius:8px; margin:20px 0}
      .contact-grid{display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:15px}
      .contact-item{display:flex; flex-direction:column}
      .contact-label{font-weight:600; color:var(--dark-gray); font-size:14px}
      .contact-value{color:var(--dzride-green); font-weight:500}
      .last-update{color:#666; font-size:14px; margin-top:10px}
      p.lead{color:#374151; font-size:16px}
      nav.breadcrumb{font-size:13px; color:#6b7280; margin-top:10px}
      section{margin-top:22px}
      section h2{font-size:18px; margin:14px 0; color:var(--dark-gray)}
      ul{margin:8px 0 16px 20px}
      .muted{color:#6b7280}
      footer{margin-top:28px; font-size:13px; color:#6b7280; border-top:1px solid #eaeaea; padding-top:20px}
      .notice{background:#f0f9ff; border-left:4px solid var(--accent); padding:12px; border-radius:6px}
      .arbitration-notice{background:#fff8e6; border-left:4px solid #ffc107; padding:12px; border-radius:6px; margin:15px 0}
      .section-list{list-style:none; padding:0; margin:20px 0}
      .section-list li{margin-bottom:8px; padding-left:15px; position:relative}
      .section-list li:before{content:"•"; color:var(--dzride-green); position:absolute; left:0}
      @media (max-width:640px){.container{margin:18px;padding:18px}}
    </style>
  </head>
  <body>
    <div class="container">
      <header>
        <div class="logo">DzRide</div>
        <div>
          <h1>DzRide User Agreement</h1>
          <div class="muted">Effective date: January 1, 2025</div>
        </div>
      </header>

      <nav class="breadcrumb">Home / Legal / User Agreement</nav>

      <div class="contact-info">
        <h3 style="margin-top:0">Customer Service</h3>
        <div class="contact-grid">
          <div class="contact-item">
            <span class="contact-label">Email</span>
            <span class="contact-value">hamza.faiz.ahmedfouatih@ensia.edu.dz</span>
          </div>
          <div class="contact-item">
            <span class="contact-label">Call</span>
            <span class="contact-value">052322418</span>
          </div>
          <div class="contact-item">
            <span class="contact-label">Text</span>
            <span class="contact-value">052322418</span>
          </div>
        </div>
        <div class="last-update">Last Update: July 15, 2025</div>
      </div>

      <div class="arbitration-notice">
        <strong>IMPORTANT NOTE ON ARBITRATION:</strong> PLEASE CAREFULLY REVIEW THE ARBITRATION PROVISION IN SECTION 3, WHICH REQUIRES YOU TO RESOLVE ANY DISPUTES WITH US ON AN INDIVIDUAL BASIS THROUGH FINAL AND BINDING ARBITRATION. YOUR AGREEMENT TO THESE TERMS INDICATES YOUR EXPRESS ACKNOWLEDGEMENT AND AGREEMENT THAT YOU HAVE READ AND UNDERSTAND HOW THE ARBITRATION PROVISION WORKS.
      </div>

      <p class="lead">Welcome to DzRide! This User Agreement explains the terms under which you may use our shared electric micromobility services. By using our website, app, or services, you accept and agree to be bound by the terms below.</p>

      <h2>Table of Contents</h2>
      <ul class="section-list">
        <li>1. Contractual Relationship</li>
        <li>2. Assumption of Risk; Waiver and Release of Claims</li>
        <li>3. Mutual Arbitration Provision</li>
        <li>4. DzRide User Account</li>
        <li>5. Using the App and our Services</li>
        <li>6. Financial Terms</li>
        <li>7. Warranty Disclaimers</li>
        <li>8. Indemnity</li>
        <li>9. Your Personal Information</li>
        <li>10. Intellectual Property</li>
        <li>11. Network Access and Devices</li>
        <li>12. Governing Law and Jurisdiction</li>
      </ul>

      <section>
        <h2>1. Contractual Relationship</h2>
        <p>Neutron Holdings Inc., dba DzRide (hereafter "DzRide", or "we", "us", or "our" depending on context), is a global leader in shared electric micromobility transportation services. DzRide is pleased to offer you access to its shared micromobility offerings subject to the important terms and conditions of this User Agreement.</p>
        <p>By using our Services (including creating a DzRide user account, using the DzRide App, registering for promotions or subscriptions, and accessing DzRide vehicles), you represent and warrant that you are of legal age to enter into binding contracts and agree to these Terms.</p>
      </section>

      <section>
        <h2>2. Assumption of Risk; Waiver and Release of Claims</h2>
        <p class="muted">Please read and understand this section carefully</p>
        <p>You acknowledge and agree that:</p>
        <ul>
          <li>There are inherent risks associated with the use of shared micromobility vehicles</li>
          <li>Vehicles may be damaged or in disrepair due to regular use</li>
          <li>Your use of the Services may result in injury or illness including bodily injury, disability, or death</li>
        </ul>
        <p>You expressly agree to assume all risks and accept all responsibility for any accident, personal injury, property damage, death or disability that you may suffer as a result of using the Services.</p>
      </section>

      <section>
        <h2>3. Mutual Arbitration Provision</h2>
        <p>We each mutually agree to resolve any justiciable disputes between us exclusively through final and binding arbitration instead of filing a lawsuit in court.</p>
        <p><strong>Class Action Waiver:</strong> We both waive our right to have any dispute brought, heard or arbitrated as, or to participate in, a class action, collective action and/or representative action.</p>
        <p>Any dispute shall be determined by final and binding arbitration administered by the American Arbitration Association under its Consumer Arbitration Rules.</p>
      </section>

      <section>
        <h2>4. DzRide User Account</h2>
        <p>To use most aspects of the Services, you must register for and maintain an active personal user account, which requires a valid payment method and other requested information.</p>
        <p>You are responsible for all activity that occurs under your account. Let us know immediately if you suspect unauthorized use of your account.</p>
      </section>

      <section>
        <h2>5. Using the App and our Services</h2>
        <p>Once your account is properly set up, you can use the DzRide App to locate, reserve and/or access our available Services.</p>
        <p><strong>Rules to Ride:</strong></p>
        <ul>
          <li>Don't ride under the influence of alcohol or drugs</li>
          <li>You must be at least 18 years old</li>
          <li>One rider per vehicle only - no passengers</li>
          <li>Wear a helmet (required in some jurisdictions)</li>
          <li>Follow all local traffic laws and regulations</li>
          <li>Park vehicles upright in designated areas</li>
        </ul>
      </section>

      <section>
        <h2>6. Financial Terms</h2>
        <p>You may use our Services on a per-ride and/or subscription basis. Before you start a ride, you will see the applicable fees (start/unlock fee, per minute fee, and/or minimum fee).</p>
        <p>Ride times are rounded up to the nearest minute for fee calculation. Our pricing is exclusive of taxes and other applicable governmental charges.</p>
        <p>If you disagree with any charges, you must let us know within 10 business days from the end of the month in which the disputed charge took place.</p>
      </section>

      <section>
        <h2>7. Warranty Disclaimers</h2>
        <p>We provide our Services "AS IS" and "AS AVAILABLE." Other than as expressly set out in these Terms, we do not make any specific promises about any Services.</p>
        <p class="notice">To the extent permitted by law, we exclude all warranties, whether express or implied.</p>
      </section>

      <section>
        <h2>8. Indemnity</h2>
        <p>To the fullest extent permitted by law, you agree to defend, indemnify and hold harmless DzRide and its affiliates from any and all claims arising out of or in connection with your use of the Services and/or Products, your breach of these Terms, or your violation of any applicable law.</p>
      </section>

      <section>
        <h2>9. Your Personal Information</h2>
        <p>DzRide's collection and use of personal information in connection with the Services is set forth in our Privacy Notice found at <a href="/privacy-policy">/privacy-policy</a>.</p>
        <p>Unless you opt out, you agree that we may contact you by telephone, SMS or text message at the phone numbers you have provided to us, including for marketing purposes.</p>
      </section>

      <section>
        <h2>10. Intellectual Property</h2>
        <p>Subject to these Terms, DzRide grants you a limited, non-exclusive, revocable, non-transferable license to access and use the App and our related software and Services.</p>
        <p>The Products and the Services are DzRide's exclusive property, and your use of them does not transfer any ownership rights to you.</p>
      </section>

      <section>
        <h2>11. Network Access and Devices</h2>
        <p>You are responsible for obtaining the data network access necessary to use the Services. Your mobile network's data and messaging rates and fees may apply if you access or use the Services from your device.</p>
      </section>

      <section>
        <h2>12. Governing Law and Jurisdiction</h2>
        <p>These Terms will be governed by and construed in accordance with the laws of the State of New York, without regard to its conflicts of law provisions.</p>
        <p>You may not assign these Terms without our prior written approval. We may assign these Terms without your consent to a related or affiliated entity.</p>
      </section>

      <section>
        <h2>THANK YOU FOR CHOOSING DzRide!</h2>
        <p>We appreciate you choosing DzRide for your transportation needs. Ride safely and responsibly!</p>
      </section>

      <footer>© 2025 Neutron Holdings Inc., dba DzRide — All rights reserved.</footer>
    </div>
  </body>
</html>
"""

PRIVACY_POLICY_HTML = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>DzRide Privacy Policy</title>
    <style>
      :root{--maxw:900px;--accent:#00d12e;--dzride-green:#00d12e;--dark-gray:#1a1a1a;--light-gray:#f5f5f5}
      body{font-family:Inter, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial; margin:0; background:#f7f9fc; color:#1b1f23; line-height:1.6}
      .container{max-width:var(--maxw); margin:40px auto; background:#fff; padding:28px; border-radius:12px; box-shadow:0 6px 24px rgba(12,18,30,0.06)}
      header{display:flex; align-items:center; gap:18px; border-bottom:1px solid #eaeaea; padding-bottom:20px}
      .logo{width:56px; height:56px; border-radius:10px; background:linear-gradient(135deg,var(--dzride-green),#6bff8f); display:flex; align-items:center; justify-content:center; color:#fff; font-weight:700; font-size:24px}
      h1{margin:0; font-size:24px; color:var(--dark-gray)}
      h2{font-size:20px; margin:25px 0 15px 0; color:var(--dark-gray)}
      h3{font-size:18px; margin:20px 0 10px 0; color:var(--dark-gray)}
      .contact-info{background:var(--light-gray); padding:20px; border-radius:8px; margin:20px 0}
      .contact-grid{display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:15px}
      .contact-item{display:flex; flex-direction:column}
      .contact-label{font-weight:600; color:var(--dark-gray); font-size:14px}
      .contact-value{color:var(--dzride-green); font-weight:500}
      .last-update{color:#666; font-size:14px; margin-top:10px}
      p.lead{color:#374151; font-size:16px}
      nav.breadcrumb{font-size:13px; color:#6b7280; margin-top:10px}
      section{margin-top:22px}
      ul{margin:8px 0 16px 20px}
      .muted{color:#6b7280}
      footer{margin-top:28px; font-size:13px; color:#6b7280; border-top:1px solid #eaeaea; padding-top:20px}
      .notice{background:#f0f9ff; border-left:4px solid var(--accent); padding:12px; border-radius:6px; margin:15px 0}
      .section-list{list-style:none; padding:0; margin:20px 0}
      .section-list li{margin-bottom:8px; padding-left:15px; position:relative}
      .section-list li:before{content:"•"; color:var(--dzride-green); position:absolute; left:0}
      @media (max-width:640px){.container{margin:18px;padding:18px}}
    </style>
  </head>
  <body>
    <div class="container">
      <header>
        <div class="logo">DzRide</div>
        <div>
          <h1>Privacy Notice</h1>
          <div class="muted">Effective: June 30, 2025</div>
        </div>
      </header>

      <nav class="breadcrumb">Home / Legal / Privacy Policy</nav>

      <div class="contact-info">
        <h3 style="margin-top:0">Contact Information</h3>
        <div class="contact-grid">
          <div class="contact-item">
            <span class="contact-label">Email</span>
            <span class="contact-value">hamza.faiz.ahmedfouatih@ensia.edu.dz</span>
          </div>
          <div class="contact-item">
            <span class="contact-label">Phone</span>
            <span class="contact-value">052322418</span>
          </div>
        </div>
        <div class="last-update">Last Update: June 30, 2025</div>
      </div>

      <p class="lead">Neutron Holdings, Inc. dba DzRide and its affiliates (collectively "DzRide," "we," "us," or "our") are strongly committed to transparency, and we want you ("you" or "your") to understand how we collect, use, share and protect your information.</p>

      <section>
        <h2>1. The Types of Information We Collect and Receive</h2>
        <p>The types of information we collect or receive depend on how you use and interact with our Services. We use, disclose and retain this information for the purposes described further below.</p>
        
        <h3>Information We Collect:</h3>
        <ul>
          <li><strong>Account information:</strong> Your name, email address, telephone number, date of birth, gender, address details, and payment information</li>
          <li><strong>Identification documentation:</strong> Government-issued ID for certain Services where required</li>
          <li><strong>Trip and Location data:</strong> Location of your mobile device and DzRide vehicles, start and end times of rides</li>
          <li><strong>Selfies:</strong> For identity verification and safety purposes where required</li>
          <li><strong>Environmental visual data:</strong> Images of surroundings captured by camera-enabled vehicles for safety</li>
          <li><strong>Technical information:</strong> Device IP address, cookies, and similar tracking technologies</li>
          <li><strong>User-generated content:</strong> Information you share on our Services, communities, or social media</li>
        </ul>
      </section>

      <section>
        <h2>2. How We Use Information</h2>
        <p>We use your information, including information about your location, to:</p>
        <ul>
          <li>Provide the Services to you and manage your account</li>
          <li>Verify your identity and age requirements</li>
          <li>Monitor, track and service DzRide vehicles</li>
          <li>Process payments, subscriptions, and special offers</li>
          <li>Communicate with you about your account and our Services</li>
          <li>Personalize advertisements and improve our Services</li>
          <li>Comply with legal obligations and prevent illegal activities</li>
          <li>Collaborate with third parties to improve transportation infrastructure</li>
        </ul>
      </section>

      <section>
        <h2>3. Who Do We Share Your Information With?</h2>
        <p>We share your information with:</p>
        <ul>
          <li><strong>Service providers and partners:</strong> Companies that provide services to DzRide such as hosting, payment processing, and customer support</li>
          <li><strong>Research collaborations:</strong> De-identified trip data with universities and research partners</li>
          <li><strong>Government agencies:</strong> To meet legal requirements and address illegal activities</li>
          <li><strong>Employers:</strong> For DzRide for Business accounts</li>
          <li><strong>Integrated partners:</strong> Third-party services that integrate with our platform</li>
          <li><strong>Local authorities:</strong> For city planning and mobility insights</li>
        </ul>
      </section>

      <section>
        <h2>4. Advertising and Analytics</h2>
        <p>We use analytics services and serve advertisements through third parties that may use cookies, web beacons, and similar technologies to collect information about your use of our Services.</p>
        <p>These entities may use this information to analyze and track data, determine content popularity, deliver targeted advertising, and better understand your online activity.</p>
      </section>

      <section>
        <h2>5. Data Retention</h2>
        <p>We keep your information for as long as is reasonably necessary to provide the Services to you or until your account is deleted, whichever is longer, subject to any longer period as may be required by applicable law.</p>
        <ul>
          <li>Account information is retained for the lifetime of the account</li>
          <li>Transaction information is retained for 7 years for accounting obligations</li>
          <li>Customer support information is retained for the lifetime of the account</li>
        </ul>
      </section>

      <section>
        <h2>6. Your Rights and Choices</h2>
        <p>Depending on where you live, you may have rights including:</p>
        <ul>
          <li><strong>Right to access:</strong> Request a copy of your information</li>
          <li><strong>Right to rectification:</strong> Correct inaccurate information</li>
          <li><strong>Right to erasure:</strong> Delete your information</li>
          <li><strong>Right to restrict processing:</strong> Limit how we use your information</li>
          <li><strong>Right to data portability:</strong> Receive your information in a portable format</li>
          <li><strong>Right to object:</strong> Object to certain processing activities</li>
        </ul>
        
        <div class="notice">
          <p><strong>Managing Your Information:</strong> You can review, change, or delete your information by logging into your account. You can delete your DzRide account at any time through the app settings or by contacting us.</p>
        </div>
      </section>

      <section>
        <h2>7. Contact Us</h2>
        <p>If you have any questions about this Privacy Notice or our data practices, please contact us:</p>
        <ul>
          <li>Email: hamza.faiz.ahmedfouatih@ensia.edu.dz</li>
          <li>Phone: 052322418</li>
        </ul>
        <p>To exercise your privacy rights, please visit the DzRide Privacy Center in the app or contact us directly.</p>
      </section>

      <footer>© 2025 Neutron Holdings Inc., dba DzRide — All rights reserved.</footer>
    </div>
  </body>
</html>
"""

@app.route('/user-agreement')
def user_agreement():
    return render_template_string(USER_AGREEMENT_HTML)

@app.route('/privacy-policy')
def privacy_policy():
    return render_template_string(PRIVACY_POLICY_HTML)

@app.route('/')
def index():
    return ("<p>Flask app is running. Visit <a href='" + url_for('user_agreement') + "'>/user-agreement</a> or <a href='" + url_for('privacy_policy') + "'>/privacy-policy</a></p>")

if __name__ == '__main__':
    # For local development only. Vercel will serve via WSGI.
    app.run(host='0.0.0.0', port=5000, debug=True)
