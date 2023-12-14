from dataclasses import dataclass


@dataclass
class Palette:
    DARK_PRIMARY_COLOR: str = '#00796B'
    LIGHT_PRIMARY_COLOR: str = "#B2DFDB"
    PRIMARY_COLOR: str = "#009688"
    TEXT_ICON: str = "#FFFFFF"
    ACCENT_COLOR: str = "#7C4DFF"
    PRIMARY_TEXT: str = "#212121"
    SECONDARY_TEXT: str = "#757575"
    DIVIDER_COLOR: str = "#BDBDBD"
