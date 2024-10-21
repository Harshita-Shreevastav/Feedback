from flask import Flask, render_template, url_for, request, redirect
from memory import name_comment

app= Flask(__name__)

@app.route("/")
def home():

    
    return  render_template("index.html")


@app.route("/form", methods=['GET', 'POST'])
def form():
    global name_comment

    if request.method=="POST":
        print("Full Form Data:", request.form)
        user=request.form.get("user")
        cmt=request.form.get("cmt")
        if user not in name_comment:
            name_comment[user]=[]
            


        name_comment[user].append(cmt)

        
        print(user)
        print(cmt)
        return redirect(url_for("entry", user=user))

    return render_template("Form.html")

@app.route("/form/entry/<user>")
def entry(user):

    
    return  render_template("enteries.html", user=user,  name_comment=name_comment )


if __name__=="__main__":
    app.run(debug=True)


