from flask import *
import pandas as pd
app = Flask(__name__)

@app.route("/")
def show_tables():
    data = pd.read_csv('titanic.csv')
    data.set_index(['Name'], inplace=True)
    data.index.name=None

    datahead=data.head()
    return render_template('view.html',tables=[datahead.to_html(classes='titanic')],
    titles = ['na', 'Titanic Data'])

if __name__ == "__main__":
    app.run(debug=True)