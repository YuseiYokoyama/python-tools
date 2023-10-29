import os

os.environ['NEW_KEY'] = 'test'
new_key = os.getenv("NEW_KEY")
print(os.environ['NEW_KEY'])
print(os.environ.get('NEW_KEY', 'default'))

os.makedirs("any/path", exist_ok=True)
