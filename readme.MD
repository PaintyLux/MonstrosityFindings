This project is intended to largely be a scratchpad for finding out the workings of the Monstrosity system in Final Fantasy XI and how it interacts with the different systems in game.

Results will hopefully be used in order to contribute to the [LandSandBoat Project](https://github.com/LandSandBoat/server).

Information is gathered from multiple sources:
- [BG-Wiki](https://www.bg-wiki.com/ffxi/Category:Monstrosity)
- [FFXIclopedia](https://ffxiclopedia.fandom.com/wiki/Category:Monstrosity)
- The [LandSandBoat Project](https://github.com/LandSandBoat/server)
- [Operation Bluffalo](https://docs.google.com/spreadsheets/d/1i-Z4A4GLfhvKg_3QFQDA9WZ-M8Gb-g1v_KyHNa24G7s/edit?gid=228593342#gid=228593342)
- In-game via plain elbow grease
    - [messier google sheet scratchpad for number crunching](https://docs.google.com/spreadsheets/d/1U0dBUXZXej28SvlB05UOqDFq8slSGWhyG37EAfupS9Q/edit?usp=sharing)

# Documentation

Some of the files (e.g. monster data tables) are generated from the `.yaml` files contained in the `/yaml` directory using [pyyaml](https://github.com/yaml/pyyaml/).

### Setup

To install the required libraries (via `pip`), run the following command:

```
pip install -r requirements.txt
```

After this is installed, run the following command to regenerate the monster data files:

```
python generate.py
```