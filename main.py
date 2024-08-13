from database_setup import initialize_db
from operations import add_road, get_all_roads
from visualization import visualize_conditions

def main():
    # Initialize the database
    initialize_db()
    
    # Add some roads
    add_road('Main St', 5.2, 'Good', '2024-01-15')
    add_road('Second St', 3.5, 'Fair', '2023-11-23')
    add_road('Third St', 7.8, 'Poor', '2022-09-05')
    
    # Retrieve and print all roads
    roads = get_all_roads()
    for road in roads:
        print(road)
    
    # Visualize road conditions
    visualize_conditions()

if __name__ == "__main__":
    main()
