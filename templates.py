"""
* JOHN PRIME TEMPLATES
"""
# Standard Library Imports
from functools import cached_property
from typing import Optional

# Third Party Imports
from photoshop.api._artlayer import ArtLayer

# Local Imports
from src.templates import (
    BorderlessTemplate,
    MDFCTemplate,
    TransformTemplate, NormalTemplate
)
import src.helpers as psd
from src.enums.layers import LAYERS


class BorderlessShortTemplate (BorderlessTemplate):
    """
     * Borderless Template with short textbox.
     * Created by JohnPrime
    """
    template_suffix = "Borderless Short"


"""
MDFC TEMPLATES
"""


class BorderlessMDFCTemplate (MDFCTemplate):
    """
    * Borderless version of the MDFCTemplate.
    """
    template_suffix = "Borderless"

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_content_aware_enabled(self) -> bool:
        return True

    """
    LAYERS
    """

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        return

    """
    METHODS
    """

    def enable_crown(self) -> None:
        # No borders, no hollow crown
        psd.enable_mask(self.pinlines_layer.parent)
        self.crown_layer.visible = True


"""
TRANSFORM TEMPLATES
"""


class BorderlessTFTemplate (TransformTemplate):
    """
    * Borderless version of TransformTemplate.
    """
    template_suffix = "Borderless"

    @property
    def is_nyx(self) -> bool:
        return False

    @property
    def is_content_aware_enabled(self):
        return True

    @property
    def is_name_shifted(self) -> bool:
        return False

    """
    LAYERS / REFERENCES
    """

    @property
    def background_layer(self) -> Optional[ArtLayer]:
        # No backgrounds
        return

    @cached_property
    def pinlines_layer(self) -> Optional[ArtLayer]:
        # No land pinlines group
        return psd.getLayer(self.pinlines, LAYERS.PINLINES_TEXTBOX)

    @cached_property
    def pt_layer(self) -> Optional[ArtLayer]:
        # Group must be turned on if needed
        if self.is_creature:
            group = psd.getLayerSet(LAYERS.PT_BOX)
            group.visible = True
            return psd.getLayer(self.layout.twins, group)
        return

    """
    METHODS
    """

    def basic_text_layers(self):
        # Skip the Eldrazi black text step
        super(NormalTemplate, self).basic_text_layers()

    def enable_crown(self) -> None:
        # Crown group must be turned on first if front face
        if self.is_front:
            self.crown_layer.parent.visible = True

        # No borders, no hollow crown
        psd.enable_mask(self.pinlines_layer.parent)
        self.crown_layer.visible = True
