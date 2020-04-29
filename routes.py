from flask import Flask, request, render_template, url_for, redirect, Response
from contojson import convert_to_json
from holidayData import init, getData
from forms import contactform, autocompleteform
from flask_mail import Message, Mail

# resource_scripts
convert_to_json()
init()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'skd3k24lk23489df09sdkl2342k3j4woiq23lk4'

# Mail settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
# Enter your email id
app.config['MAIL_USERNAME'] = ''
# Enter your email password
app.config['MAIL_PASSWORD'] = ''

companies = []

# index
@app.route('/')
def generate_index():
    form1 = contactform(request.form)
    return render_template('index.html', form=form1)

# holiday Calendar
@app.route('/companies/<company_name>/<location>')
def generate(company_name, location):
    global companies
    for(c, l, hols) in getData():
        if company_name == c and location == l:
            return render_template('search_results.html', j_company_name=c, j_location=l, j_holidays=hols)

# List of Companies
@app.route('/companies')
def generate_companies():
    global companies
    for(c, l, hols) in getData():
        link = url_for('generate', company_name=c, location=l)
        companies.append((c, l, link))
    return render_template('companies.html', j_companies=companies)


#Autocomplete and Search
@app.route('/search', methods=['POST'])
def autocomplete():
    form1 = contactform(request.form)
    autocomplete_list = str(request.form.get('autocomplete_list'))
    autocomplete_list = autocomplete_list.split(',')
    companies = autocomplete_list[0].split(':')
    companies = companies[1].replace('"', '')

    location = autocomplete_list[1].split(':')
    location = location[1].replace('"', '')
    location = location.replace('}', '')

    return redirect('/companies/' + companies + '/' + location)

# Send email
# Email is buggy. Need to be set on your own.
@app.route('/', methods=['POST'])
def sendmail():
    form1 = contactform(request.form)
    if request.method == 'POST':
        if form1.validate_on_submit():
            # Enter your email id in the recipient below
            msg = Message(form1.subject.data, sender='contact@example.com', recipients=[
                          ''])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form1.name.data, form1.email.data, form1.message.data)
            mail.send(msg)
            print("posted")
    return render_template('index.html', form=form1)


# Main
if __name__ == '__main__':
    app.run(debug=True)
