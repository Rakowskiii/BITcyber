from app import db, Division
java = Division(id=1, division = "BIT Java", link = "https://www.facebook.com/groups/bit.java.agh", description="Jeśli lubisz programowanie obiektowe i język java to idealne miejsce. Dodatkowo można od prowadzącego nauczyć się wyciskać 30h z doby.", logo = "bit-logo-java.svg")

algo = Division(id=2, division="BIT Algo",link ="https://www.facebook.com/groups/bitalgoagh", description="Nie oszukujmy się, cudów nie ma, byłbym członkiem gdybym umiał matme.", logo="bit-logo-algo.svg")

infra = Division(id=3, division = "BIT Infra", link = "https://www.facebook.com/groups/bitinfra", description="Jak tak teraz o tym czytam, to żałuje że nie dołączyłem. Na stronie mają nawet zakładkę CyberSec. Full love.", logo = "bit-logo-infra.svg")

db.session.add(java)

db.session.add(algo)
db.session.add(infra)
db.session.commit()
