/*
 * =====================================================================================
 *
 *       Filename:  main.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  2013年12月04日 14时10分05秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
#include <cstdlib>
#include <cstdio>

#include "python2.6/Python.h"

/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  main
 *  Description:  
 * =====================================================================================
 */
	int
main ( int argc, char *argv[] )
{
	printf ( "Python and C Plus Plus program\n" );
	Py_Initialize();

	PyObject *pmodule = NULL;
	PyObject *pfunc   = NULL;
	PyObject *pname   = NULL;
	PyObject *pdict   = NULL;

	if ( !Py_IsInitialized() )
	{
		printf ("bad no initialization of python env\n");
		goto Error;
	}
	if ( PyRun_SimpleString("import sys") == -1 )
	{
		printf("error import sys\n");
		goto Error;
	}
	if ( PyRun_SimpleString("sys.path.append('./')") == -1 )
	{
		printf("error append path\n");
		goto Error;
	}

	pname   = PyString_FromString("globle"); 
	pmodule = PyImport_Import(pname);
	if ( !pmodule )
	{
		printf("bad no found module\n");
		goto Error;
	}

	pdict = PyModule_GetDict(pmodule);
	if ( !pdict )
	{ 
		printf("bad no get dict\n");
		goto Error;
	}

	pfunc   = PyDict_GetItemString(pdict,"Print_Version");
	if ( pfunc == NULL ) printf("bad no found func\n");
	PyEval_CallObject(pfunc,NULL);

	Py_DECREF(pmodule);
	Py_DECREF(pfunc);
	Py_DECREF(pname);
	Py_DECREF(pdict);

Error:
	Py_Finalize();
	return EXIT_SUCCESS;
}				/* ----------  end of function main  ---------- */


