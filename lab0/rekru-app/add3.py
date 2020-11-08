from app import db, Division
#java cyber infra algo python shader sfi
ai = Division(id=7, division = "BIT AI", link = "https://www.facebook.com/groups/bit.ai.agh", description="Mózgi. AI to też matma niestety. Ale to jest przyszłość. Dopóki nie przejmą kontroli, a Alexa robi co jej każę, jest super!", logo = "bit-logo-ai.svg")

dotnet = Division(id=8, division="BIT .NET",link ="https://www.facebook.com/knbit", description="Taka java. Ale M$. W Unity można w tym robić gry. Ale na kole pewnie też jakieś poważne rzeczy. Czekam na crossover z javą.", logo="bit-logo-net.svg")


db.session.add(ai)

db.session.add(dotnet)
db.session.commit()
