#include <pybind11/pybind11.h>
/*
<%
setup_pybind11(cfg)
%>
*/
namespace py = pybind11;

int add(int i = 1, int j = 2) {
    return i + j;
}

PYBIND11_MODULE(example, m) {
    m.doc() = "pybind11 example"; // optional module docstring

    m.def("add", &add, "A function which adds two numbers",
      py::arg("i") = 1, py::arg("j") = 2);
}
