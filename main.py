from flask import Flask, render_template, request, jsonify
import traceback

app = Flask(__name__)

# メインページ（フォームページ）
@app.route('/')
def index():
    return render_template('index.html')

# Pythonコードを実行するエンドポイント
@app.route('/run_python_code', methods=['POST'])
def run_python_code():
    code = request.form['code']
    
    try:
        # execを使ってPythonコードを実行
        local_vars = {}
        exec(code, {}, local_vars)
        result = local_vars
    except Exception as e:
        # エラーが発生した場合の処理
        result = {'error': str(e)}

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
