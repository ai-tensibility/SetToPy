#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <sstream>
#include "settopy.cpp" // Ensure this includes the declaration of SetElement

namespace py = pybind11;

PYBIND11_MODULE(settopy_bindings, m) {
    py::class_<SetElement>(m, "SetElement")
        .def(py::init<>())
        .def_readwrite("x", &SetElement::x)
        .def_readwrite("y", &SetElement::y)
        .def_readwrite("value", &SetElement::value)
        .def("__repr__",
             [](const SetElement &e) {
                 std::stringstream ss;
                 ss << "{" << "x: " << e.x << ", y: " << e.y << ", value: " << e.value << "}";
                 return ss.str();
             });

    py::class_<SetTopy>(m, "SetTopy")
        .def(py::init<>())
        .def("add", &SetTopy::add)
        .def("contains", &SetTopy::contains)
        .def("remove", &SetTopy::remove)
        .def("get_elements", &SetTopy::get_elements)
        .def("size", &SetTopy::size);
}
