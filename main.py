from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Declare a mapping
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    age = Column(Integer)
    work = Column(String)

    def __repr__(self):
        return f'User(name= {self.name}, age={self.age}, work={self.work})'

# Create an engine that stores data in the local directory's 'example.db' file.
engine = create_engine('sqlite:///example.db')

# Create all tables
# Base.metadata.create_all(engine)
# Drop all tables and recreate them with the updated schema
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Define a list of users to add
users_to_add = [
    {'name': 'Sumar', 'age': 30, 'work': 'Artist'},
    {'name': 'Mike', 'age': 30, 'work': 'Engineer'},
    {'name': 'Alice', 'age': 28, 'work': 'Scientist'}
]
# Add a new user
existing_user = session.query(User).filter_by(name='name').first()
# Add users to the session
for user_data in users_to_add:
    existing_user = session.query(User).filter_by(name=user_data['name']).first()
    if existing_user:
        print(f"User with name {user_data['name']} already exists.")
    else:
        new_user = User(name=user_data['name'], age=user_data['age'], work=user_data['work'])
        session.add(new_user)
# Commit the session to save all new users
session.commit()
session.close()
