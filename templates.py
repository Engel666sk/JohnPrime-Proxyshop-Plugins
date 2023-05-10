"""
JOHNPRIME TEMPLATES
"""
# Standard Library Imports
from functools import cached_property
from typing import Optional

# Third Party Imports
from photoshop.api._artlayer import ArtLayer

# Local Imports
from src import templates as temp
from src.settings import cfg
import src.helpers as psd
from src.utils.enums_layers import LAYERS


class WomensdayShortTemplate (temp.WomensDayTemplate):
    """
     * Womensday Short Template
     * Created by JohnPrime
    """
    template_suffix = "Showcase Short"

    def __init__(self, layout):
        cfg.remove_flavor = True
        super().__init__(layout)


"""
MDFC TEMPLATES
"""


class BorderlessMDFCTemplate (temp.MDFCTemplate):
    """
    Borderless version of the MDFC Back template
    """
    template_suffix = "Showcase"

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def is_nyx(self) -> bool:
        return False

    @cached_property
    def art_reference_layer(self) -> ArtLayer:
        # Only Full Art reference
        return psd.getLayer(LAYERS.FULL_ART_FRAME)

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        # No backgrounds
        return

    def enable_crown(self) -> None:
        # No borders, no nyx, no companion
        psd.enable_mask(self.pinlines_layer.parent)
        self.crown_layer.visible = True

    def load_artwork(self):
        super().load_artwork()

        # Content aware fill
        psd.content_fill_empty_area(self.art_layer)


"""
TRANSFORM TEMPLATES
"""


class BorderlessTFTemplate (temp.TransformTemplate):
    """
    Template for the back faces of transform cards.
    """
    template_suffix = "Borderless"

    @property
    def is_companion(self) -> bool:
        return False

    @property
    def is_nyx(self) -> bool:
        return False

    @cached_property
    def text_layer_name(self) -> Optional[ArtLayer]:
        # CARD NAME
        return psd.getLayer(LAYERS.NAME, self.text_layers)

    @cached_property
    def art_reference_layer(self) -> ArtLayer:
        # Only Full Art reference
        return psd.getLayer(LAYERS.FULL_ART_FRAME)

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        # No backgrounds
        return

    @cached_property
    def pinlines_layer(self) -> Optional[ArtLayer]:
        # No land pinlines group
        return psd.getLayer(self.layout.pinlines, LAYERS.PINLINES_TEXTBOX)

    @cached_property
    def pt_layer(self) -> Optional[ArtLayer]:
        # Group must be turned on if needed
        if self.is_creature:
            group = psd.getLayerSet(LAYERS.PT_BOX)
            group.visible = True
            return psd.getLayer(self.layout.twins, group)
        return

    def enable_crown(self) -> None:
        # Crown group must be turned on first if front face
        if self.is_front:
            self.crown_layer.parent.visible = True

        # No borders, no nyx, no companion
        psd.enable_mask(self.pinlines_layer.parent)
        self.crown_layer.visible = True

    def load_artwork(self):
        super().load_artwork()

        # Content aware fill
        psd.content_fill_empty_area(self.art_layer)
