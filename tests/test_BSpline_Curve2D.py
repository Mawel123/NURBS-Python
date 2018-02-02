"""
    Tests for the NURBS-Python package
    Released under The MIT License. See LICENSE file for details.
    Copyright (c) 2018 Onur Rauf Bingol

    Tests geomdl.BSpline.Curve2D module. Requires "pytest" to run.
"""
from geomdl import BSpline

GEOMDL_DELTA = 0.001
OBJECT_INSTANCE = BSpline.Curve2D
CONTROL_POINTS = [[5.0, 5.0], [10.0, 10.0], [20.0, 15.0], [35.0, 15.0], [45.0, 10.0], [50.0, 5.0]]


def test_bspline_curve2d_degree():
    # Create a curve instance
    curve = OBJECT_INSTANCE()

    # Set curve degree
    curve.degree = 3

    assert curve.degree == 3


def test_bspline_curve2d_ctrlpts():
    # Create a curve instance
    curve = OBJECT_INSTANCE()

    # Set curve degree
    curve.degree = 3

    # Set control points
    curve.ctrlpts = [[5.0, 5.0], [10.0, 10.0], [20.0, 15.0], [35.0, 15.0], [45.0, 10.0], [50.0, 5.0]]

    assert curve.ctrlpts == ((5.0, 5.0), (10.0, 10.0), (20.0, 15.0), (35.0, 15.0), (45.0, 10.0), (50.0, 5.0))


def test_bspline_curve2d_knot_vector():
    # Create a curve instance
    curve = OBJECT_INSTANCE()

    # Set curve degree
    curve.degree = 3

    # Set control points
    curve.ctrlpts = [[5.0, 5.0], [10.0, 10.0], [20.0, 15.0], [35.0, 15.0], [45.0, 10.0], [50.0, 5.0]]

    # Set knot vector
    curve.knotvector = [0.0, 0.0, 0.0, 0.0, 0.33, 0.66, 1.0, 1.0, 1.0, 1.0]

    assert curve.knotvector == (0.0, 0.0, 0.0, 0.0, 0.33, 0.66, 1.0, 1.0, 1.0, 1.0)


def test_bspline_curve2d_eval1():
    # Create a curve instance
    curve = OBJECT_INSTANCE()

    # Set curve degree
    curve.degree = 3

    # Set control points
    curve.ctrlpts = CONTROL_POINTS

    # Set knot vector
    curve.knotvector = [0.0, 0.0, 0.0, 0.0, 0.33, 0.66, 1.0, 1.0, 1.0, 1.0]

    # Evaluate curve
    evalpt = curve.curvept(0.0)

    # Evaluation result
    res = [5.0, 5.0]

    assert abs(evalpt[0] - res[0]) < GEOMDL_DELTA
    assert abs(evalpt[1] - res[1]) < GEOMDL_DELTA


def test_bspline_curve2d_eval2():
    # Create a curve instance
    curve = OBJECT_INSTANCE()

    # Set curve degree
    curve.degree = 3

    # Set control points
    curve.ctrlpts = CONTROL_POINTS

    # Set knot vector
    curve.knotvector = [0.0, 0.0, 0.0, 0.0, 0.33, 0.66, 1.0, 1.0, 1.0, 1.0]

    # Evaluate curve
    evalpt = curve.curvept(0.3)

    # Evaluation result
    res = [18.617, 13.377]

    assert abs(evalpt[0] - res[0]) < GEOMDL_DELTA
    assert abs(evalpt[1] - res[1]) < GEOMDL_DELTA


def test_bspline_curve2d_eval3():
    # Create a curve instance
    curve = OBJECT_INSTANCE()

    # Set curve degree
    curve.degree = 3

    # Set control points
    curve.ctrlpts = CONTROL_POINTS

    # Set knot vector
    curve.knotvector = [0.0, 0.0, 0.0, 0.0, 0.33, 0.66, 1.0, 1.0, 1.0, 1.0]

    # Evaluate curve
    evalpt = curve.curvept(0.5)

    # Evaluation result
    res = [27.645, 14.691]

    assert abs(evalpt[0] - res[0]) < GEOMDL_DELTA
    assert abs(evalpt[1] - res[1]) < GEOMDL_DELTA


