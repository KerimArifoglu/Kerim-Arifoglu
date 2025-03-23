from flask import Flask, request, render_template_string
import html

app = Flask(__name__)

# Kullanıcı yorumlarını saklamak için basit bir liste
comments = []


@app.route('/')
def index():
    template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>XSS Fixed Comment System</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }
            .container { max-width: 800px; margin: 0 auto; }
            h1 { color: #333; }
            .comment { border: 1px solid #ddd; padding: 10px; margin-bottom: 10px; border-radius: 5px; }
            form { margin: 20px 0; }
            textarea { width: 100%; padding: 10px; }
            button { padding: 8px 16px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Güvenli Yorum Sistemi</h1>

            <form action="/post_comment" method="POST">
                <textarea name="comment" rows="4" placeholder="Yorumunuzu buraya yazın..."></textarea>
                <button type="submit">Yorum Yap</button>
            </form>

            <h2>Yorumlar</h2>
            {% for comment in comments %}
                <div class="comment">{{ comment }}</div>
            {% endfor %}
        </div>
    </body>
    </html>
    '''
    return render_template_string(template, comments=comments)


@app.route('/post_comment', methods=['POST'])
def post_comment():
    comment = request.form.get('comment', '')
    if comment:
        # Kullanıcı girdisi html.escape() ile temizleniyor
        sanitized_comment = html.escape(comment)
        comments.append(sanitized_comment)
    return index()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)