#include "factorial.h"

/*
 * Define the "factorial" function exposed by the module
 */
static PyMethodDef factorial_methods[] = {
    {"factorial", (PyCFunction)(void (*)(void))factorial, METH_FASTCALL},
    {NULL, NULL, 0, NULL}};

/**
 * Define the "factorial" module
 */
static struct PyModuleDef factorial_module = {
    PyModuleDef_HEAD_INIT,
    "factorial",
    NULL,
    0,
    factorial_methods,
};

/**
 * Calculate the factorial of a number between 0 and 16
 */
PyObject *factorial(PyObject *self, PyObject *const *args, Py_ssize_t nargs)
{
    unsigned long input;

    /* Check we received a single integer between 0 and 16 */
    if (nargs != 1 || (input = PyLong_AsUnsignedLong(args[0])) < 0 || input > 16)
    {
        PyErr_SetString(PyExc_TypeError, "Invalid input");
        return NULL;
    }

    /* Naive factorial algorithm */
    unsigned long result = 1;
    for (unsigned long i = 1; i <= input; i++)
    {
        result *= i;
    }

    return PyLong_FromUnsignedLong(result);
}

/**
 * Initialise the "factorial" module
 */
PyMODINIT_FUNC PyInit_factorial(void)
{
    return PyModuleDef_Init(&factorial_module);
}