from flask import Flask, render_template, request, jsonify
import numpy as np
import matplotlib
matplotlib.use('Agg')  # 使用非交互式後端
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import io
import base64
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

def generate_data(a, b=0, noise_level=1, num_points=100):
    # 固定 X 的範圍為 0 到 10
    x = np.linspace(0, 10, num_points)
    y = a * x + b + np.random.normal(0, noise_level, num_points)
    return x, y

def create_plot(x, y, y_pred):
    try:
        plt.figure(figsize=(10, 6))
        plt.scatter(x, y, color='blue', alpha=0.5)
        plt.plot(x, y_pred, color='red', linewidth=2)
        plt.xlabel('X')
        plt.ylabel('Y')
        # plt.title('簡單線性回歸')
        
        # 設置固定的軸範圍
        plt.xlim(0, 10)
        plt.ylim(-10, 60)  # 根據您的數據範圍調整這個值
        
        # 添加網格線以便更容易比較
        plt.grid(True, linestyle='--', alpha=0.7)
        
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()
        plt.close()
        return plot_url
    except Exception as e:
        logging.error(f"Error in create_plot: {str(e)}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            a = float(request.form['a'])
            noise_level = float(request.form['noise_level'])
            num_points = int(request.form['num_points'])

            x, y = generate_data(a, noise_level=noise_level, num_points=num_points)
            
            model = LinearRegression()
            model.fit(x.reshape(-1, 1), y)
            
            y_pred = model.predict(x.reshape(-1, 1))
            
            plot_url = create_plot(x, y, y_pred)
            
            if plot_url is None:
                return jsonify({'error': 'Failed to generate plot'}), 500
            
            return jsonify({'plot_url': plot_url})
        except Exception as e:
            logging.error(f"Error in index route: {str(e)}")
            return jsonify({'error': str(e)}), 400
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
