#ifndef __graph_h__
#define __graph_h__

#include "node.h"
#include <string>
#include <map>
#include <unordered_map>

class Graph {
    public:
        Graph(std::string filename);
        ~Graph();

        std::map<int, std::map<int, Node*>> node_map;
        std::unordered_map<char, Node*> specials;
};

#endif