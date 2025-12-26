import pytest
from app import app


def test_header_present():
    """Test that the header is present in the app layout"""
    layout_children = app.layout.children

    # Find the header (it's in the first Div)
    header_div = layout_children[0]
    header = header_div.children[0]

    # Check it's an H1 element with correct text
    assert header.children == "Pink Morsel Sales Visualizer"
    print("✓ Header test passed!")


def test_visualization_present():
    """Test that the graph component is present"""
    layout_children = app.layout.children

    # The graph is in the third Div (index 2)
    chart_div = layout_children[2]
    graph = chart_div.children[0]

    # Check that the graph has the correct ID
    assert graph.id == "sales-chart"
    print("✓ Visualization test passed!")


def test_region_picker_present():
    """Test that the region picker is present"""
    layout_children = app.layout.children

    # The radio items are in the second Div (index 1)
    filter_div = layout_children[1]
    radio_items = filter_div.children[1]

    # Check that it's a RadioItems component
    assert radio_items.id == "region-filter"

    # Check all options are present
    options = [opt['value'] for opt in radio_items.options]
    assert 'all' in options
    assert 'north' in options
    assert 'east' in options
    assert 'south' in options
    assert 'west' in options
    print("✓ Region picker test passed!")