from jinja2 import Template


HTML_TEMPLATE = """
<!DOCTYPE html>
<html>

<head>
    <title>AI Newsletter</title>

    <style>
        body {
            font-family: Arial;
            background: #0f172a;
            color: white;
            padding: 40px;
        }

        .card {
            background: #1e293b;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 12px;
        }

        h1 {
            color: #38bdf8;
        }

        h2 {
            color: #f8fafc;
        }
    </style>

</head>

<body>

    <h1>🚀 Weekly AI Agent Newsletter</h1>

    {% for item in summaries %}

    <div class="card">
        <h2>{{ item.title }}</h2>

        <p>{{ item.summary }}</p>

        <a href="{{ item.url }}" target="_blank">
            Read More
        </a>
    </div>

    {% endfor %}

</body>

</html>
"""


def generate_html(summaries):

    template = Template(HTML_TEMPLATE)

    return template.render(
        summaries=summaries
    )