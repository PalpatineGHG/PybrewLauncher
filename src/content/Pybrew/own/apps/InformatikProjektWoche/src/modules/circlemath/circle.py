import math

class Circle:
    class InvalidCircleError(Exception):
        """Exception raised when the provided radius and diameter do not match."""
        pass

    class InvalidAngleError(Exception):
        """Exception raised when the provided Angle isn't accurate"""
        pass

    def __init__(self, radius=None, diameter=None) -> None:
        """
        Initialize a Circle object.

        Parameters:
        radius (float): The radius of the circle (optional).
        diameter (float): The diameter of the circle (optional).

        If neither radius nor diameter are provided, defaults to radius=1.0 and diameter=2.0.\n
        If only radius is provided, calculates diameter as 2 * radius.\n
        If only diameter is provided, calculates radius as diameter / 2.\n
        If both are provided, checks if diameter is 2 * radius, else raises InvalidCircleError.
        """
        if radius is None and diameter is None:
            self.radius = 1.0
            self.diameter = 2.0
        elif radius is not None and diameter is None:
            self.radius = float(radius)
            self.diameter = 2 * self.radius
        elif radius is None and diameter is not None:
            self.diameter = float(diameter)
            self.radius = self.diameter / 2
        else:
            self.radius = float(radius)
            self.diameter = float(diameter)
            if self.diameter != 2 * self.radius:
                raise Circle.InvalidCircleError("Der Durchmesser muss doppelt so groß wie der Radius sein.")

    def __repr__(self) -> str:
        return f"Circle(radius={self.radius}, diameter={self.diameter})"

    def __str__(self) -> str:
        """
        Provide a user-friendly string representation of the circle.

        Returns:
        str: A string describing the circle's radius and diameter.
        """
        return f"Circle with radius {self.radius} and diameter {self.diameter}"

    def get(self, attribute) -> int | float:
        """
        Get the value of the specified attribute.

        Parameters:
        attribute (str): The name of the attribute ('radius' or 'diameter').

        Returns:
        float: The value of the specified attribute.

        Raises:
        AttributeError: If the attribute is not 'radius' or 'diameter'.
        """
        if attribute.lower() == 'radius':
            return self.radius
        elif attribute.lower() == 'diameter':
            return self.diameter
        else:
            raise AttributeError(f"'Circle' object has no attribute '{attribute}'")

    def changeAttr(self, attribute, value) -> None:
        """
        Change the value of the specified attribute.

        Parameters:
        attribute (str): The name of the attribute ('radius' or 'diameter').
        value (float): The new value of the attribute.

        Raises:
        AttributeError: If the attribute is not 'radius' or 'diameter'.
        """
        if attribute.lower() == 'radius':
            self.radius = float(value)
            self.diameter = 2 * self.radius
        elif attribute.lower() == 'diameter':
            self.diameter = float(value)
            self.radius = self.diameter / 2
        else:
            raise AttributeError(f"'Circle' object has no attribute '{attribute}'")

    def area(self) -> int | float:
        """
        Calculate the area of the circle.

        Returns:
        float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def circumference(self) -> int | float:
        """
        Calculate the circumference of the circle.

        Returns:
        float: The circumference of the circle.
        """
        return 2 * math.pi * self.radius

    def sin(self, angle) -> int | float:
        """
        Calculate the sine of a specific angle.

        Parameters:
        The angle to work with.

        Returns:
        float: The sine of a specific angle.
        """
        return math.sin(angle)

    def cos(self, angle) -> int | float:
        """
        Calculate the cosine of a specific angle.

        Parameters:
        The angle to work with.

        Returns:
        float: The cosine of a specific angle.
        """
        return math.cos(angle)
    
    def tan(self, angle) -> int | float:
        """
        Calculate the tangent of a specific angle.

        Parameters:
        The angle to work with.

        Returns:
        float: The tangent of a specific angle.
        """
        return math.tan(angle)

    def arc_length(self, angle) -> int | float:
        """
        Calculate the length of an arc on the circle for a given angle.

        Parameters:
        angle (float): The angle (in radians) defining the arc.

        Returns:
        float: The length of the arc.
        """
        return self.radius * angle

    def arc_length_slice(self, start_angle, end_angle) -> int | float:
        """
        Calculate the length of an arc on the circle between two angles.

        Parameters:
        start_angle (float): The starting angle (in radians) of the arc.
        end_angle (float): The ending angle (in radians) of the arc.

        Returns:
        float: The length of the arc.
        """
        # Normalize angles to be in the range [0, 2*pi)
        start_angle = start_angle % (2 * math.pi)
        end_angle = end_angle % (2 * math.pi)

        # Ensure end angle is greater than start angle
        if end_angle > start_angle:
            # Calculate the arc length
            arc_length = self.radius * (end_angle - start_angle)
            return arc_length
        else:
            raise circle.InvalidAngleError("Der Start Winkel muss kleiner sein als der Endwinkel")


# Beispielanwendung
if __name__ == "__main__":
    circle = Circle(radius=2, diameter=4)
    print(circle)
    print(f'Radius: {circle.get(attribute="radius")}')
    print(f'Diameter: {circle.get(attribute="diameter")}')
    print(f'Area: {circle.area()}')
    print(f'Circumference: {circle.circumference()}')
    print(f'Sin: {circle.sin(angle=45)}')
    print(f'Cos {circle.cos(angle=45)}')
    print(f'Tan: {circle.tan(angle=45)}')
    print(f'Arc-Length: {circle.arc_length(angle=45)}')
    print(f'Arc-Length-Slice {circle.arc_length_slice(start_angle=0, end_angle=45)}')
    print(circle)
