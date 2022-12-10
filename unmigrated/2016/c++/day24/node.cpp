#include "node.h"
#include <limits.h>

Node::Node(int x, int y, char name) {
    this->x = x;
    this->y = y;
    this->name = name;
    this->visited = false;
    this->distance = INT_MAX;
}