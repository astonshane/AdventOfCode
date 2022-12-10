#ifndef __node_h__
#define __node_h__

#include <string>
#include <vector>

class Node {
    public:
        Node(int x, int y, char name);

        bool isWall() {return name == '#';}

        char name;
        int x;
        int y;
        bool visited;
        int distance;
        std::vector<Node*> neighbors;
};

#endif