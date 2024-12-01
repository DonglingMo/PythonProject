unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f'Confirmed user: {current_user}')
    confirmed_users.append(current_user)

for user in confirmed_users:
    print(f'Confirmed user: {user}')