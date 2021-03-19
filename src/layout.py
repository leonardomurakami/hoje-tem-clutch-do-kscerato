import dash_html_components as html

from flask import render_template
from routes import hoje_tem_clutch_do_kscerato
from style import h2_style, h3_style

def create_root(app):
    @app.route('/')
    def get_layout():
        response_string = hoje_tem_clutch_do_kscerato()
        h3 = "Hoje tem clutch do KSCERATO?"
        h2 = f"{response_string}"
        return render_template("layout.html", h2=h2, h3=h3)



