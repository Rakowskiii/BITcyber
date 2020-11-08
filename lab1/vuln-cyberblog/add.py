from app import db
from app.models import Post,User, UserData
p1 = Post(id="4c4be2dc-c3e9-401d-9127-b33befcd49ba", title="Path Traversal", description = "Meaning the art of exploiting user-given filepaths.", img="path-trav.png", date = "November 2, 2020", content="""
\"A path traversal attack (also known as directory traversal) aims to access files and directories that are stored outside the web root folder. By manipulating variables that reference files with “dot-dot-slash (../)” sequences and its variations or by using absolute file paths, it may be possible to access arbitrary files and directories stored on file system including application source code or configuration and critical system files. It should be noted that access to files is limited by system operational access control (such as in the case of locked or in-use files on the Microsoft Windows operating system).

This attack is also known as “dot-dot-slash”, “directory traversal”, “directory climbing” and “backtracking”.



 Actually I've been thinking about it, and have decided to give it a try. I made this super secure file upload&load that is definitely not vulnerable!\n""")

p2 = Post(id="ba1d889c-a14a-427d-b9a6-a4b7f43cf831", title="Insecure Direct Object Reference", description = "Also called IDOR (quite shorter)", img="idor.png", date = "November 2, 2020", content="""
Insecure Direct Object Reference (called IDOR from here) occurs when a application exposes a reference to an internal implementation object. Using this way, it reveals the real identifier and format/pattern used of the element in the storage backend side. The most common example of it (although is not limited to this one) is a record identifier in a storage system (database, filesystem and so on).
""")
p3 = Post(id="89ae6631-0d26-43c3-9981-5171e6ff9701", title="Test blog post v3", description = "This is a amazing test blog postv3", img="jwt.png", date = "November 2, 2020", content="")

u1 = User(id = 0, done=False, done2 = False, adm_blocked = True)

d1 = UserData(id="eydpZCc6MH0K", username = "Guest", password = "None", localization = "KN BIT Lab", card = "Kept secure(hopefully)", cve = "997")
d2 = UserData(id="eydpZCc6NjY2fQo=", username = "Marcin Dekiel", password = "RuszofeMotyle12!", localization = "Gdansk", card = "4913152021013559", cve = "950")
d3 = UserData(id="eydpZCc6NzMxMn0K", username = "Jezus", password = "12apostolow+jJ100%", localization = "Lodz", card = "5130216704108756", cve = "373")

db.create_all()
db.session.add(d1)
db.session.add(d2)
db.session.add(d3)
db.session.add(p1)
db.session.add(u1)
db.session.add(p2)
#db.session.add(p3)
db.session.commit()


