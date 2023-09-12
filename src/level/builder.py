from src.configs.settings import TILESIZE


class LevelMapBuilder:

    def __init__(self, layouts):
        self._layouts = layouts

    def build(self, builders):
        for style, layout in self._layouts.items():
            for y_index, row in enumerate(layout):
                y = y_index * TILESIZE
                for x_index, col in enumerate(row):
                    if col != "-1":
                        x = x_index * TILESIZE
                        builders[style]((x, y), col)
