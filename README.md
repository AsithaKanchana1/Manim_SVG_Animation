# Animate SVG with Manim

This script uses the **Manim** library to animate an SVG file. The SVG is loaded, colored, scaled, and displayed with animations such as shifting and scaling. This README provides instructions on how to set up and run the script.

![Animation Preview](doc/manimLogo.svg)

<video src="https://github.com/AsithaKanchana1/Manim_SVG_Animation/raw/main/doc/video.mp4" controls="controls" style="max-width: 720px;"></video>

## Prerequisites

Before running the script, make sure you have the following installed:

1. **Python 3.7+**  
   This script requires Python 3.7 or later. You can download it from [python.org](https://www.python.org/downloads/).

2. **Manim**  
   Manim is a community-maintained library used for creating animations. To install it, run the following command in your terminal or command prompt:

   ```bash
   pip install manim
   ```

3. **FFmpeg**  
   FFmpeg is used by Manim to handle video rendering. You can download it from [ffmpeg.org](https://ffmpeg.org/download.html). After installation, make sure that FFmpeg is added to your system's `PATH`.

   But if you are using this only for image animation dont need this.

4. **SVG File**  
   You need an SVG file to animate. Ensure the SVG file is in the same directory as the script or update the path in the script accordingly.

## Setting Up the Script

1. Clone or download this repository.

2. Place your SVG file (e.g., `2.svg`) in the same directory as `animation.py`.

3. Open the script in a text editor (e.g., VSCode, Sublime Text) and ensure that the SVG file path is correct. If the SVG file is located in a different directory, update the path in the `SVGMobject` constructor.

   ```python
   svg_image = SVGMobject("2.svg")  # Adjust the path if necessary
   ```

## Running the Script

Once you have set everything up, you can run the script from the command line.

1. Navigate to the directory containing `animation.py` and the SVG file.

2. Run the following command to render the animation:

   ```bash
   python -m manim animation.py AnimateSVG
   ```

   This will generate a video file in the `media` folder created by Manim.

### Understanding the Command

- `python -m manim`: This is the Manim command-line interface.
- `animation.py`: This is the name of the script containing your scene.
- `AnimateSVG`: This is the name of the scene class that Manim will render.

### Output

The animation will be rendered and saved in the `media` folder (or the directory set in your Manim configuration). The output video will be in the `videos` subfolder of the `media` directory.

## Customizing the Script

You can customize the colors and behavior of the SVG in the script:

- **Change the Color of the SVG**:
  Modify the line:
  ```python
  svg_image.set_color(WHITE)
  ```
  Replace `WHITE` with any of the following colors: `RED`, `GREEN`, `BLUE`, `YELLOW`, `ORANGE`, `PURPLE`, etc. You can also use color gradients, such as:
  ```python
  svg_image.set_color_by_gradient(RED, BLUE)
  ```

- **Scaling and Positioning**:
  Adjust the scale and position of the SVG with the following lines:
  ```python
  svg_image.scale(2)  # Change the scaling factor
  svg_image.move_to(ORIGIN)  # Change the positioning
  ```

- **Animations**:
  You can add more animations to your SVG by modifying the `self.play()` function. For example, to rotate the SVG, add:
  ```python
  self.play(Rotate(svg_image, angle=PI))
  ```

## Troubleshooting

- **Error: File Not Found**: Make sure the path to the SVG file is correct.
- **FFmpeg not found**: Ensure that FFmpeg is installed and added to your system's `PATH`. For Windows users, check that the `bin` folder of FFmpeg is in the `PATH` environment variable.

## Contacts 

You can reach me via Email : [asitha.contact.me](mailto:asitha.contact.me@gmail.com)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
