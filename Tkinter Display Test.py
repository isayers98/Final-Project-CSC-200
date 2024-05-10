from tkinter import ttk
import tkinter as tk
import sqlite3
import tksheet

def enter_data():
    #Name Info
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    
    if firstname and lastname:
        gender = gender_box.get()
        fiftyfree = fifty_free_entry.get()

        print("First Name: ", firstname, "Last Name: ", lastname) 
        print("Gender: ", gender, "50Free: ", fiftyfree)
        
        conn = sqlite3.connect('data.db')
        table = """ CREATE TABLE IF NOT EXISTS Student_Data (
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            gender TEXT,
            fiftyfree INT
                ); """
        conn.execute(table)

 
        print("Table is Ready")

        #Insert Data
        data_insert_querey = '''INSERT INTO Student_Data (firstname, lastname, gender, fiftyfree) VALUES 
        (?,?,?,?)
        '''
        data_insert_tuple = (firstname, lastname, gender, fiftyfree)
        cursor = conn.cursor()
        cursor.execute(data_insert_querey, data_insert_tuple)
        conn.commit() 
        conn.close()

    else:
        tk.messagebox.showwarning(title="Error", message="First Name and Last Name are Required Fields")


#root Window 
window = tk.Tk()
window.title("Data Entry Form")

#Frame within Window (make + pack)
frame = tk.Frame(window)
frame.pack()

menu = tk.Menu(window)
window.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=window.quit)
helpmenu = tk.Menu(menu)


#Event Frame Widgets
##Free
#Frame within Frame within Window
user_info_frame = tk.LabelFrame(frame, text = "User Information")
user_info_frame.grid(row= 0, column= 0, padx= 20, pady= 10)

#Name Info (full_name_label)
first_name_label = tk.Label(user_info_frame, text="First Name: ")
first_name_label.grid(row=0, column=0)
first_name_entry = tk.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)

last_name_label = tk.Label(user_info_frame, text="Last Name: ")
last_name_label.grid(row=0, column=1)
last_name_entry = tk.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

#Competition Gender Info (gender_label, gender_box)
gender_label = tk.Label(user_info_frame, text="Gender")
gender_box = ttk.Combobox(user_info_frame, values=["M", "F"])
gender_label.grid(row=0, column=2)
gender_box.grid(row=1, column=2) 

fifty_free = tk.Label(user_info_frame, text="50 Free: ")
fifty_free.grid(row=0,column=3)
fifty_free_entry = tk.Entry(user_info_frame)
fifty_free_entry.grid(row=1, column=3)


#Padding for Widgets
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx= 10, pady=5)


#Entry Button
button = tk.Button(frame, text= "Submit Data", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

#Display Button
def View():
    conn = sqlite3.connect("data.db")
    cur1 = conn.cursor()
    cur1.execute("SELECT * FROM Student_Data Order BY fiftyfree")
    rows = cur1.fetchall()    
    for row in rows:
        print(row) 
        tree.insert("", tk.END, values=row)        
    conn.close()
button1 = tk.Button(text="Display data", command= View)
button1.pack(pady=10)

def connect():
    conn = sqlite3.connect("data.db")
    cur1 = conn.cursor()
    cur1.execute(""" CREATE TABLE IF NOT EXISTS Student_Data (
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            gender TEXT,
            fiftyfree INT
                ); """)
    conn.commit()
    conn.close()



# connect to the database
connect() 
root = tk.LabelFrame(frame, text = "Event Order")
root.grid(row= 4, column= 0, padx= 20, pady= 10)
tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4"), show='headings')
tree.column("#1", anchor=tk.CENTER)
tree.heading("#1", text="First")
tree.column("#2", anchor=tk.CENTER)
tree.heading("#2", text="Last")
tree.column("#3", anchor=tk.CENTER)
tree.heading("#3", text="Gender")
tree.column("#4", anchor=tk.CENTER)
tree.heading("#4", text="Time")
tree.pack()

#Loop for Operation
window.mainloop() 