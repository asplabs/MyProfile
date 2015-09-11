from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)
app.config['DEBUG'] = True

from google.appengine.api import mail

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/', methods=['GET', 'POST'])
def home():
    """Home page."""
    if request.method == 'POST':
        mail.send_mail(
            sender="%s <%s>" % (request.form.get('your-name'), request.form.get('your-email')),
            to="Arun Shanker Prasad <arunshankerprasad+profile@gmail.com>",
            subject="%s has sent you a message from your profile website" % request.form.get('your-name'),
            body="""
Dear Arun,

Company: %s

Website: %s

The message:

%s

Your Profile.
""" % (request.form.get('company'), request.form.get('website'), request.form.get('message')))
        return redirect(url_for('home'))

    return render_template('home.html')


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
