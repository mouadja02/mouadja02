# Profile artwork

The profile follows the portfolio at [mouadja02.github.io](https://mouadja02.github.io/): an IC datasheet for part MJ02. The header is the datasheet's title block, with a noisy signal cleaned up by a pipeline and a model. The pinout shows the tech stack as a 20-pin package.

- Light: paper `#eef0df`, sheet `#e5e9d3`, ink `#15201b`, red pen `#d93c16`.
- Dark: paper `#0d1310`, sheet `#131b17`, ink `#dee5d5`, amber `#ffb224`.
- Typography: system sans and monospace stacks. GitHub serves README images without web fonts, so the drawings name no font that has to be installed.

All six SVGs are generated. To change a label, a colour or the pin list, edit `build.py` and run:

```bash
python3 assets/build.py
```

The README picks desktop or mobile artwork, each in light and dark, with a `picture` element. There are no scripts, animations or remote image services. Identity and the pin list also appear in each image's alternative text.
