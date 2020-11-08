Register page
Login page
Admin panel
Posty
Mypanel





Rejestracja -> Można zakładać konto admina

Zapomniałem hasła - enumeracja



Logowanie -> nazwa użytkownika w template {{extends "mypanel.html}} 

@app.errorhandler(404)

def page_not_found(e):

    template = '''{ extends "layout.html" }
 { block body }
 <div class="center-content error">
 <h1>Oops! That page doesn't exist.</h1>
 <h3>%s</h3>
 </div>
 { endblock }
 ''' % (request.url)

    return render_template_string(template), 404
    
    

 W wyszukiwarce SQLI 
 
 
 Dodać ciasteczka
 W postach XSS, dodać autoklikacza, który będzie sprawdzał czy jest i dawał się zxssować
