from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/replace")
def template():
    return render_template("replace.html")


@app.route("/api/replace", methods=["POST"])
def replace():
    form = request.form
    src1 = form.get("source1")
    tar1 = form.get("target1")
    doc = request.files["docfile"]

    print(src1, tar1)
    print(doc)
    return "123"


if __name__ == "__main__":
    app.run(debug=True)
