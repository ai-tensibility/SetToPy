#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "settopy.cpp"

namespace py = pybind11;

PYBIND11_MODULE(SetTopy, m) {
    py::class_<SetTopy>(m, "SetTopy")
        .def(py::init<>())
        .def("add", &SetTopy::add)
        .def("contains", &SetTopy::contains)
        .def("remove", &SetTopy::remove)
        .def("get_elements", &SetTopy::get_elements)
        .def("size", &SetTopy::size);
}
