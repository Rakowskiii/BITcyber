from app import db, Division
#java cyber infra algo python shader sfi
python = Division(id=4, division = "BIT Python", link = "https://www.facebook.com/groups/bit.python", description="Ta sekcja zajmuje się językiem programowania, który nie będzie regularnie napędzał Ci myśli samobójczych. Ale nigdy nie masz pewności co jest intem.", logo = "bit-logo-python.svg")

shader = Division(id=5, division="BIT Shader",link ="https://www.facebook.com/SKNShader", description="Spójrzmy prawdzie w oczy. Grafika to wyższy poziom magii. Oddałbym moje obie dwie lewe ręce żeby tak umieć.", logo="bit-logo-shader.svg")

sfi = Division(id=6, division = "BIT SFI", link = "https://sfi.pl/en/home-page/", description="S F I. Cudowny event. Co z tego, że jest covid. Globalna konferencja. Genialni ludzie. Kosmos.", logo = "bit-logo-sfi.svg")

db.session.add(python)

db.session.add(shader)
db.session.add(sfi)
db.session.commit()
