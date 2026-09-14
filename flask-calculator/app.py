from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ""
    if request.method == 'POST':
        # HTMLから送られてきた数式を受け取る
        expr = request.form.get('expression', '')
        if expr:
            try:
                # 安全のため、数字と記号だけを許可して計算（eval）する
                allowed = set("0123456789+-*/.()")
                if all(c in allowed for c in expr):
                    result = str(eval(expr))
                else:
                    result = "Error"
            except Exception:
                result = "Error"
                
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)