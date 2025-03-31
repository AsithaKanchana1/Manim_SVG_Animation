from manim import *

class AnimateSVG(Scene):
    def construct(self):
        # Load the SVG file
        svg_image = SVGMobject("2.svg")  # Replace with your file path

        # Optionally scale and position the SVG (it will retain its original colors)
        svg_image.scale(2)  # Scale the SVG
        svg_image.move_to(ORIGIN)  # Position the SVG at the center of the screen

        # Display the SVG image on screen
        self.play(DrawBorderThenFill(svg_image))  # Draw and fill the SVG

        # Additional animations (optional)
        self.play(svg_image.animate.shift(UP))  # Move the image upwards
        self.play(svg_image.animate.scale(0.5))  # Scale the image down

        # Fade the SVG out (optional)
        self.play(FadeOut(svg_image))
