from flask import Flask, render_template_string
import os

app = Flask(__name__, template_folder=os.getcwd())  # Tentukan folder template ke direktori saat ini

@app.route('/')
def home():
    # Membaca dan merender index.html dari file secara langsung
    with open('index.html', 'r') as f:
        content = f.read()
    return render_template_string(content)  # Gunakan render_template_string untuk langsung merender HTML

@app.route('/business')
def business():
    # Membaca dan merender business.html dari file secara langsung
    with open('business.html', 'r') as f:
        content = f.read()
    return render_template_string(content)  # Gunakan render_template_string untuk langsung merender HTML

if __name__ == '__main__':
    app.run(host='192.168.18.102', port=5000)
