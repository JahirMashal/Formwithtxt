# import json
# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///formdata.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class Form(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     your_name = db.Column(db.String(50), nullable=False)
#     email = db.Column(db.String(100), nullable=False)
#     address = db.Column(db.String(500), nullable=False)
#     number = db.Column(db.Integer, nullable=False)
    
    
#     # def __repr__(self) -> str:
#     #     return f"{self.sno} - {self.Your_Name}"  


# def create_tables():
#     with app.app_context():
#         db.create_all()  
#         # print("Tables created.")
        
        
# @app.route("/", method=['POST'])
# def form():
#          with app.app_context():
#             db.session.add(form)
#             # form = Form(
#             #     your_name="Akash Melkeri",
#             #     email="akashmelkeri@gmail.com",
#             #     address="shivtej nagar",
#             #     number=1234567890
#             # )
#             db.session.add(form)
#             db.session.commit()
#             alldata = Form.query.all()
#             print(alldata)
#             return render_template("form.html", alldata)
#             # print("Sample data added.")
                
# # @app.route("/show")
# # def show():
# #     # return render_template('form.html')


# def export_to_json():
#     with app.app_context():
#         try:
            
#             data = Form.query.all()

            
#             data_list = []
#             for item in data:
#                 data_list.append({
#                     'sno': item.sno,
#                     'email': item.email,
#                     'your_name': item.your_name,
#                     'address': item.address,
#                     'number': item.number,
#                 })

            
#             json_data = json.dumps(data_list, indent=4)

            
#             with open('formdata.json', 'w') as json_file:
#                 json_file.write(json_data)
#             # print("Data exported to formdata.json")

#         except Exception as e:
#             print(f"An error occurred: {e}")


# if __name__ == '__main__':
#     with app.app_context():
#         create_tables() 
#         # sample_data() 
#         export_to_json()
#         app.run(debug=True)
        
        


import json
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        your_name = request.form['your_name']
        email = request.form['email']
        address = request.form['address']
        number = request.form['number']

       
        with open('formdata.txt', 'a') as file:
            file.write(f'Name: {your_name}, Email: {email}, Address: {address}, Number: {number}\n')

        return redirect(url_for('success'))

    return render_template('form.html')

@app.route('/covno')
def success():
    return 'Form submitted successfully!'
    data = []
    try:
         with open('formdata.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(', ')
                entry = {}
                for part in parts:
                    key, value = part.split(': ', 1)
                    entry[key.strip()] = value.strip()
                    data.append(entry)
                    with open('formdata.json', 'w') as json_file:
                        json.dump(data, json_file, indent=4)
                        return 'Data converted to JSON and saved as formdata.json'
    except Exception as e:
        return f'An error occurred: {e}'

if __name__ == '__main__':
    app.run(debug=True)


        
        
        

# @app.route("/")
# def form():
#     db.create_all()  
#     form = Form(
#     your_name="Akash Melkeri",
#     email="akashmelkeri@gmail.com",
#     address="shivtej nagar",
#     number=1234567890
# )
#     db.session.add(form)
#     db.session.commit()
#     print("Sample data added.")
#     return render_template("form.html")

# # if __name__ == '__main__':
#     # with app.app_context():
#         # db.create_all()  # Create the database tables
# app.run(debug=True)


# def create_tables():
#     with app.app_context():
#         db.create_all()  
#         print("Tables created.")

# def export_to_json():
#     with app.app_context():
#         try:
            
#             data = Form.query.all()

            
#             data_list = []
#             for item in data:
#                 data_list.append({
#                     'sno': item.sno,
#                     'your_name': item.your_name,
#                     'email': item.email,
#                     'address': item.address,
#                     'number': item.number,
#                 })

            
#             json_data = json.dumps(data_list, indent=4)

            
#             with open('formdata.json', 'w') as json_file:
#                 json_file.write(json_data)
#             print("Data exported to formdata.json")

#         except Exception as e:
#             print(f"An error occurred: {e}")

# if __name__ == '__main__':
#     with app.app_context():
#         # create_tables()  
#         export_to_json() 
#         app.run(debug=True)