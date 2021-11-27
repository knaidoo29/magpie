import numpy as np
import magpie


def test_is_pos_monotonic():
    arr = np.linspace(0., 100., 100)
    assert magpie.utils.is_pos_monotonic(arr) is True, "Array should be recognised as positively monotonic."
    arr = np.linspace(0., 100., 100)[::-1]
    assert magpie.utils.is_pos_monotonic(arr) is False, "Array should be recognised as not positively monotonic."


def test_progress_bar():
    length = 10
    for index in range(length):
        magpie.utils.progress_bar(index, length, explanation=None, indexing=False,
                                  num_refresh=50, marker_done="#", marker_undone="_", bar_edges="|",
                                  bar_edge_left=None, bar_edge_right=None, bar_length=50)
    for index in range(length):
        magpie.utils.progress_bar(index, length, explanation='Test', indexing=False,
                                  num_refresh=50, marker_done="#", marker_undone="_", bar_edges="|",
                                  bar_edge_left=None, bar_edge_right=None, bar_length=50)
    for index in range(length):
        magpie.utils.progress_bar(index, length, explanation=None, indexing=True,
                                  num_refresh=50, marker_done="#", marker_undone="_", bar_edges="|",
                                  bar_edge_left=None, bar_edge_right=None, bar_length=50)
    for index in range(length):
        magpie.utils.progress_bar(index, length, explanation=None, indexing=False,
                                  num_refresh=50, marker_done="#", marker_undone="_", bar_edges="|",
                                  bar_edge_left=None, bar_edge_right='test', bar_length=50)
    for index in range(length):
        magpie.utils.progress_bar(index, length, explanation=None, indexing=False,
                                  num_refresh=50, marker_done="#", marker_undone="_", bar_edges="|",
                                  bar_edge_left='test', bar_edge_right=None, bar_length=50)