def test_bspline_curve2d_eval4():
    # Create a curve instance
    curve = OBJECT_INSTANCE()

    # Set curve degree
    curve.degree = 3

    # Set control points
    curve.ctrlpts = CONTROL_POINTS

    # Set knot vector
    curve.knotvector = [0.0, 0.0, 0.0, 0.0, 0.33, 0.66, 1.0, 1.0, 1.0, 1.0]

    # Evaluate curve
    evalpt = curve.curvept(0.6)

    # Evaluation result
    res = [32.143, 14.328]

    assert abs(evalpt[0] - res[0]) < GEOMDL_DELTA
    assert abs(evalpt[1] - res[1]) < GEOMDL_DELTA


def test_bspline_curve2d_eval5():
    # Create a curve instance
    curve = OBJECT_INSTANCE()

    # Set curve degree
    curve.degree = 3

    # Set control points
    curve.ctrlpts = CONTROL_POINTS

    # Set knot vector
    curve.knotvector = [0.0, 0.0, 0.0, 0.0, 0.33, 0.66, 1.0, 1.0, 1.0, 1.0]

    # Evaluate curve
    evalpt = curve.curvept(1.0)

    # Evaluation result
    res = [50.0, 5.0]

    assert abs(evalpt[0] - res[0]) < GEOMDL_DELTA
    assert abs(evalpt[1] - res[1]) < GEOMDL_DELTA


def test_bspline_curve2d_insert_knot1():
    # Create a curve instance
    curve = OBJECT_INSTANCE()

    # Set curve degree
    curve.degree = 3

    # Set control points
    curve.ctrlpts = CONTROL_POINTS

    # Set knot vector
    curve.knotvector = [0.0, 0.0, 0.0, 0.0, 0.33, 0.66, 1.0, 1.0, 1.0, 1.0]

    # Set evaluation parameter
    u = 0.3

    # Insert knot
    curve.insert_knot(u)

    # Evaluate curve at the given parameter
    evalpt = curve.curvept(u)

    # Evaluation result
    res = [18.617, 13.377]

    assert abs(evalpt[0] - res[0]) < GEOMDL_DELTA
    assert abs(evalpt[1] - res[1]) < GEOMDL_DELTA


def test_bspline_curve2d_insert_knot2():
    # Create a curve instance
    curve = OBJECT_INSTANCE()

    # Set curve degree
    curve.degree = 3

    # Set control points
    curve.ctrlpts = CONTROL_POINTS

    # Set knot vector
    curve.knotvector = [0.0, 0.0, 0.0, 0.0, 0.33, 0.66, 1.0, 1.0, 1.0, 1.0]

    # Set evaluation parameter
    u = 0.6

    # Insert knot
    curve.insert_knot(u)

    # Evaluate curve at the given parameter
    evalpt = curve.curvept(u)

    # Evaluation result
    res = [32.143, 14.328]

    assert abs(evalpt[0] - res[0]) < GEOMDL_DELTA
    assert abs(evalpt[1] - res[1]) < GEOMDL_DELTA


def test_bspline_curve2d_insert_knot3():
    # Create a curve instance
    curve = OBJECT_INSTANCE()

    # Set curve degree
    curve.degree = 3

    # Set control points
    curve.ctrlpts = CONTROL_POINTS

    # Set knot vector
    curve.knotvector = [0.0, 0.0, 0.0, 0.0, 0.33, 0.66, 1.0, 1.0, 1.0, 1.0]

    # Set evaluation parameter
    u = 0.6

    # Insert knot
    curve.insert_knot(u, 2)

    # Evaluate curve at the given parameter
    evalpt = curve.curvept(u)

    # Evaluation result
    res = [32.143, 14.328]

    assert abs(evalpt[0] - res[0]) < GEOMDL_DELTA
    assert abs(evalpt[1] - res[1]) < GEOMDL_DELTA


def test_bspline_curve2d_insert_knot4():
    # Create a curve instance
    curve = OBJECT_INSTANCE()

    # Set curve degree
    curve.degree = 3

    # Set control points
    curve.ctrlpts = CONTROL_POINTS

    # Set knot vector
    curve.knotvector = [0.0, 0.0, 0.0, 0.0, 0.33, 0.66, 1.0, 1.0, 1.0, 1.0]

    # Set evaluation parameter
    u = 0.6

    # Insert knot
    curve.insert_knot(u, 2)

    assert curve.knotvector[5] == u
