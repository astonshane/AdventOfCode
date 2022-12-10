#include <iostream>
#include "graph.h"
#include "node.h"
#include <unordered_map>
#include <algorithm>
#include <limits.h>
#include <iomanip>


Node* next(std::vector<Node*>& nodes) {
    Node* next = nullptr;
    for (Node* n : nodes) {
        if (n->visited) {
            continue;
        }
        if (!next || n->distance < next->distance) {
            next = n;
        }
    }
    return next;
}

int dijkstras(Graph& g, char start_name, char goal_name) {
    g.specials[start_name]->distance = 0;
    
    std::vector<Node*> pq;
    for (auto& itr: g.node_map) {
        for (auto& itr2: itr.second) {
            Node* n = itr2.second;
            pq.push_back(n);
        }
    } 
    

    while (true) {
        Node* current = next(pq);
        if (current->name == goal_name) {
            return current->distance;
        }

        for (Node* neigbor: current->neighbors) {
            int tenative_dist = current->distance + 1;
            if (tenative_dist < neigbor->distance) {
                neigbor->distance = tenative_dist;
            } 
        }
        current->visited = true;
    }
    std::cerr << "uh oh. not found" << std::endl;
    return -1;
}

int distanceBetween(char start, char end, std::map<char, std::map<char, int>>& distances) {
    if (distances.find(start) == distances.end() || distances[start].find(end) == distances[start].end()) {
        Graph g("input.txt");
        int distance = dijkstras(g, start, end);
        distances[start][end] = distance;
        distances[end][start] = distance;
    }

    return distances[start][end];
}

int shortestPath(std::string numbers, std::map<char, std::map<char, int>>& distances, bool endZero) {
    int shortest = INT_MAX;
    
    std::sort(numbers.begin(), numbers.end());

    int count = 0;
    do {
        std::string order = "0" + numbers;
        if (endZero)
            order += "0";
        int distance = 0;
        for (int i=0; i<order.size()-1; i++) {
            distance += distanceBetween(order[i], order[i+1], distances);
        }
        if (distance < shortest){
            std::cout << count << "  " << order << "  old shortest: " << shortest << " new shortest: " << distance << std::endl;
            shortest = distance;
        }
        count += 1;
    } while (std::next_permutation(numbers.begin(), numbers.end()));
    return shortest;
}

int main() {
    
    std::map<char, std::map<char, int>> distances;

    std::string numbers = "";
    {
        Graph g("input.txt");
        for (auto& itr: g.specials) {
            numbers += itr.first;
        }
    }
    
    int part1 = shortestPath(numbers, distances, false);
    std::cout << "Part1: " << part1 << std::endl;
    int part2 = shortestPath(numbers, distances, true);
    std::cout << "Part2: " << part2 << std::endl;

    /*std::cout << std::setw(5) << "_";
    for (auto& itr: distances) {
        std::cout << std::setw(5) << itr.first;
        distances[itr.first][itr.first] = 0;
    }
    std::cout << std::endl;

    for (auto& itr: distances) {
        std::cout << std::setw(5) << itr.first;
        for (auto& itr2: itr.second) {
            std::cout << std::setw(5) <<  itr2.second;
        }
        std::cout << std::endl;
    }*/

    return 0;
}