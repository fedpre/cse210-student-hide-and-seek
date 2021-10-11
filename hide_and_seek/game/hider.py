import random

# TODO: Define the Hider class here

class Hider:
    """A code template for the hider who escapes the Hider. The 
    responsibility of this class of objects is to hide in a specific location from the Hider.
    
    Stereotype:
        Information Holder

    Attributes:
        location (integer): The location of the Hider (1-1000).
        distance (list): The distance travelled with each move.
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Hider): An instance of Hider.
        """
        self.location = random.randint(1, 1000)
        self.distance = [0, 0]
    
    def get_hint(self):
        """The get_hint method returns a hint that depends on whether or not the seeker has moved closer or farther away. This is determined by inspecting the last two distances contained in the distance attribute.

        Gets a message for the seeker from the hider.
            
        Returns:
            string: A message for the seeker from the hider.
        
        Args:
            self (Hider): An instance of the Hider
        
        """
        print(self.location)
        message = "(;.;) You found me!\n"
        if self.distance[-1] == 0:
            message = "(;.;) You found me!\n"
        elif self.distance[-1] < self.distance[-2]:
            message = "(>.<) Getting warmer!"
        elif self.distance[-1] > self.distance[-2]:
            message = "(^.^) Getting colder!"
        return message



    def watch(self, location):
        """The watch method keeps track of how far away the Hider is by calculating the difference between their locations. The distance is appended to the corresponding attribute for later use.
        
        Args:
            self (Hider): An instance of the Hider
            location: The last location of the Seeker
        """
        current_distance = abs(self.location - location)
        self.distance.append(current_distance)



    

