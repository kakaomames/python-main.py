from flask import Flask, render_template, request, jsonify
import traceback

app = Flask(__name__)

# メインページ（フォームページ）
@app.route('/')
def index():
    return render_template('index.html')

# PythonコードをGETリクエストで実行するエンドポイント
@app.route('/run_python_code', methods=['GET'])
def run_python_code():
    code = request.args.get('code', '')
    
    if not code:
        return jsonify({'error': 'コードが提供されていません'})

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
