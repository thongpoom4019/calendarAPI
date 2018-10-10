from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
@app.route('/events')
def event():
    return  ('''This is your <font color=red>upcoming events <font color=black>within today''')
   

@app.route('/timeslot')
def slots():
    return '''
    <font color='blue'>this is <font color ='green'>your <font color='red'> freetime
    '''

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    event = ''
    if request.method=='POST':
        do_the_login()
        c = ''
        for i in request.get_json():
            print(i['summary'], i['creator']['displayName'])
            c += ' ' + i['creator']['displayName'] + '  ' + i['summary'] + ' ' + 'From' + ' ' + i['start']['dateTime'] +' '+'until'+' '+ i['end']['dateTime']
        f = open("timeshown.txt",'w')
        f.write(c)
        return ''' FILE POSTED '''
    else:
        show_the_login_form()
        f = open("timeshown.txt",'r')
        return f.read()

def do_the_login():
    print('FILE ACQUIRED SUCCESFULLY')

def show_the_login_form():
    print('FILE DOWNLOADED SUCCESSFULLY')