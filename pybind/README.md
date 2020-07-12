### reference:
	http://people.duke.edu/~ccc14/sta-663-2020/notebooks/S13_pybind11.html
	https://pybind11.readthedocs.io/en/stable/index.html

----------- example.cpp ----------------
```
#include <pybind11/pybind11.h>
namespace py = pybind11;

int add(int i = 1, int j = 2) {
    return i + j;
}

PYBIND11_MODULE(example, m) {
    m.doc() = "pybind11 example"; // optional module docstring

	m.def("add", &add, "A function which adds two numbers",
      py::arg("i") = 1, py::arg("j") = 2);
}
```
----------------------------------------

### build manually on linux

	c++ -O3 -Wall -shared -std=c++11 -fPIC `python3 -m pybind11 --includes` example.cpp -o example`python3-config --extension-suffix`

### build manaully on mac

	c++ -O3 -Wall -shared -std=c++11 -undefined dynamic_lookup `python3 -m pybind11 --includes` example.cpp -o example`python3-config --extension-suffix`

	note the '-undefined dynamic_lookup' extra 

### to use cppimport 
add 
```
/* 
<%
setup_pybind11(cfg)
%>
*/
```
to the example.cpp code, then directly import

	import cppimport
	example = cppimport.imp('example')  ## build once here.
	example.add(3, 5)


