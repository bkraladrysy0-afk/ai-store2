from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1 style='text-align:center;font-family:Arial'>متجر الذكاء الاصطناعي 🤖</h1>
    <p style='text-align:center'>أهلاً بك في متجرك، الموقع شغال!</p>
    <div style='text-align:center'>
    <a href='/product1' style='background:#000;color:#fff;padding:10px 20px;text-decoration:none;border-radius:10px'>شاهد المنتج</a>
    </div>
    """

@app.route('/product1')
def p1():
    return "<h1>منتج 1 - أداة ذكاء اصطناعي</h1><p>السعر: 10$</p><a href='/'>رجوع</a>"

if __name__ == '__main__':
    app.run()
