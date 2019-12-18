from flask import Blueprint, current_app, render_template
from papertrail.cache import cache
from papertrail.data.models import Author, Book


main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
# @cache.cached(300)
def home():
    return render_template('home.htm')

@main.route('/features')
# @cache.cached(300)
def features():
    return render_template('features.htm')

@main.route('/about')
# @cache.cached(300)
def about():
    return render_template('about.htm')

@main.route('/pricing')
# @cache.cached(300)
def pricing():
    return render_template('pricing.htm')

@main.route('/privacy')
# @cache.cached(300)
def privacy():
    return render_template('privacy.htm')

@main.route('/terms')
# @cache.cached(300)
def terms():
    return render_template('terms.htm')

@main.route('/profile')
# @cache.cached(300)
def profile():
    return render_template('profile.htm')

@main.route('/settings')
# @cache.cached(300)
def settings():
    return render_template('settings.htm')

@main.route('/books/')
# @cache.cached(300)
def display_books():
    books = [book for book in Book.query.all()]
    current_app.logger.info('Displaying all books.')

    return render_template("books.htm", books=books)

@main.route('/authors/')
# @cache.cached(300)
def display_authors():
    authors = [author for author in Author.query.all()]
    current_app.logger.info('Displaying all authors.')

    return render_template("authors.htm", authors=authors)
