from datetime import datetime,timezone
from .app import db,app
from .models.pizza import Pizza
from .models.restaurant import Restaurant
from .models.restaurant_pizza import RestaurantPizza
#Seed Database
#Seed Pizza Table 

#pizza's sample data.
pizzas = [
    {
        'name': 'Margherita',
        'ingredients': ['Tomato Sauce', 'Mozzarella Cheese', 'Basil'],
        'created_at': datetime.now(timezone.utc),
        'updated_at': datetime.now(timezone.utc),
    },
    {
        'name': 'Pepperoni',
        'ingredients': ['Tomato Sauce', 'Mozzarella Cheese', 'Pepperoni'],
        'created_at': datetime.now(timezone.utc),
        'updated_at': datetime.now(timezone.utc),
    },
    {
        'name': 'Vegetarian',
        'ingredients': ['Tomato Sauce', 'Mozzarella Cheese', 'Bell Peppers', 'Mushrooms', 'Onions'],
        'created_at': datetime.now(timezone.utc),
        'updated_at': datetime.now(timezone.utc),
    },
    {
        'name': 'BBQ Chicken',
        'ingredients': ['BBQ Sauce', 'Mozzarella Cheese', 'Grilled Chicken', 'Red Onions', 'Cilantro'],
        'created_at': datetime.now(timezone.utc),
        'updated_at': datetime.now(timezone.utc),
    },
    {
        'name': 'Seafood Delight',
        'ingredients': ['Garlic Butter Sauce', 'Mozzarella Cheese', 'Shrimp', 'Calamari', 'Mussels'],
        'created_at': datetime.now(timezone.utc),
        'updated_at': datetime.now(timezone.utc),
    }
]



#Restaurant Seed Data 
restaurants=[
    {
       
        'name': 'Mama Stella’s Pizzeria',
        'address': '123 Pizza Lane, Eldoret',
        'created_at': datetime.now(timezone.utc),
        'updated_at': datetime.now(timezone.utc),
    },
    {
        
        'name': 'The Dough House',
        'address': '456 Crust Ave, Nairobi',
        'created_at': datetime.now(timezone.utc),
        'updated_at': datetime.now(timezone.utc),
    },
    {
        
        'name': 'Slice of Heaven',
        'address': '789 Mozza St, Mombasa',
        'created_at':datetime.now(timezone.utc),
        'updated_at':datetime.now(timezone.utc),
    },
    {
        
        'name': 'Crust & Craft',
        'address': '321 Bake Blvd, Kisumu',
        'created_at': datetime.now(timezone.utc),
        'updated_at': datetime.now(timezone.utc),
    },
    {
      
        'name': 'The Rustic Oven',
        'address': '654 Tomato Rd, Nakuru',
        'created_at': datetime.now(timezone.utc),
        'updated_at':datetime.now(timezone.utc),
    }
]
 

 #RestaurantPizza Seed Data
restaurantpizzas=[
    {
        
        'prize': 8,
        'restaurant_id': 1,
        'pizza_id': 2,
        'created_at': datetime.now(timezone.utc),
        'updated_at': datetime.now(timezone.utc),
    },
    {
        
        'prize': 6,
        'restaurant_id': 1,
        'pizza_id': 1,
        'created_at': datetime.now(timezone.utc),
        'updated_at':datetime.now(timezone.utc),
    },
    {
      
        'prize': 9,
        'restaurant_id': 2,
        'pizza_id': 3,
        'created_at': datetime.now(timezone.utc),
        'updated_at': datetime.now(timezone.utc),
    },
    {
       
        'prize': 7,
        'restaurant_id': 3,
        'pizza_id': 4,
        'created_at': datetime.now(timezone.utc),
        'updated_at': datetime.now(timezone.utc),
    },
    {
       
        'prize': 5,
        'restaurant_id': 4,
        'pizza_id': 5,
        'created_at': datetime.now(timezone.utc),
        'updated_at': datetime.now(timezone.utc),
    },
    {
       
        'prize': 10,
        'restaurant_id': 5,
        'pizza_id': 1,
        'created_at': datetime.now(timezone.utc),
        'updated_at': datetime.now(timezone.utc),
    },
    {
      
        'prize': 4,
        'restaurant_id': 5,
        'pizza_id': 2,
        'created_at': datetime.now(timezone.utc),
        'updated_at': datetime.now(timezone.utc),
    }
]

with app.app_context():
    #Reset Data to avoid adding duplicates records 
    db.session.execute(db.text('TRUNCATE TABLE restaurantpizzas RESTART IDENTITY CASCADE'))
    db.session.execute(db.text('TRUNCATE TABLE restaurants RESTART IDENTITY CASCADE'))
    db.session.execute(db.text('TRUNCATE TABLE restaurants RESTART IDENTITY CASCADE'))
    db.session.commit()

    # Insert dummy records to respective tables in Database 
    #Pizza Table 
    for pizza in pizzas:
        pizza_record=pizza = Pizza(
        name=pizza.get('name'),
        ingredients=['Tomato Sauce', 'Mozzarella Cheese', 'Basil'],
        created_at=pizza.get('created_at'),
        updated_at=pizza.get('updated_at'))
        db.session.add(pizza_record)

    #Restaurant Table
    for restaurant in restaurants:
        restaurant_record =Restaurant(
        name=restaurant.get('name'),
        address=restaurant.get('address'),
        created_at=restaurant.get('created_at'),
        updated_at=restaurant.get('updated_at'))
        db.session.add(restaurant_record)
    

    #RestaurantPizza
    for restaurantpizza in restaurantpizzas:
        restaurantpizza_record = RestaurantPizza(
            prize=restaurantpizza.get('prize'),
            restaurant_id=restaurantpizza.get('restaurant_id'),
            pizza_id=restaurantpizza.get('pizza_id'),
            created_at=restaurantpizza.get('created_at'),
            updated_at=restaurantpizza.get('updated_at'),
        )
        db.session.add(restaurantpizza_record)
    
    db.session.commit()

                                                                        
    