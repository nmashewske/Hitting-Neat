/*
 * _mem.c
 * 
 * Copyright 2017 Matthew Mashewske <matthew@matthew-W65-67SJ>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


#include <stdio.h>
#include <Python.h>
#include "mem.h"



static PyObject *mem_health2(PyObject *self, PyObject *args);
static PyObject *mem_health1(PyObject *self, PyObject *args);
static PyObject *mem_comboStage1(PyObject *self, PyObject *args);
static PyObject *mem_comboDamage1(PyObject *self, PyObject *args);
PyMODINIT_FUNC PyInit_mem(void);
PyMODINIT_FUNC PyInit__mem(void);

static char module_docstring[] =
    "This module provides methods to read the memory values from skullgirls";
static char health2_docstring[] =
    "Read the memory value of player two's health";
static char health1_docstring[] =
    "Read the memory value of player ones's health";
static char comboStage1_docstring[] =
    "Read the memory value of player ones's combo stage";
static char comboDamage1_docstring[] =
    "Read the memory value of player ones's combo's damage";

static PyMethodDef module_methods[] = {
    {"health2", mem_health2, METH_VARARGS, health2_docstring},
    {"health1", mem_health1, METH_VARARGS, health1_docstring},
    {"comboStage1", mem_comboStage1, METH_VARARGS, comboStage1_docstring},
    {"comboDamage1", mem_comboDamage1, METH_VARARGS, comboDamage1_docstring},
    {NULL, NULL, 0, NULL}
};

static PyObject *mem_health2(PyObject *self, PyObject *args)
{   
    long pid;
    if (!PyArg_ParseTuple(args, "l", &pid))
        return NULL;
    
    
    double f = (double)health2(pid);
    PyObject *ret = PyFloat_FromDouble(f);
    return ret;
}

static PyObject *mem_health1(PyObject *self, PyObject *args)
{   
    long pid;
    if (!PyArg_ParseTuple(args, "l", &pid))
        return NULL;
    
    
    double f = (double)health1(pid);
    PyObject *ret = PyFloat_FromDouble(f);
    return ret;
}
static PyObject *mem_comboStage1(PyObject *self, PyObject *args)
{   
    long pid;
    if (!PyArg_ParseTuple(args, "l", &pid))
        return NULL;
    
    
    long i = (long)comboStage1(pid);
    PyObject *ret = PyLong_FromLong(i);
    return ret;
}
static PyObject *mem_comboDamage1(PyObject *self, PyObject *args)
{   
    long pid;
    if (!PyArg_ParseTuple(args, "l", &pid))
        return NULL;
    
    
    double f = (double)comboDamage1(pid);
    PyObject *ret = PyFloat_FromDouble(f);
    return ret;
}
static struct PyModuleDef mem =
{
    PyModuleDef_HEAD_INIT,
    "mem", /* name of module */
    module_docstring,          /* module documentation, may be NULL */
    0,          /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    module_methods
};

int
main(int argc, char *argv[])
{
    wchar_t *program = Py_DecodeLocale(argv[0], NULL);
    if (program == NULL) {
        fprintf(stderr, "Fatal error: cannot decode argv[0]\n");
        exit(1);
    }

    /* Add a built-in module, before Py_Initialize */
    PyImport_AppendInittab("mem", PyInit_mem);

    /* Pass argv[0] to the Python interpreter */
    Py_SetProgramName(program);

    /* Initialize the Python interpreter.  Required. */
    Py_Initialize();

    /* Optionally import the module; alternatively,
       import can be deferred until the embedded script
       imports it. */
    PyImport_ImportModule("mem");

    PyMem_RawFree(program);
    return 0;
}


PyMODINIT_FUNC
PyInit_mem(void)
{
    return PyModuleDef_Init(&mem);
}

PyMODINIT_FUNC
PyInit__mem(void)
{
    return PyModule_Create(&mem);
}
