from flask import Flask, render_template, request, flash, send_file
from controllers.replace import gen_from_template
from IPython import embed
from werkzeug.wsgi import wrap_file
from werkzeug.wrappers import Response
from io import BytesIO

app = Flask(__name__)
app.config["SECRET_KEY"] = "the random string"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/replace")
def template():
    return render_template("replace.html")


@app.route("/api/replace", methods=["POST"])
def replace():
    doc = request.files["docfile"]
    xls = request.files["excelfile"]

    if doc.filename == "":
        return render_template("replace.html", error="模板 Word 文件 不能为空")
    if xls.filename == "":
        return render_template("replace.html", error="替换内容的 Excel 文件 不能为空")

    bs = gen_from_template(doc.stream, xls.stream)

    return send_file(
        bs,
        mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        as_attachment=True,
        download_name="%s.docx" % (request.form["new_filename"] or doc.filename),
    )


if __name__ == "__main__":
    app.run(debug=True)
