from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route("/")
def main():
    html = """<form method="GET" action="/">"""
    for key, value in request.args.items():
        html += f"""<label>{key}</label> <input name="{key}" value="{value}" style="width:700px;"><br/>"""
    html += f"""<button type="submit">Submit</button></form>"""
    html += render_template_string(request.args.get('ssti') or "")
    return html, 200

app.run(host='0.0.0.0', port=9999, debug=True)