/*
 * =============================================================================
 *
 *       Filename:  main.cpp
 *
 *    Description:  类的描述
 *
 *        Version:  1.0
 *        Created:  2021年07月26日
 *       Revision:  1
 *       Compiler:  gcc
 *
 *         Author:  kevin.wang
 *   Organization:
 *
 * =============================================================================
 */

#include <cstdio>
#include <cstdlib>
#include <iostream>

extern "C" {
int getVersion() { return 100; }
int addAlgorithm(int a, int b) { return a + b; }
bool getFlag(int value) {
        if (value > 10)
                return true;
        else
                return false;
}

const char *dispName(const char *name) {
        printf("%s\n", name);
        static std::string s(name);
        s = s + " help";
        return const_cast<const char *>(s.c_str());
}
}
