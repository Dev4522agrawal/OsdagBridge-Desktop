from osdagbridge_desktop.ui.docks.cad_cross_section import CrossSectionCADWidget
from osdagbridge_desktop.ui.dialogs.additional_input.drawings.support_conditions_cad import SupportCADWidget
from osdagbridge_desktop.ui.dialogs.additional_input.drawings.support_detail_cad import SupportDetailCADWidget
from osdagbridge_desktop.ui.dialogs.additional_input.drawings.cad_preview_widget import CadPreviewWidget
from osdagbridge_desktop.ui.dialogs.additional_input.ui_builder._segment_table_widget import SegmentTableWidget
from osdagbridge_desktop.ui.dialogs.additional_input.drawings.rolled_section_preview import RolledSectionPreview
from osdagbridge_desktop.ui.dialogs.additional_input.drawings.stiffener_details_cad import StiffenerDetailsCad
from osdagbridge_desktop.ui.dialogs.additional_input.drawings.end_diaphragm_cad import (
    CrossBracingLayoutCad,
    EndDiaphragmBracingLayoutCad,
    BracingSectionPreview,
    TopChordSectionPreview,
    BottomChordSectionPreview,
)
from osdagbridge_core.core.utils.common import (
    KEY_MP_CB_BOTTOM_CHORD_PREVIEW,
    KEY_MP_CB_BRACING_PREVIEW,
    KEY_MP_CB_TOP_CHORD_PREVIEW,
    KEY_MP_CB_TYPE_CAD_PREVIEW,
    KEY_MP_ED_BOTTOM_CHORD_PREVIEW,
    KEY_MP_ED_BRACING_LAYOUT_CAD,
    KEY_MP_ED_BRACING_SECTION_PREVIEW,
    KEY_MP_ED_ROLLED_PREVIEW,
    KEY_MP_ED_TOP_CHORD_PREVIEW,
    KEY_MP_GD_CAD_PREVIEW,
    KEY_MP_GD_SECTION_PREVIEW,
    KEY_MP_GD_SEGMENT_TABLE,
    KEY_SC_LEFT_CAD,
    KEY_SC_RIGHT_CAD,
    KEY_SD_STIFFENER_DETAILS,
    KEY_TS_CAD_PREVIEW,
    KEY_MP_ED_WELDED_PREVIEW
)

DIRECT_WIDGET_MAP = {

    # --------Typical-Section-Drwaing-Widgets------------------
    KEY_TS_CAD_PREVIEW: CrossSectionCADWidget,

    # --------Support-Condition-Drwaing-Widgets----------------
    KEY_SC_LEFT_CAD: SupportCADWidget,
    KEY_SC_RIGHT_CAD: SupportDetailCADWidget,

    # --------Girder-Details-Drwaing-Widgets-------------------
    KEY_MP_GD_CAD_PREVIEW: CadPreviewWidget,
    KEY_MP_GD_SEGMENT_TABLE: SegmentTableWidget,
    KEY_MP_GD_SECTION_PREVIEW: RolledSectionPreview,

    # --------Stiffener-Details-Drwaing-Widgets----------------
    KEY_SD_STIFFENER_DETAILS: StiffenerDetailsCad,

    # --------Cross-Bracing-Drwaing-Widgets--------------------
    KEY_MP_CB_TYPE_CAD_PREVIEW: CrossBracingLayoutCad,
    KEY_MP_CB_BRACING_PREVIEW: BracingSectionPreview,
    KEY_MP_CB_TOP_CHORD_PREVIEW: TopChordSectionPreview,
    KEY_MP_CB_BOTTOM_CHORD_PREVIEW: BottomChordSectionPreview,

    # --------End-Diaphragm-Drwaing-Widgets--------------------
    KEY_MP_ED_BRACING_LAYOUT_CAD: EndDiaphragmBracingLayoutCad,
    KEY_MP_ED_BRACING_SECTION_PREVIEW: BracingSectionPreview,
    KEY_MP_ED_TOP_CHORD_PREVIEW: TopChordSectionPreview,
    KEY_MP_ED_BOTTOM_CHORD_PREVIEW: BottomChordSectionPreview,
    KEY_MP_ED_ROLLED_PREVIEW: RolledSectionPreview,
    KEY_MP_ED_WELDED_PREVIEW: RolledSectionPreview,

}