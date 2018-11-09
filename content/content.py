from flask import render_template, Blueprint
from database.db import FootballTable

content = Blueprint('content', __name__, static_folder='./static', template_folder='./template')

@content.route('/', methods=['GET', 'POST'])
@content.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@content.route('/list_of_products', methods=['GET'])
def list_of_products():
    football = FootballTable.query.order_by(FootballTable.id).all()
    return render_template('list_of_products.html', values=football)

@content.route('/list_of_products_detail/<int:id>')
def list_of_products_detail(id):
    footballer = FootballTable.query.filter_by(id=id).first()
    if footballer:
        return render_template('list_of_products_detail', footballer=footballer)

    return "No such id"


@content.errorhandler(404)
def error_handler(e):
    return render_template('404.html'), 404
