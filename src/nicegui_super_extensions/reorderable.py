from __future__ import annotations

import random

from nicegui import ui


class ReorderableItem(ui.card):
    """
    Represents a reorderable item that can be moved within a `ReorderableRow` or `ReorderableColumn`.
    """

    def __init__(self, enable_dragging: bool = True, drop_check_duration=3) -> None:
        """
        Initializes a `ReorderableItem`.

        Args:
            enable_dragging: Whether the item is reorderable. Defaults to True.
        """
        super().__init__()
        self.drag_enabled = enable_dragging
        self.drop_check_duration = drop_check_duration

        # Create the card with reorderable props and style
        with self.props("draggable").classes(f"cursor-pointer").style(
            "box-shadow: none;"
        ):
            self.build()

        # Set up event listeners for drag and drop
        self.on("dragstart", self.on_dragstart)
        self.on("dragenter", self.on_dragenter)
        self.on("dragleave", self.on_dragleave)
        self.on("dragover.prevent", self.on_dragover_prevent)
        self.on("drop", self.on_drop)

        # Disable dragging if not enabled
        if not self.drag_enabled:
            self.disable_drag()

    def disable_drag(self) -> None:
        """Disables dragging for this item."""
        self.drag_enabled = False
        self.classes(remove="cursor-pointer")
        self.props(remove="reorderable")

    def enable_drag(self) -> None:
        """Enables dragging for this item."""
        self.drag_enabled = True
        self.classes(add="cursor-pointer")
        self.props(add="reorderable")

    def get_parent(self) -> ReorderableColumn | ReorderableRow | None:
        """Returns the parent container (ReorderableColumn or ReorderableRow) of this item."""
        return self.parent_slot.parent  # type:ignore

    def delete_from_parent(self) -> None:
        """Removes this item from its parent container."""
        parent = self.get_parent()
        if parent is not None:
            parent.remove(self)

    def build(self) -> None:
        """
        Override this method to build the content of the reorderable card.
        """

    def on_dragstart(self) -> None:
        """
        Event handler for the 'dragstart' event.
        Highlights the dragged item and sets it as the currently dragged item.
        """
        if not self.drag_enabled:
            return
        global _dragged
        _dragged = self

    def on_drop_check(self) -> None:
        """
        Event handler for checking if the dragged item should be dropped.
        Removes the highlight from the dragged item and cancels the timer.
        """
        global _dragged
        if _dragged is not None:
            self.timer.cancel()

    def on_dragenter(self) -> None:
        """
        Event handler for the 'dragenter' event.
        Highlights the target item and sets a timer to check for dropping.
        """
        if not self.drag_enabled:
            return

        self.timer = ui.timer(self.drop_check_duration, self.on_drop_check)

    def on_dragleave(self) -> None:
        """
        Event handler for the 'dragleave' event.
        Removes the highlight from the target item and cancels the timer.
        """
        if not self.drag_enabled:
            return

        if hasattr(self, "timer"):
            self.timer.cancel()

    def on_drop(self) -> None:
        """
        Event handler for the 'drop' event.
        Moves the dragged item to the target position and resets the dragged item.
        """
        if not self.drag_enabled:
            return
        global _dragged
        if not _dragged:
            return

        parent = self.get_parent()
        if parent is None:
            return

        children = parent.get_reorderable_children()
        try:
            self_index = children.index(self)
        except ValueError:
            return

        _dragged.move(target_index=self_index)
        self.on_dragleave()

    def on_dragover_prevent(self):
        """Prevent default dragover event to allow drop event"""
        return


class ReorderableRow(ui.row):
    """
    Represents a row that can contain reorderable items.
    """

    def get_reorderable_children(self) -> list[ReorderableItem]:
        """
        Returns a list of reorderable items in this row.
        """
        children = []
        for i in self.default_slot.children:
            if issubclass(i.__class__, ReorderableItem):
                if i.drag_enabled:
                    children.append(i)
        return children

    def shuffle(self) -> None:
        """
        Shuffles the order of reorderable items in this row.
        """
        children = self.get_reorderable_children()
        random.shuffle(children)
        for i in children:
            i.move(target_index=0)


class ReorderableColumn(ui.column):
    """
    Represents a column that can contain reorderable items.
    """

    def get_reorderable_children(self) -> list[ReorderableItem]:
        """
        Returns a list of reorderable items in this column.
        """
        children = []
        for i in self.default_slot.children:
            if issubclass(i.__class__, ReorderableItem):
                if i.drag_enabled:
                    children.append(i)
        return children

    def shuffle(self) -> None:
        """
        Shuffles the order of reorderable items in this column.
        """
        children = self.get_reorderable_children()
        random.shuffle(children)
        for i in children:
            i.move(target_index=0)
