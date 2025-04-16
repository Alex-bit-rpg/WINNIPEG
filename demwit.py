class Superhero:
    """
    Represents a superhero with a name, secret identity, powers, and current energy level.
    """
    def __init__(self, name, secret_identity, powers, energy=100):
        """
        Constructor to initialize a Superhero object.

        Args:
            name (str): The superhero's public name.
            secret_identity (str): The superhero's hidden identity.
            powers (list): A list of the superhero's abilities.
            energy (int): The current energy level of the superhero (default: 100).
        """
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers
        self.energy = energy

    def reveal_identity(self):
        """Prints the superhero's secret identity (for authorized personnel only!)."""
        print(f"Attention! {self.name}'s secret identity is: {self.secret_identity}")

    def use_power(self, power_name):
        """
        Attempts to use a specified power, reducing energy if successful.

        Args:
            power_name (str): The name of the power to use.
        """
        if power_name in self.powers:
            if self.energy >= 20:  # Example energy cost
                print(f"{self.name} uses {power_name}!")
                self.energy -= 20
                print(f"Energy remaining: {self.energy}")
            else:
                print(f"{self.name} is too tired to use {power_name}.")
        else:
            print(f"{self.name} doesn't have the power: {power_name}.")

    def recharge(self, amount=30):
        """
        Increases the superhero's energy level.

        Args:
            amount (int): The amount of energy to recharge (default: 30).
        """
        self.energy = min(100, self.energy + amount)
        print(f"{self.name} recharged. Current energy: {self.energy}")

    def display_info(self):
        """Displays the public information about the superhero."""
        print(f"Superhero Name: {self.name}")
        print(f"Powers: {', '.join(self.powers)}")
        print(f"Current Energy: {self.energy}")

class FlyingSuperhero(Superhero):
    """
    Represents a superhero with the additional ability to fly.
    Inherits from the Superhero class.
    """
    def __init__(self, name, secret_identity, powers, max_altitude, energy=100):
        """
        Constructor for FlyingSuperhero, calling the parent's constructor and adding max_altitude.

        Args:
            name (str): The superhero's public name.
            secret_identity (str): The superhero's hidden identity.
            powers (list): A list of the superhero's abilities.
            max_altitude (int): The maximum flying altitude.
            energy (int): The current energy level (default: 100).
        """
        super().__init__(name, secret_identity, powers, energy)
        self.max_altitude = max_altitude

    def fly(self, altitude):
        """
        Simulates the superhero flying to a certain altitude.

        Args:
            altitude (int): The desired flying altitude.
        """
        if self.energy >= 15: # Example energy cost for flying
            if altitude <= self.max_altitude:
                print(f"{self.name} is flying at {altitude} meters.")
                self.energy -= 15
                print(f"Energy remaining: {self.energy}")
            else:
                print(f"{self.name} cannot fly that high! Maximum altitude: {self.max_altitude} meters.")
        else:
            print(f"{self.name}")