#!/bin/bash
#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
    if (!PyList_Check(p))
    {
        printf("Invalid List Object\n");
        return;
    }
    Py_ssize_t size = PyList_Size(p);
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
    for (int i = 0; i < size; i++)
    {
        printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    if (!PyBytes_Check(p))
    {
        printf("Invalid Bytes Object\n");
        return;
    }
    Py_ssize_t size = PyBytes_Size(p);
    printf("[*] Python bytes info\n");
    printf("[*] Size of the Python Bytes = %ld\n", size);
    printf("[*] Tying to print the first %ld bytes:\n", size > 10 ? 10 : size);
    char *str = PyBytes_AsString(p);
    for (int i = 0; i < size && i < 10; i++)
    {
        printf("%02x ", str[i] & 0xff);
    }
    puts("");
}

