from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/static/graph")
def static_graph_js():
    return render_template('echart_embed.js')

if __name__ == "__main__":
    app.run()
