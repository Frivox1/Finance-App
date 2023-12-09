import matplotlib
matplotlib.use('Agg')

from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from flask import Flask, render_template, request
from io import BytesIO
import base64

from config import API_KEY

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        symbol = request.form['symbol']
        days = int(request.form['days'])
        return generate_chart(symbol, days)

    return render_template('index.html')

def generate_chart(symbol, days):
    ts = TimeSeries(key=API_KEY, output_format='pandas')  # Utilisez la clé API importée
    data, meta_data = ts.get_daily(symbol=symbol, outputsize='compact')

    plt.figure()
    data['4. close'].iloc[:days].plot()
    plt.title(f'Cours de clôture pour {symbol} sur {days} jours')
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return render_template('index.html', plot_url=plot_url, symbol=symbol, days=days)

if __name__ == '__main__':
    app.run(debug=True)
