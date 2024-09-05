from modules.otherprintfuncs.printfuncs import *
from modules.circlemath.circle import *
from modules.math.pymath import *
import os


class PrintApp:
    @staticmethod
    def allprint(selection: int = 0, text: str = "Hello World") -> None:
        if selection == 0:
            print(text)  # Python print()-function
        elif selection == 1:
            printf(text)  # C print()-function
        elif selection == 2:
            System.out.printIn(text)  # Java print()-function
        elif selection == 3:
            console.log(text)  # JavaScript print()-function
        elif selection == 4:
            Console.WriteLine(text)  # C# print()-function
        elif selection == 5:
            printIn(text)  # Scala print()-function
        elif selection == 6:
            puts(text)  # Ruby print()-function
        elif selection == 7:
            echo(text)  # PHP print()-function
        elif selection == 8:
            print_r(text)  # Also PHP print()-function
        elif selection == 9:
            print_with_newline(text)  # Perl print()-function
        else:
            print("Not implemented!")


class CircleApp:
    @staticmethod
    def run():
        circle = Circle(radius=2, diameter=4)
        print(circle)
        print(f'Radius: {circle.get(attribute="radius")}')
        print(f'Diameter: {circle.get(attribute="diameter")}')
        print(f'Area: {circle.area()}')
        print(f'Circumference: {circle.circumference()}')
        print(f'Sin: {circle.sin(angle=45)}')
        print(f'Cos: {circle.cos(angle=45)}')
        print(f'Tan: {circle.tan(angle=45)}')
        print(f'Arc-Length: {circle.arc_length(angle=45)}')
        print(f'Arc-Length-Slice {circle.arc_length_slice(start_angle=0, end_angle=45)}')
        print(circle)


class MathApp:
    @staticmethod
    def run():
        math = Math()
        print(math.add(1, 2, 3))
        print(math.subtract(1, 2, 3))
        print(math.multiply(1, 2, 3))
        print(math.divide(1, 2, 3))
        print(math.root(2, 2))
        print(math.sqrt(2))
        print(math.pythagoras(3, 3))
        print(math.multiply(1, math.Constantes.pi))
        print(math.Constantes())


def main():
    mathapp = MathApp()
    mathapp.run()

if __name__ == '__main__':
    main()
    os.system('pause')  # Hält die Konsole offen, bis eine Taste gedrückt wird