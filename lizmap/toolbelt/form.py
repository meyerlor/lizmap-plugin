"""Utilities for inspecting QGIS drag & drop form layouts."""

from qgis.core import (
    QgsAttributeEditorContainer,
    QgsAttributeEditorRelation,
    QgsRelationManager,
)


def form_has_relation_widget(node, relation_manager: QgsRelationManager) -> bool:
    """Return True if *node* or any descendant is a valid QgsAttributeEditorRelation.

    When a relation widget is placed inside a Tab or GroupBox in a DnD form,
    Lizmap's maptip generator creates a ``popup_lizmap_dd_relation`` placeholder
    div at that position.  LWC then fills that div with child-feature content
    when ``popupDisplayChildren`` is enabled.

    This helper lets the desktop plugin detect that setup so it can guide or
    auto-configure the user accordingly.
    """
    if isinstance(node, QgsAttributeEditorRelation):
        node.init(relation_manager)
        return node.relation().isValid()
    if isinstance(node, QgsAttributeEditorContainer):
        return any(form_has_relation_widget(child, relation_manager) for child in node.children())
    return False
