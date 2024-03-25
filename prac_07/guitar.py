CURRENT_YEAR = 2023
VINTAGE_YEAR = 50


class Guitar:
    """Represent a guitar object."""
    def __int__(self, name="", year=0, cost=0.0):
        """Initialize a guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of a guitar."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __rep__(self):
        """Return string representation of a guitar."""
        return f"{self.name} {self.year} {self.cost}"

    def get_age(self):
        """Get the guitar's age."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Check if the guitar is vintage or not."""
        return self.get_age() >= VINTAGE_YEAR

    def __lt__(self, other):
        return self.year < other.year