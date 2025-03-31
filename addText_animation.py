from manim import *

class AnimateSVG(Scene):
    def construct(self):
        # Load the SVG file
        svg_image = SVGMobject("2.svg")  # Replace with your file path

        # Optionally scale and position the SVG (it will retain its original colors)
        svg_image.scale(2)  # Scale the SVG
        svg_image.move_to(ORIGIN)  # Position the SVG at the center of the screen

        # Create the text to display below the SVG with a custom font
        text = Text("ASI SOLUTION", font="Arial")  # Replace with your desired text and font
        text.next_to(svg_image, DOWN)  #  Position the text below the SVG

        # Apply a color gradient to the text (e.g., from red to blue)
        text.set_color_by_gradient(GREEN, YELLOW, RED)

        # Display the SVG image and the text on screen
        self.play(DrawBorderThenFill(svg_image))  # Draw and fill the SVG
        self.play(Write(text))  # Write the text on the screen

        # Move both the SVG and the text with animation
        self.play(
            svg_image.animate.shift(UP),  # Move the SVG upwards
            text.animate.shift(UP)  # Move the text upwards along with the SVG
        )

        # Scale the SVG and text
        self.play(
            svg_image.animate.scale(0.5),  # Scale the SVG down
            text.animate.scale(0.5)  # Scale the text down
        )

        # Fade the SVG and text out (optional)
        self.play(FadeOut(svg_image), FadeOut(text))
