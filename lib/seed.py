from faker import Faker
from random import choice, randint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Dog

engine = create_engine("sqlite:///demo.db")

Session = sessionmaker(bind=engine)
session = Session()

faker = Faker()

def create_dogs(num):
    for x in range(num):

        breeds_list = [
            "Labrador", 
            "Irish Setter", 
            "Dauchshund", 
            "Cocker Spaniel", 
            "Border Terrier", 
            "Rhodesian Ridgeback", 
            "Golden Retriever", 
            "Whippet", 
            "Beagle", 
            "Cattle Dog", 
            "Kelpie", 
            "Chow Chow", 
            "German Shepherd", 
            "Border Collie", 
            "Basset Hound", 
            "Vizsla", 
            "Great Dane", 
            "Saint Bernard"
        ]

        new_dog = Dog (name=faker.first_name(), age=randint(1,20), breed=choice(breeds_list))
        
        session.add(new_dog)
        session.commit()

def delete_records():
    session.query(Dog).delete()

    session.commit()


if __name__ == "__main__":
    delete_records()
    create_dogs(20)
