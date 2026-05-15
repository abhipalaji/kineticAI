from flask import Flask, render_template

app = Flask(__name__)

# =========================================
# PUBLIC PAGES
# =========================================

@app.route("/")
def landing():
    return render_template("dashboard.html")


@app.route("/pricing")
def pricing():
    return render_template("pricing.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/support")
def support():
    return render_template("support.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")


# =========================================
# AI WORKSPACE PAGES
# =========================================

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/enhancer")
def enhancer():
    return render_template("enhancer.html")


@app.route("/blogger")
def blogger():
    return render_template("blogger.html")


@app.route("/ad-writer")
def ad_writer():
    return render_template("ad_writer.html")


@app.route("/caption")
def caption():
    return render_template("caption.html")


@app.route("/rewriter")
def rewriter():
    return render_template("rewriter.html")


# =========================================

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)