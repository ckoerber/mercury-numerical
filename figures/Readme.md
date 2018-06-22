# Creation of Animations
The script `animation.py` is used to create multiple `.png`s which are combined to a `.gif` by `png2gif.sh`.

# Description
The script `animation.py` runs the simulation and periodically makes screenshots which are exported to the `files/` directory.
Note that the screenshot `bbox` depends on the display and browser of choice.
Here one has to select a proper range of screenshots in order to have a smooth gif.
The unwanted `.png`s must be delteted.
Once this is done one can run `png2gif.sh` which converts the `.png`s to an optimized `.gif` file.


## Selected `.png` ranges
* `alpha = 0`: from `perihelion_0084.png` to `perihelion_0166.png`
* `alpha = 1.e6`: from `perihelion_0001.png` to `perihelion_0228.png`

# Dependencies
* `animation.py`
  * `Vpython`
  * `PIL`
* `png2gif.sh`
  * `convert`
  * `gifsicle`
