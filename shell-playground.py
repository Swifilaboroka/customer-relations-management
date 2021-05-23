# run in django shell
# exec(open('shell-playground.py').read())

from leads.models import Lead, Agent
from django.contrib.auth import get_user_model

User = get_user_model()

# user = User.objects.create_user('deeznuts@gmail.com', 'deeznuts')
# print(user)

# user = User.objects.filter().first()
print(User.objects.all())
# id = user.id
# agent = Agent.objects.create(user_id=id)
# print(agent)

# agent = Agent.objects.filter().first()
# print(agent)
# print(agent.id)


# lead = Lead.objects.create(first_name="Joe", last_name="Mama", age=35, agent_id=agent.id)

# lead = Lead.objects.filter().first()
# print(lead)
# print(Lead.objects.all())
# agent = None
# lead.delete()

# user = User.objects.filter().first()
# second = User.objects.filter()[1]
# print(user)
# print(second)
# print(user.date_joined)
# print(second.date_joined)

# from django.urls import reverse
# print(reverse("hahahahahanamespace:list"))

# print(Lead.objects.all())
# print(Lead.objects.get(pk=9))
