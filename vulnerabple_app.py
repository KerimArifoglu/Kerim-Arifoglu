from flask import Flask, request, render_template_string

app = Flask(__name__)

# Kullanıcı yorumlarını saklamak için basit bir liste
comments = []


@app.route('/')
def index():
    # XSS zafiyeti: Kullanıcı girdisi doğrudan HTML'e gömülüyor
    template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>XSS Vulnerable Comment System</title>
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
            <h1>Yorum Sistemi</h1>

            <form action="/post_comment" method="POST">
                <textarea name="comment" rows="4" placeholder="Yorumunuzu buraya yazın..."></textarea>
                <button type="submit">Yorum Yap</button>
            </form>

            <h2>Yorumlar</h2>
            {% for comment in comments %}
                <div class="comment">{{ comment|safe }}</div>
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
        # Hiçbir sanitizasyon yapılmadan kullanıcı girdisi ekleniyor
        comments.append(comment)
    return index()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)