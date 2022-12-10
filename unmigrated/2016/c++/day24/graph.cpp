#include "graph.h"
#include "node.h"

#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>

Graph::Graph(std::string filename) {
    std::string line;
    std::ifstream infile(filename);

    int y = 0;
    while(getline(infile, line)) {
        for (int x=0; x<line.size(); x++) {
            Node* n = new Node(x, y, line[x]);
            node_map[x][y] = n;

            if (line[x] != '#' && line[x] != '.') {
                specials[line[x]] = n;
            }
        }
        y++;
    }
    infile.close();

    for (auto& itr: node_map) {
        for (auto& itr2: itr.second) {
            Node* n = itr2.second;
            for (auto& pair: {std::pair<int,int>{-1,0}, {1,0}, {0,-1}, {0, 1}}) {
                
                int x = n->x + pair.first;
                int y = n->y + pair.second;
                
                if (node_map.find(x) != node_map.end() && node_map[x].find(y) != node_map[x].end()) {
                    Node* neighbor = node_map[x][y];
                    if (!neighbor->isWall()) {
                        n->neighbors.push_back(neighbor);
                    }
                }
            }
        }
    }

}

Graph::~Graph() {
    for (auto& itr: node_map) {
        for (auto& itr2: itr.second) {
            Node* n = itr2.second;
            delete n;
        }
    }
}